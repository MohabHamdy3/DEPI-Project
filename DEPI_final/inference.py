import torch
import torchvision.transforms as T
from PIL import Image
import os
import traceback

# استدعاء الإعدادات والموديل والأدوات من ملفاتهم
# تأكد إن ملفات config.py و utils.py موجودة في نفس الفولدر
from config import N_FRAMES, IMG_SIZE, DEVICE
from model import VideoModel
from utils import sample_frames_from_video, crop_face_or_center

# تجهيز الصور بنفس طريقة التدريب (بدون Data Augmentation)
inference_transforms = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def load_model_from_path(path, device=DEVICE):
    """
    دالة لتحميل الموديل المدرب من المسار المحدد
    """
    print(f"Loading model from: {path}")
    
    # بنعمل init للموديل بس pretrained=False عشان هنحمل أوزاننا الخاصة
    model = VideoModel(pretrained=False)
    
    # تحميل ملف الأوزان
    checkpoint = torch.load(path, map_location=device)
    
    # معالجة مشاكل مفاتيح الـ DataParallel (لو كان فيه 'module.' في الاسم)
    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']
    else:
        state_dict = checkpoint

    new_state_dict = {}
    for k, v in state_dict.items():
        name = k[7:] if k.startswith('module.') else k
        new_state_dict[name] = v
        
    model.load_state_dict(new_state_dict)
    model.to(device)
    model.eval() # وضع التقييم (بيوقف الـ Dropout والـ BatchNorm)
    return model

def predict_video_with_model(model, video_path, device=DEVICE, n_frames=N_FRAMES, thresh=0.5):
    """
    دالة بتاخد مسار الفيديو وبترجع التوقع
    Returns: (binary_pred (0/1), probability, error_message)
    """
    try:
        # 1. سحب الفريمات من الفيديو
        frames = sample_frames_from_video(video_path, n_frames=n_frames)
        if len(frames) == 0:
            return None, 0.0, "Could not read frames from video (or video is empty)."

        # 2. قص الوجوه وتجهيز الصور
        processed_frames = []
        for frame in frames:
            # قص الوجه
            face_img = crop_face_or_center(frame, out_size=IMG_SIZE)
            # تحويل لـ PIL
            pil_img = Image.fromarray(face_img)
            # تطبيق الـ Transforms
            tensor_img = inference_transforms(pil_img)
            processed_frames.append(tensor_img)
        
        # لو عدد الفريمات أقل من المطلوب بنكرر آخر فريم (Padding)
        while len(processed_frames) < n_frames:
            processed_frames.append(processed_frames[-1])
            
        # تجميعهم في Batch واحد
        # Shape: (1, Frames, Channels, Height, Width)
        input_tensor = torch.stack(processed_frames).unsqueeze(0).to(device)
        
        # 3. عمل التوقع
        with torch.no_grad():
            logits = model(input_tensor)
            prob = torch.sigmoid(logits).item()
            
        pred = 1 if prob >= thresh else 0
        return pred, prob, None

    except Exception as e:
        traceback.print_exc()
        return None, 0.0, str(e)