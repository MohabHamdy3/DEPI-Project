import streamlit as st

st.title("About the Project")

st.write("""
The **Deepfake Detection System** is an advanced tool designed to identify 
manipulated videos created using deep learning methods.

### Purpose
- Protect privacy  
- Improve security  
- Fight misinformation  
- Verify media authenticity  

### How it works
- Extracts frames  
- Processes using a model  
- Identifies manipulation artifacts  
- Predicts real vs fake  

### Datasets
- FaceForensics++ C23 
""")
# لازم تعمل import للملف (لو نقلته بره pages)
from footer_component import show_footer

# ولو استخدمت الحل التاني (حطيت underscore) يبقى:
# from pages._footer_component import show_footer

# وفي آخر السطر خالص استدعي الدالة:
show_footer()
