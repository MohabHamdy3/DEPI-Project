import streamlit as st
import gdown
import os


# Path where you want to store the model locally
MODEL_PATH = "models/best_model.pth"
DRIVE_FILE_ID = "136oMq1IwodcijxodONLjN8ipGaokSfCC"
MODEL_DIR = os.path.dirname(MODEL_PATH)

os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model..."):
        url = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)


# -------------------------------------------
# Page Configuration
# -------------------------------------------
st.set_page_config(
    page_title="Deepfake Detector",
    layout="wide"
)

# -------------------------------------------
# Dashboard Page (Main App)
# -------------------------------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 48px;
            text-align: center;
            font-weight: bold;
            margin-bottom: -10px;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            letter-spacing: 2px;
            text-transform: uppercase;
            font-family: 'Arial', sans-serif;
            line-height: 1.2;
            
        }
        .sub-title {
            font-size: 20px;
            text-align: center;
            margin-bottom: 30px;
            font-family: 'Arial', sans-serif;
        }
        .center-img {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='main-title'>Deepfake Detection System</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<h5 class='sub-title'>AI-powered tool for detecting manipulated and fake videos</h5>", unsafe_allow_html=True)

# Large Centered Image
st.markdown(
    '<div class="center-img"><img src="https://cdn-icons-png.flaticon.com/512/10609/10609042.png" width="260"></div>',
    unsafe_allow_html=True,
)

st.divider()

# Features
st.subheader("Features")

st.write("""
- **AI Deepfake Detection**
- **Video Upload & Real-Time Analysis**
- **Model & Data Visualization**
- **Project Documentation and Details**
""")

st.divider()

# Navigation Hint
st.info("Use the sidebar on the left to navigate between pages.")


# Footer
st.markdown("---")
st.markdown("<p class='sub-title'>&copy; 2025 Deepfake Detection System | All rights reserved</p>", unsafe_allow_html=True)

