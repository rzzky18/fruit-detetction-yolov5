import sys
import os
import argparse

# Tambahkan path ke folder YOLOv5 agar bisa import modul detect asli
FILE = os.path.abspath(__file__)
ROOT = os.path.dirname(FILE)
YOLOV5_PATH = os.path.join(ROOT, 'yolov5')
sys.path.append(YOLOV5_PATH)

from detect import run as yolo_detect  # Sekarang ini mengarah ke yolov5/detect.py

def detect(weights_path, source_path, project_name="runs/detect", exp_name="exp"):
    yolo_detect(
        weights=weights_path,
        source=source_path,
        imgsz=(416, 416),
        conf_thres=0.25,
        iou_thres=0.45,
        max_det=1000,
        device='cpu',
        project=project_name,
        name=exp_name,
        save_txt=False,
        save_conf=True,
        save_crop=False,
        exist_ok=True
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, required=True, help='Path ke model .pt')
    parser.add_argument('--source', type=str, required=True, help='Path gambar/video/folder')
    args = parser.parse_args()

    detect(args.weights, args.source)
