# dataset.py
import os
import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as T

from config import CACHE_DIR, N_FRAMES, IMG_SIZE
from utils import sample_frames_from_video, crop_face_or_center

# --- Transforms Definition (Train & Val) ---
train_transforms = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.RandomHorizontalFlip(),
    T.ColorJitter(brightness=0.1, contrast=0.1),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

val_transforms = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def cache_video_to_npz(video_path):
    video_id = os.path.splitext(os.path.basename(video_path))[0]
    out_path = os.path.join(CACHE_DIR, f"{video_id}.npz")

    if os.path.exists(out_path):
        return out_path   # DON'T recache

    frames = sample_frames_from_video(video_path)
    
    # Handle broken/empty videos
    if len(frames) == 0:
        arr = np.zeros((N_FRAMES, IMG_SIZE, IMG_SIZE, 3), np.uint8)
        np.savez_compressed(out_path, frames=arr)
        return out_path

    # Pad if not enough frames
    if len(frames) < N_FRAMES:
        while len(frames) < N_FRAMES:
            frames.append(frames[-1])

    processed = [crop_face_or_center(f, IMG_SIZE) for f in frames[:N_FRAMES]]
    arr = np.stack(processed, axis=0).astype(np.uint8)
    np.savez_compressed(out_path, frames=arr)
    return out_path

class CachedVideoDataset(Dataset):
    def __init__(self, video_list, transforms=None):
        self.items = video_list
        self.transforms = transforms

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        video_path, label = self.items[idx]
        vid = os.path.splitext(os.path.basename(video_path))[0]
        npz_path = os.path.join(CACHE_DIR, f"{vid}.npz")

        # Create cache if strictly needed (lazy loading safety)
        if not os.path.exists(npz_path):
            npz_path = cache_video_to_npz(video_path)

        try:
            data = np.load(npz_path)
            arr = data["frames"]
        except:
            # Fallback for corrupted cache
            arr = np.zeros((N_FRAMES, IMG_SIZE, IMG_SIZE, 3), np.uint8)

        processed = []
        if self.transforms:
            for f in arr:
                processed.append(self.transforms(Image.fromarray(f)))
        else:
            # Default transform to tensor if none provided
            to_tensor = T.ToTensor()
            processed = [to_tensor(f) for f in arr]
            
        frames = torch.stack(processed)           # (N_FRAMES, 3, H, W)
        # frames = frames.unsqueeze(0)              # (1, N_FRAMES, 3, H, W)

        labels = torch.tensor(label, dtype=torch.float32)
        return frames, labels