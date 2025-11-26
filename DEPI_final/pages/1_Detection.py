import streamlit as st
import tempfile
import os
import torch
import time
import numpy as np
from inference import load_model_from_path, predict_video_with_model
from utils import sample_frames_from_video, crop_face_or_center
from config import N_FRAMES, IMG_SIZE

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_PATH = "models/best_model.pth"

# ---------------------------------------------------------
# Load the model once
# ---------------------------------------------------------
@st.cache_resource
def load_engine():
    if not os.path.exists(MODEL_PATH):
        return None
    return load_model_from_path(MODEL_PATH, device=DEVICE)

model = load_engine()

# ---------------------------------------------------------
# SIDEBAR CONTENT
# ---------------------------------------------------------
st.sidebar.header("⚙ Detection Settings")

# THRESHOLD SLIDER
threshold = st.sidebar.slider(
    "Fake Probability Threshold",
    min_value=0.1,
    max_value=0.9,
    value=0.5,
    step=0.01,
    help="If the model's output probability is above this value, the video is classified as FAKE."
)

st.sidebar.write(f"Current threshold: **{threshold:.2f}**")

st.sidebar.markdown("---")

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("Deepfake Detection System")

st.markdown("""
Upload a video to analyze whether it is **Real** or **Fake**.
""")

st.write("---")

# ---------------------------------------------------------
# Video Upload
# ---------------------------------------------------------
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file:
    st.video(uploaded_file)

# ---------------------------------------------------------
# Preview frames
# ---------------------------------------------------------
def show_preview_frames(video_path):
    st.subheader("Preview Sampled Frames")

    frames = sample_frames_from_video(video_path, n_frames=6)

    if len(frames) == 0:
        st.warning("Could not extract frames from this video.")
        return

    cols = st.columns(3)
    idx = 0
    for i in range(2):
        for j in range(3):
            if idx < len(frames):
                cols[j].image(
                    frames[idx],
                    caption=f"Frame {idx+1}",
                    use_container_width=True
                )
                idx += 1

# ---------------------------------------------------------
# Analyze Button
# ---------------------------------------------------------
if uploaded_file and st.button("Analyze Video"):

    if model is None:
        st.error("Model not found. Make sure your weights file exists.")
    else:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        tfile.close()

        show_preview_frames(video_path)

        st.write("---")

        progress = st.progress(0)
        status = st.empty()
        status.text("Processing video...")

        try:
            start = time.time()

            pred, prob, err = predict_video_with_model(
                model,
                video_path,
                device=DEVICE,
                n_frames=N_FRAMES
            )

            progress.progress(100)
            status.empty()

            st.subheader("Detection Result")
            st.write("---")

            # APPLY THRESHOLD
            label = 1 if prob >= threshold else 0

            col1, col2 = st.columns(2)

            with col1:
                if label == 1:
                    st.error(f"FAKE")
                else:
                    st.success(f"REAL")

            with col2:
                st.metric("Fake Probability", f"{prob:.4f}")
                st.write(f"Processing Time: **{time.time() - start:.2f}s**")

            if err:
                st.warning(err)

        finally:
            os.unlink(video_path)
