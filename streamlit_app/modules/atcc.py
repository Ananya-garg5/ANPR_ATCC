from ultralytics import YOLO
import cv2
import numpy as np
import os

def run_atcc_on_image(uploaded_file, model_path):
    model = YOLO(model_path)

    # Decode image from buffer
    img_bytes = uploaded_file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    # Inference
    results = model(img, conf=0.4, verbose=False)[0]
    annotated = cv2.cvtColor(results.plot(), cv2.COLOR_BGR2RGB)

    # Counting
    counts = {}
    if results.boxes:
        class_ids = results.boxes.cls.cpu().numpy().astype(int)
        for cls_id in class_ids:
            class_name = results.names[cls_id]
            counts[class_name] = counts.get(class_name, 0) + 1

    return annotated, counts
