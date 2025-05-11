import pandas as pd
import yaml
import os

def convert_to_yaml(csv_path, yaml_path):
    if not os.path.exists(csv_path):
        print(f"❌ File tidak ditemukan: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')  # normalisasi kolom
    last = df.iloc[-1]

    # Ambil hanya metrik utama
    result_data = {
        "metrics/precision": float(last.get("metrics/precision", 0)),
        "metrics/recall": float(last.get("metrics/recall", 0)),
        "metrics/mAP_0.5": float(last.get("metrics/mAP_0.5", 0)),
        "metrics/mAP_0.5:0.95": float(last.get("metrics/mAP_0.5:0.95", 0))
    }

    with open(yaml_path, "w") as f:
        yaml.dump(result_data, f)

    print(f"✅ Hasil disimpan ke: {yaml_path}")

# Konversi untuk kedua model
convert_to_yaml("runs/train/fruits_per_object/results.csv", "runs/train/fruits_per_object/results.yaml")
convert_to_yaml("runs/train/fruits_per_group/results.csv", "runs/train/fruits_per_group/results.yaml")
