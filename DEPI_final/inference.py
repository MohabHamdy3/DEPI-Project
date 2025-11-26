#inference.py
import torch
import torchvision.transforms as T
from PIL import Image
import os
import traceback
from config import N_FRAMES, IMG_SIZE , DEVICE
from model import VideoModel
from utils import sample_frames_from_video, crop_face_or_center

# --- Transforms for Inference (without augmentation) ---
inference_transforms = T.Compose([
    T.Resize((IMG_SIZE, IMG_SIZE)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def load_model_from_path(path, device=DEVICE):
    """
    Returns: model loaded from the specified path.
    """
    print(f"Loading model from: {path}")
    
    model = VideoModel(pretrained=False)
    
    checkpoint = torch.load(path, map_location=device)
    
    
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
    model.eval() # Set the model to evaluation mode
    return model

def predict_video_with_model(model, video_path, device=DEVICE, n_frames=N_FRAMES, thresh=0.5):
    """
    Returns: (binary_pred (0/1), probability, error_message)
    """
    try:
        # 1. read frames from video
        frames = sample_frames_from_video(video_path, n_frames=n_frames)
        if len(frames) == 0:
            return None, 0.0, "Could not read frames from video (or video is empty)."

        # 2. crop faces and prepare images
        processed_frames = []
        for frame in frames:
            # crop face
            face_img = crop_face_or_center(frame, out_size=IMG_SIZE)
            # convert to PIL
            pil_img = Image.fromarray(face_img)
            # apply Transforms
            tensor_img = inference_transforms(pil_img)
            processed_frames.append(tensor_img)
        
        # If the number of frames is less than required, repeat the last frame (Padding)
        while len(processed_frames) < n_frames:
            processed_frames.append(processed_frames[-1])
            
        # Stack them into a single batch tensor
        # Shape: (1, Frames, Channels, Height, Width)
        input_tensor = torch.stack(processed_frames).unsqueeze(0).to(device)
        
        # 3. make prediction
        with torch.no_grad():
            logits = model(input_tensor)
            prob = torch.sigmoid(logits).item()
            
        pred = 1 if prob >= thresh else 0
        return pred, prob, None

    except Exception as e:
        traceback.print_exc()
        return None, 0.0, str(e)