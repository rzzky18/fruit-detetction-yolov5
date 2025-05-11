import yaml

def load_results(path):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    return data["metrics/mAP_0.5"]

mAP_obj = load_results("runs/train/fruits_per_object/results.yaml")
mAP_grp = load_results("runs/train/fruits_per_group/results.yaml")

print(f"mAP Per Objek: {mAP_obj:.3f}")
print(f"mAP Per Grup : {mAP_grp:.3f}")

if mAP_obj > mAP_grp:
    print("Model dengan labeling per objek lebih akurat.")
else:
    print("Model dengan labeling per grup lebih akurat.")
