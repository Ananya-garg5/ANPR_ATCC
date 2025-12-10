🚦 AI Traffic Analytics (ATCC & ANPR)
A real-time traffic monitoring system that integrates Automatic Traffic Counting and Classification (ATCC) with Automatic Number Plate Recognition (ANPR). Built using YOLOv8 for vehicle detection and Streamlit for the interactive dashboard.

📝 Project Overview
This project aims to automate traffic analysis by processing video feeds to detect vehicles, classify them (Car, Truck, Bus, Motorcycle), and extract license plate numbers. It provides a visual dashboard for traffic authorities or urban planners to monitor road usage and congestion.

Key Features
Real-Time Vehicle Detection: Identifies and tracks vehicles in video streams.

Multi-Class Classification: Distinguishes between Cars, Trucks, Buses, and Motorcycles.

Traffic Counting (ATCC): Maintains a live count of vehicles passing through the frame.

License Plate Recognition (ANPR): Extracts and logs license plate text from detected vehicles.

Interactive Dashboard: A user-friendly web interface powered by Streamlit to upload videos and view analytics.

Data Visualization: Live metrics and visual bounding boxes.

📸 Demo
[Insert a screenshot of your Streamlit Dashboard here] [Insert a sample processed image with bounding boxes here]

🛠 Tech Stack
Language: Python 3.11+

Computer Vision: OpenCV, Ultralytics YOLOv8

Dashboard Framework: Streamlit

ANPR Engine: [Mention your ANPR lib here, e.g., EasyOCR / Tesseract / LPRNet]

Data Manipulation: NumPy, Pandas

📂 Project Structure
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
🚀 Installation & Setup
Follow these steps to run the dashboard locally.

1. Clone the Repository
Bash

git clone https://github.com/your-username/traffic-analytics.git
cd Traffic_Dashboard
2. Create a Virtual Environment (Optional but Recommended)
Bash

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Add Your Model
Place your trained YOLOv8 model file (best.pt) inside the models/ directory.

Note: The model was trained on the BDD100K dataset using Kaggle GPUs.

🖥 Usage
To start the dashboard, run the following command in your terminal:

Bash

streamlit run app.py
A browser tab will open (usually at http://localhost:8501).

Use the Sidebar to upload a traffic video file (.mp4, .avi).

Adjust the Confidence Threshold slider to filter weak detections.

Watch the live processing and statistics update in real-time.

📊 Dataset & Training
The ATCC model was trained using the BDD100K (Berkeley DeepDrive) dataset.

Training Images: ~7,000 images (Subset of 10k train set).

Validation Images: 10,000 images (Official Val set).

Classes: Car, Truck, Bus, Motorcycle.

Training Platform: Kaggle (Tesla T4 GPUs).

Epochs: 50 (with Early Stopping).

🔮 Future Improvements
[ ] Integration with live IP Camera feeds (RTSP).

[ ] Export analytics data to CSV/Excel.

[ ] Speed estimation logic.

[ ] Night-mode enhancement for ANPR.


📜 License
Distributed under the MIT License. See LICENSE for more information.