# config.py
import os
import torch
import random
import numpy as np

# --- Paths (عدل المسارات دي حسب جهازك) ---
DATA_ROOT = r"E:\Datasets\FaceForensics++_C23"  # مثال: غير المسار ده لمسار الداتا عندك
CACHE_DIR = "./cache_frames"         # الكاش هيتحفظ في نفس فولدر المشروع
SAVE_DIR = "./models"                # الموديل هيتحفظ هنا

# تأكد من إنشاء الفولدرات
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(SAVE_DIR, exist_ok=True)

# --- Hyperparameters ---
REAL_SUBFOLDER = "original"
FAKE_TYPES = ["Deepfakes", "Face2Face", "FaceSwap", "FaceShifter"]
VIDEO_EXTS = [".mp4", ".avi", ".mov", ".mkv"]

N_FRAMES = 10
IMG_SIZE = 224
BATCH_VIDEO = 8
EPOCHS = 20
LR = 1e-4

# --- Device & Seed ---
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
# لزيادة السرعة لو كارت الشاشة NVIDIA
if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = True

RANDOM_SEED = 42
NUM_WORKERS = 4  # خليها 0 لو شغال ويندوز وحصل مشاكل، بس 4 أسرع
PIN_MEMORY = True

def seed_everything(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

seed_everything()