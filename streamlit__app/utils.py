import os
import cv2
import numpy as np

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary path."""
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())
    return temp_path
