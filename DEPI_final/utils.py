# utils.py
import os
import glob
import cv2
import numpy as np
from config import VIDEO_EXTS, IMG_SIZE, N_FRAMES

# تحميل ملف الهار كاسكيد للوجه
haar_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haar_path)

def list_videos_in_dir(dir_path):
    vids = []
    if not os.path.exists(dir_path):
        return []
    # البحث المباشر
    for ext in VIDEO_EXTS:
        vids.extend(glob.glob(os.path.join(dir_path, f"*{ext}")))
    # البحث داخل المجلدات الفرعية
    for sub in sorted(os.listdir(dir_path)):
        p = os.path.join(dir_path, sub)
        if os.path.isdir(p):
            for ext in VIDEO_EXTS:
                vids.extend(glob.glob(os.path.join(p, f"*{ext}")))
    return sorted(list(set(vids)))

def sample_frames_from_video(video_path, n_frames=N_FRAMES):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []

    if total <= 0:
        # Fallback if frame count is unknown
        for _ in range(n_frames):
            ret, frame = cap.read()
            if ret:
                frames.append(frame[..., ::-1]) # BGR to RGB
        cap.release()
        return frames

    indices = np.linspace(0, total - 1, n_frames, dtype=int)
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
        ret, frame = cap.read()
        if ret:
            frames.append(frame[..., ::-1])

    cap.release()
    return frames

def crop_face_or_center(frame, out_size=IMG_SIZE):
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        x, y, fw, fh = max(faces, key=lambda r: r[2] * r[3])
        cx, cy = x + fw // 2, y + fh // 2
        side = int(max(fw, fh) * 1.4)
        x1 = max(0, cx - side // 2)
        y1 = max(0, cy - side // 2)
        face = frame[y1:y1 + side, x1:x1 + side]
    else:
        side = min(h, w)
        x1 = (w - side) // 2
        y1 = (h - side) // 2
        face = frame[y1:y1 + side, x1:x1 + side]

    return cv2.resize(face, (out_size, out_size))
