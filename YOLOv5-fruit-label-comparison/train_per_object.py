import os
import subprocess

# Path ke YOLOv5
yolov5_path = "yolov5"  # pastikan sudah clone repo ultralytics/yolov5

# Training per objek
subprocess.run([
    "python", os.path.join(yolov5_path, "train.py"),
    "--img", "640",
    "--batch", "16",
    "--epochs", "50",
    "--data", "train_per_object.yaml",
    "--weights", "yolov5s.pt",
    "--name", "fruits_per_object"
])
