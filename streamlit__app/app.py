import streamlit as st
from app.anpr import run_anpr_on_image, run_anpr_on_video
from app.atcc import run_atcc_on_image, run_atcc_on_video

st.set_page_config(page_title="ATCC + ANPR Dashboard", layout="wide")

st.title("🚗 ATCC + ANPR Streamlit Dashboard")

st.sidebar.header("🔧 Settings")
task_type = st.sidebar.selectbox("Task", ["ATCC", "ANPR"])
input_type = st.sidebar.selectbox("Input Type", ["Image", "Video"])

model_path = st.sidebar.text_input("Model Path", "models/anpr_model.pt" if task_type=="ANPR" else "models/atcc_model.pt")

uploaded_file = st.sidebar.file_uploader("Upload Image/Video")

run_button = st.sidebar.button("Run Detection")

if run_button:
    if uploaded_file is None:
        st.error("Please upload a file first.")
    else:
        if task_type == "ANPR":
            if input_type == "Image":
                out_img = run_anpr_on_image(uploaded_file, model_path)
                st.image(out_img, caption="ANPR Output")
            else:
                out_vid_path = run_anpr_on_video(uploaded_file, model_path)
                st.video(out_vid_path)

        elif task_type == "ATCC":
            if input_type == "Image":
                out_img = run_atcc_on_image(uploaded_file, model_path)
                st.image(out_img, caption="ATCC Output")
            else:
                out_vid_path = run_atcc_on_video(uploaded_file, model_path)
                st.video(out_vid_path)
