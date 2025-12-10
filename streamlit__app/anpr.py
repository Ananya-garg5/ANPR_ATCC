from ultralytics import YOLO
import tempfile
import cv2
import numpy as np

def run_anpr_on_image(uploaded_file, model_path):
    model = YOLO(model_path)

    # Read image
    img_bytes = uploaded_file.read()
    img_arr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    results = model(img)

    annotated = results[0].plot()
    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
    return annotated


def run_anpr_on_video(uploaded_file, model_path):
    model = YOLO(model_path)

    # Save uploaded video temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    # Run YOLO tracking/video inference
    output_path = tfile.name + "_anpr_output.mp4"
    model.predict(
        source=tfile.name,
        save=True,
        save_txt=False,
        project="runs/anpr_streamlit",
        name="output",
        conf=0.4
    )

    # YOLO saves video at:
    # runs/anpr_streamlit/output/*.mp4
    return "runs/anpr_streamlit/output/" + [f for f in os.listdir("runs/anpr_streamlit/output") if f.endswith(".mp4")][0]
