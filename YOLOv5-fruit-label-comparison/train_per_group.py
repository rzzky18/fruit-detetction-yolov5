import os
import subprocess

# Path ke YOLOv5 dan direktori proyek
yolov5_path = "yolov5"
project_path = "runs/train"  # direktori output hasil training (di luar yolov5)

# Training per grup
subprocess.run([
    "python", os.path.join(yolov5_path, "train.py"),
    "--img", "640",                        # resolusi gambar 
    "--batch", "16",                        # batch 
    "--epochs", "50",                      
    "--data", "train_per_group.yaml",     # file konfigurasi dataset
    "--weights", "yolov5s.pt",            # model awal
    "--name", "fruits_per_group",         # nama folder hasil
    "--project", project_path             # simpan hasil ke luar folder yolov5
])

