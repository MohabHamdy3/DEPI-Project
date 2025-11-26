import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Model Training Performance")

st.write("""
This dashboard visualizes the performance of the deepfake detection model  
across 20 training epochs:
- **Training vs Validation Loss**
- **Validation AUC**
- **Overall Training Summary**
""")

st.divider()

# -------------------------------------------------------
# CLEANED METRICS (from your real logs)
# -------------------------------------------------------

train_loss = np.array([
    0.6420, 0.5253, 0.4077, 0.3420, 0.2558,
    0.2349, 0.1855, 0.1538, 0.1225, 0.1312,
    0.1356, 0.1103, 0.1326, 0.0828, 0.0793,
    0.0787, 0.0720, 0.0845, 0.0751, 0.0436
])

val_loss = np.array([
    0.5754, 0.5238, 0.4670, 0.3872, 0.4906,
    0.9249, 0.6848, 0.2940, 0.3407, 0.3507,
    0.3688, 0.3450, 0.2818, 0.4579, 0.3222,
    0.2216, 0.2142, 0.8484, 0.2845, 0.2939
])

val_auc = np.array([
    0.7764, 0.8652, 0.9037, 0.9167, 0.9384,
    0.8678, 0.9099, 0.9538, 0.9435, 0.9572,
    0.9544, 0.9617, 0.9692, 0.9667, 0.9604,
    0.9865, 0.9749, 0.9354, 0.9661, 0.9718
])

epochs = np.arange(1, len(train_loss) + 1)

# -------------------------------------------------------
#  2 Side-by-Side Charts
# -------------------------------------------------------

col1, col2 = st.columns(2)

# ---------------------- LOSS CURVE ----------------------
with col1:
    st.subheader("Training vs Validation Loss")
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(epochs, train_loss, marker="o", label="Train Loss")
    ax.plot(epochs, val_loss, marker="o", label="Val Loss")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

# ---------------------- AUC CURVE ----------------------
with col2:
    st.subheader("Validation AUC")
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(epochs, val_auc, marker="o", color="green", label="Val AUC")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("AUC")
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

st.divider()

# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------

best_epoch_auc = val_auc.argmax() + 1
best_epoch_loss = val_loss.argmin() + 1

st.subheader("Training Summary")

st.write(f"""
- **Best Validation AUC:** `{val_auc.max():.4f}` at **Epoch {best_epoch_auc}**
- **Lowest Validation Loss:** `{val_loss.min():.4f}` at **Epoch {best_epoch_loss}**
- **Total Epochs:** `{len(train_loss)}`  
""")
