import streamlit as st
import tempfile
import os
import torch
import time

# 🔥 التعديل هنا: الاستدعاء من inference بدلاً من model
from inference import load_model_from_path, predict_video_with_model
# بنجيب N_FRAMES من config عشان نستخدمها
from config import N_FRAMES

# ---------------------------------------------------------
# 1. إعدادات الصفحة والتصميم
# ---------------------------------------------------------
st.set_page_config(
    page_title="Deepfake Detector",
    page_icon="🛡️",
    layout="centered"
)

st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF0000;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. تحميل الموديل (يتم مرة واحدة ويتحفظ في الكاش)
# ---------------------------------------------------------
# ❗ غير المسار ده لمسار الموديل عندك
MODEL_PATH = r"F:\Downloads\Fake detector\best_model (3).pth" 
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

@st.cache_resource
def load_engine():
    if not os.path.exists(MODEL_PATH):
        return None
    try:
        # استدعاء دالة التحميل من inference.py
        model = load_model_from_path(MODEL_PATH, device=DEVICE)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_engine()

# ---------------------------------------------------------
# 3. القائمة الجانبية (Sidebar)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/10609/10609042.png", width=100)
    st.title("Settings")
    confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.05)
    st.info(f"Running on: {DEVICE}")

# ---------------------------------------------------------
# 4. الواجهة الرئيسية
# ---------------------------------------------------------
st.title("🛡️ Deepfake Detection System")
st.markdown("### Upload a video to check if it's **Real** or **Fake**")

uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("🔍 Analyze Video"):
        if model is None:
            st.error(f"❌ Model file not found at: `{MODEL_PATH}`")
        else:
            # حفظ الفيديو في ملف مؤقت بنفس الامتداد
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1])
            tfile.write(uploaded_file.read())
            video_path = tfile.name
            tfile.close()

            progress_bar = st.progress(0)
            status_text = st.empty()
            status_text.text("Processing video frames...")
            
            try:
                start_time = time.time()
                
                # استدعاء دالة التوقع من inference.py
                binary_pred, prob, error_msg = predict_video_with_model(
                    model, 
                    video_path, 
                    device=DEVICE, 
                    n_frames=N_FRAMES,
                    thresh=confidence_threshold
                )
                
                progress_bar.progress(100)
                status_text.empty()

                if error_msg:
                    st.warning(f"⚠️ Analysis Warning: {error_msg}")
                    st.write("Try uploading a video with a clearer face.")
                else:
                    st.divider()
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if binary_pred == 1:
                            st.error("## 🚨 FAKE")
                            st.image("https://cdn-icons-png.flaticon.com/512/6663/6663906.png", width=150)
                        else:
                            st.success("## ✅ REAL")
                            st.image("https://cdn-icons-png.flaticon.com/512/14600/14600295.png", width=150)
                    
                    with col2:
                        st.metric("Confidence (Fake Probability)", f"{prob:.4f}")
                        st.write(f"**Time:** {time.time() - start_time:.2f}s")
                        
                        if binary_pred == 1:
                            st.warning(f"Model is **{prob*100:.1f}%** sure this is FAKE.")
                        else:
                            st.success(f"Model is **{(1-prob)*100:.1f}%** sure this is REAL.")

            except Exception as e:
                st.error(f"System Error: {e}")
            
            finally:
                # مسح الملف المؤقت
                if os.path.exists(video_path):
                    os.unlink(video_path)