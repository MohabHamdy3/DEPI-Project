# Deepfake Detection System

A powerful deep learning-based application designed to detect AI-generated fake videos (deepfakes) with high accuracy. This project includes a full pipeline: data preprocessing, model training, inference, and a Streamlit web interface for real-time video analysis.

---

## 🚀 Features
- Deepfake classification using a trained PyTorch model
- Frame extraction from uploaded videos
- Real-time prediction through Streamlit
- Modular and clean project structure
- GPU-compatible training and inference

---

## 📂 Project Structure
```
project/
│── models/
│   └── best_model.pth
│── inference.py
│── train.py
│── config.py
│── utils.py
│── streamlit_app.py
│── requirements.txt
│── README.md
```

---

## 🧠 Model Architecture
The model is a CNN-based classifier optimized for real vs. fake video frame detection. It has been trained using a balanced dataset with various augmentation strategies to improve robustness.

👉 **(Insert Model Architecture Image Here)**

---

## 📊 Model Performance
Below are the evaluation metrics obtained during testing.

### ✔ Accuracy
**87.76%**

### ✔ F1-Score
**88.68%**

### ✔ AUC
**97.67%**

### ✔ Latency per Image
**~2000ms**


![WhatsApp Image 2025-11-28 at 22 27 57_b7f5c00f](https://github.com/user-attachments/assets/4f2d8567-0b92-4ddc-a462-f00d289786f0)




![WhatsApp Image 2025-11-28 at 22 27 57_65926542](https://github.com/user-attachments/assets/4d5157c5-f169-4c8f-95cd-ddc1d248c9d3)




![WhatsApp Image 2025-11-28 at 22 27 57_cb85657f](https://github.com/user-attachments/assets/f5c3adb6-0adb-46a4-aab7-0bc623f9a977)




![WhatsApp Image 2025-11-28 at 22 27 58_1ac0ee0b](https://github.com/user-attachments/assets/588de5a4-69ab-402b-86eb-cebd27e42789)




![WhatsApp Image 2025-11-28 at 22 24 35_b7fc48e8](https://github.com/user-attachments/assets/06c60f73-5391-4b1b-8ab7-88f147ce8a87)


---

## ⚙️ Installation
```bash
git clone https://github.com/MohabHamdy3/DEPI-Project
cd project
pip install -r requirements.txt
```

---

## ▶️ Running the Streamlit App
```bash
streamlit run streamlit_app.py
```

Upload a video → Wait for processing → View predictions in real-time.

👉 **(Insert Screenshot of Streamlit Interface Here)**

---

## 📥 Inference Example (Python)
```python
from inference import load_model_from_path, predict_video_with_model

model = load_model_from_path('models/best_model.pth')
prediction = predict_video_with_model(model, 'test_video.mp4')
print(prediction)
```

---

## 📦 Requirements
```
torch
torchvision
opencv-python
numpy
streamlit
Pillow
```

---

## 📈 Training Process
The training script (`train.py`) contains:
- Data loading and preprocessing
- Frame sampling logic
- Model initialization
- Training loop + validation tracking

👉 **(Insert Training Graphs Here)**

---

## 🧪 Testing
You can test with:
```bash
python inference.py --video example.mp4
```

---

## 🛠 Future Improvements
- Reduce latency using model optimization (ONNX/TensorRT)
- Add face detection before frame classification
- Improve UI experience
- Add multi-class classification for different deepfake techniques

---

## 🙌 Acknowledgments
Special thanks to the datasets and open-source contributors that enabled this project.

---


---

## 📬 Contact
For questions or improvements:
**Mohab Hamdy**
GitHub: mohab-hamdy
Email: mohabhamdy41@gmail.com
