# 🚗 ATCC + ANPR Streamlit Dashboard  
A unified dashboard for *Automatic Traffic Counting & Classification (ATCC)* and *Automatic Number Plate Recognition (ANPR)* built using *YOLOv8* and *Streamlit*.

This project provides:
- Vehicle detection & classification  
- Number plate detection  
- Image + video inference support  
- A simple and clean Streamlit UI  
- Easy model integration using .pt YOLO weights  

---

## ⭐ Features  
### 🔵 ATCC (Automatic Traffic Counting & Classification)
- Detects vehicles (car, truck, bus, bike…)
- Counts total vehicles
- Works on *images* and *videos*
- YOLOv8 backend for fast and accurate detection

### 🟢 ANPR (Automatic Number Plate Recognition)
- Detects license plates
- Extracts plates using YOLO
- Works on images and videos
- Ready for OCR integration

### 🟣 Streamlit Dashboard
- User-friendly UI  
- Upload media directly  
- Choose model paths  
- Real-time output visualization  

---

## 📁 Project Structure

streamlit_app/
│── app/
│ ├── anpr.py # ANPR model wrapper
│ ├── atcc.py # ATCC model wrapper
│ ├── utils.py # Helper functions
│ └── streamlit_app.py # Main Streamlit app
│
├── models/
│ ├── anpr_model.pt # Trained ANPR model
│ └── atcc_model.pt # Trained ATCC model
│
├── requirements.txt
└── README.md