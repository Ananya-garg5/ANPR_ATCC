from ultralytics import YOLO
import cv2
import numpy as np
import os

def run_anpr_on_image(uploaded_file, model_path):
    model = YOLO(model_path)

    img_bytes = uploaded_file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    results = model(img, conf=0.4, verbose=False)[0]
    annotated = results.plot()
    
    # Convert back to RGB for Streamlit/Matplotlib
    return cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

