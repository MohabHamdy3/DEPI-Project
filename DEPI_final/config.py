# config.py
import os
import torch
import random
import numpy as np

# --- Paths ---
DATA_ROOT = "./FaceForensics++_C23"
CACHE_DIR = "./cache_frames"
SAVE_DIR = "./models"

# --- Create Directories ---
os.makedirs(DATA_ROOT, exist_ok=True)
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
# --- Enable cudnn benchmark for performance ---
if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = True

RANDOM_SEED = 42
NUM_WORKERS = 0 # Set to 0 for Windows compatibility (you can increase this on Linux/Mac)
PIN_MEMORY = True

def seed_everything(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

seed_everything()