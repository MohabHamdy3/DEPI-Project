# model.py
import torch
import torch.nn as nn
import torchvision.models as models

class FrameBackboneResNet(nn.Module):
    def __init__(self, feat_dim=512, pretrained=True):
        super().__init__()
        # weights='DEFAULT' is the modern way in torch, but pretrained=True works for legacy
        base = models.resnet50(pretrained=pretrained)
        in_feat = base.fc.in_features
        base.fc = nn.Identity()
        self.base = base
        self.proj = nn.Linear(in_feat, feat_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        f = self.base(x)
        return self.relu(self.proj(f))

class VideoModel(nn.Module):
    def __init__(self, feat_dim=512, lstm_hidden=256, bidir=True, pretrained=True):
        super().__init__()
        self.backbone = FrameBackboneResNet(feat_dim, pretrained)
        self.lstm = nn.LSTM(feat_dim, lstm_hidden, batch_first=True, bidirectional=bidir)
        out_dim = lstm_hidden * (2 if bidir else 1)

        self.classifier = nn.Sequential(
            nn.Linear(out_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, 1)
        )

    def forward(self, frames):
        # Shape: (Batch, Frames, Channels, Height, Width)
        B, T, C, H, W = frames.shape
        x = frames.view(B*T, C, H, W)
        
        feats = self.backbone(x)
        feats = feats.view(B, T, -1)
        
        out, _ = self.lstm(feats)
        return self.classifier(out[:, -1, :]).squeeze(1)