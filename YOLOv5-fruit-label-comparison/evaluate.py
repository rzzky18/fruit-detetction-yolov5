import pandas as pd
import os

# Path ke file hasil training
path_obj = "runs/train/fruits_per_object/results.csv"
path_grp = "runs/train/fruits_per_group/results.csv"

def show_metrics(path, label):
    print(f"\n📊 Hasil Akhir - {label}")
    if not os.path.exists(path):
        print(f"❌ File tidak ditemukan: {path}")
        return

    df = pd.read_csv(path)

    # Normalisasi nama kolom
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')  # hilangkan spasi & karakter BOM

    # Cek isi kolom sebenarnya
    print("🧾 Kolom ditemukan:", df.columns.tolist())

    # Ambil baris terakhir
    last = df.iloc[-1]

    # Cari kolom epoch (jika ada)
    epoch_col = [col for col in df.columns if 'epoch' in col.lower()]
    if epoch_col:
        print(f"Epoch     : {int(last[epoch_col[0]])}")
    else:
        print("Epoch     : (kolom epoch tidak tersedia)")

    # Tampilkan metrik jika tersedia
    for metric in ['metrics/precision', 'metrics/recall', 'metrics/mAP_0.5', 'metrics/mAP_0.5:0.95']:
        if metric in df.columns:
            print(f"{metric:<17}: {last[metric]:.3f}")
        else:
            print(f"{metric:<17}: (tidak tersedia)")

# Jalankan evaluasi
show_metrics(path_obj, "Per Objek")
show_metrics(path_grp, "Per Grup")
