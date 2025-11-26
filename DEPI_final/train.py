# train.py
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

# Import custom modules
import config
from utils import list_videos_in_dir , sample_frames_from_video
from dataset import CachedVideoDataset, cache_video_to_npz, train_transforms, val_transforms
from model import VideoModel

# --- Build Dataset List ---
def build_balanced_video_list(root, real_sub, fake_types, per_fake=250, real_limit=1000):
    all_videos = []
    
    real_path = os.path.join(root, real_sub)
    real_v = list_videos_in_dir(real_path)[:real_limit]
    all_videos.extend([(p, 0) for p in real_v])

    for i, ftype in enumerate(fake_types):
        fake_path = os.path.join(root, ftype)
        fv = list_videos_in_dir(fake_path)
        subset = fv[i * per_fake:(i + 1) * per_fake]
        print(f"Type: {ftype} | Taking: {len(subset)}")
        all_videos.extend([(p, 1) for p in subset])

    print(f"Total -> Real: {len(real_v)}, Fake: {len(all_videos)-len(real_v)}, Total: {len(all_videos)}")
    return all_videos

# --- Evaluation Function ---
@torch.no_grad()
def evaluate(model, loader, criterion):
    model.eval()
    y_true, y_scores = [], []
    total_loss = 0

    for frames, labels in loader:
        frames, labels = frames.to(config.DEVICE), labels.to(config.DEVICE)
        outputs = model(frames)
        loss = criterion(outputs, labels)
        total_loss += loss.item() * frames.size(0)

        probs = torch.sigmoid(outputs)
        y_true.extend(labels.cpu().numpy())
        y_scores.extend(probs.cpu().numpy())

    y_true = np.array(y_true)
    y_scores = np.array(y_scores)
    y_pred = (y_scores >= 0.5).astype(int)
    
    # Avoid AUC error if only one class present in batch
    try:
        auc_val = roc_auc_score(y_true, y_scores)
    except:
        auc_val = 0.5

    return {
        "loss": total_loss / len(loader.dataset),
        "auc": auc_val,
        "acc": accuracy_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "prec": precision_score(y_true, y_pred, zero_division=0),
        "rec": recall_score(y_true, y_pred, zero_division=0)
    }

# --- Training Loop ---
def run_training(model, train_loader, val_loader):
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.AdamW(model.parameters(), lr=config.LR)

    train_losses, val_losses, val_aucs = [], [], []
    best_auc = -1

    for epoch in range(1, config.EPOCHS + 1):
        print(f"\n📌 Epoch {epoch}/{config.EPOCHS}")
        model.train()
        running_loss = 0

        loop = tqdm(train_loader, desc="Training")
        for frames, labels in loop:
            frames, labels = frames.to(config.DEVICE), labels.to(config.DEVICE)

            optimizer.zero_grad()
            # frames: (BATCH, 1, N_FRAMES, 3, H, W)
            # frames = frames.squeeze(1)   # → (BATCH, N_FRAMES, 3, H, W)
            # print(frames.shape)
            outputs = model(frames)
            labels = labels.view(-1)       # (B,) instead of (B,1)
            outputs = outputs.view(-1)     # (B,) instead of (B,)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * frames.size(0)
            loop.set_postfix(loss=loss.item())

        train_loss = running_loss / len(train_loader.dataset)
        train_losses.append(train_loss)

        metrics = evaluate(model, val_loader, criterion)
        val_losses.append(metrics["loss"])
        val_aucs.append(metrics["auc"])

        print(f"Train Loss: {train_loss:.4f}")
        print(f"Val Loss: {metrics['loss']:.4f}, AUC: {metrics['auc']:.4f}, Acc: {metrics['acc']:.4f}")

        if metrics["auc"] > best_auc:
            best_auc = metrics["auc"]
            torch.save(model.state_dict(), os.path.join(config.SAVE_DIR, "best_model.pth"))
            print("Saved best model")

    # Plotting
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(train_losses, label="Train Loss")
    plt.plot(val_losses, label="Val Loss")
    plt.title("Loss Curve")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(val_aucs, label="Val AUC", color="green")
    plt.title("AUC Curve")
    plt.legend()
    
    plt.savefig(os.path.join(config.SAVE_DIR, "training_plots.png"))
    plt.show()

    return best_auc

# --- Main ---
if __name__ == "__main__":
    # 1. Prepare Video List
    videos = build_balanced_video_list(
        config.DATA_ROOT, config.REAL_SUBFOLDER, config.FAKE_TYPES
    )

    if not videos:
        print(" No videos found! Check paths in config.py")
        exit()

    # 2. Pre-process / Cache (Optional but recommended)
    print("Checking cache...")
    for p, _ in tqdm(videos, desc="Caching"):
        cache_video_to_npz(p)

    print("Number of videos:", len(videos))
    for p, _ in videos:
        print("Checking:", p)
        frames = sample_frames_from_video(p)
        print("Frames read:", len(frames))
        break
    # 3. Split Data
    paths = [p for p, _ in videos]
    labels = [l for _, l in videos]

    train_idx, val_idx = train_test_split(
        range(len(paths)), test_size=0.2, stratify=labels, random_state=config.RANDOM_SEED
    )
    
    train_list = [videos[i] for i in train_idx]
    val_list   = [videos[i] for i in val_idx]

    # 4. Data Loaders
    train_ds = CachedVideoDataset(train_list, transforms=train_transforms)
    val_ds   = CachedVideoDataset(val_list, transforms=val_transforms)

    train_loader = DataLoader(
        train_ds, batch_size=config.BATCH_VIDEO, shuffle=True,
        num_workers=config.NUM_WORKERS, pin_memory=config.PIN_MEMORY
    )
    val_loader = DataLoader(
        val_ds, batch_size=config.BATCH_VIDEO, shuffle=False,
        num_workers=config.NUM_WORKERS, pin_memory=config.PIN_MEMORY
    )

    # 5. Model & Train
    print(f"Using Device: {config.DEVICE}")
    model = VideoModel(pretrained=True).to(config.DEVICE)
    # --- Check GPU info ---
    import torch
    print("CUDA Available:", torch.cuda.is_available())
    print("Number of GPUs:", torch.cuda.device_count())
    if torch.cuda.is_available():
        print("GPU Name:", torch.cuda.get_device_name(0))
    best_auc = run_training(model, train_loader, val_loader)
    print(f"\n Finished! Best AUC: {best_auc:.4f}")