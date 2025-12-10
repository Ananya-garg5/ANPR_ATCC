from ultralytics import YOLO
import tempfile
import cv2
import numpy as np
import os

def run_atcc_on_image(uploaded_file, model_path):
    model = YOLO(model_path)

    img_bytes = uploaded_file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    results = model(img)
    annotated = results[0].plot()
    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    return annotated


def run_atcc_on_video(uploaded_file, model_path):
    model = YOLO(model_path)

    # Save temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    model.predict(
        source=tfile.name,
        save=True,
        save_txt=False,
        project="runs/atcc_streamlit",
        name="output",
        conf=0.4
    )

    return "runs/atcc_streamlit/output/" + [f for f in os.listdir("runs/atcc_streamlit/output") if f.endswith(".mp4")][0]
