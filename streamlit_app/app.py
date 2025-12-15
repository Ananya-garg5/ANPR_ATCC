import streamlit as st
from modules.anpr import run_anpr_on_image
from modules.atcc import run_atcc_on_image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ANPR & ATCC Dashboard",
    layout="wide",
    page_icon="🚦"
)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 style='text-align:center;'>🚗 ANPR & ATCC Traffic Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Configuration")

task = st.sidebar.radio(
    "Select Task",
    [
        "Automatic Number Plate Recognition (ANPR)",
        "Automatic Traffic Count & Classification (ATCC)"
    ]
)

model_path = (
    "models/best_anpr.pt" if "ANPR" in task else "models/best_atcc.pt"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

run_btn = st.sidebar.button("🚀 Run Inference")

# ---------------- MAIN AREA ----------------
if run_btn:
    if uploaded_file is None:
        st.warning("⚠️ Please upload an image.")
    else:
        with st.spinner("Running model inference..."):
            try:
                # ---------- ANPR ----------
                if "ANPR" in task:
                    output = run_anpr_on_image(uploaded_file, model_path)
                    st.image(
                        output,
                        caption="ANPR Output (Detected Number Plate)",
                        use_container_width=True
                    )

                # ---------- ATCC ----------
                else:
                    output_img, counts = run_atcc_on_image(uploaded_file, model_path)
                    st.image(
                        output_img,
                        caption="ATCC Output (Vehicle Detection)",
                        use_container_width=True
                    )

                    st.subheader("📊 Vehicle Count")
                    st.table(counts)

                st.success("Inference completed successfully!")

            except Exception as e:
                st.error(f"Error during inference: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Developed using YOLOv8 & Streamlit</p>",
    unsafe_allow_html=True
)
