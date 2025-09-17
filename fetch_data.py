import os
from kaggle.api.kaggle_api_extended import KaggleApi

# ✅ Download folder (Change only once if needed)
download_dir = r"D:\powerbi"
os.makedirs(download_dir, exist_ok=True)

# ✅ Authenticate using kaggle.json
api = KaggleApi()
api.authenticate()

# ✅ Ask user for dataset slug (like "heptapod/titanic")
dataset = input("Enter Kaggle dataset (e.g., 'heptapod/titanic'): ").strip()

# ✅ Check dataset metadata before downloading
try:
    dataset_info = api.dataset_view(dataset)
    print(f"\n📦 Dataset Found: {dataset_info.title}")
    print(f"👤 Owner: {dataset_info.ownerUser.name}")
    print(f"🔒 Private: {dataset_info.isPrivate}")

    if dataset_info.isPrivate:
        print("\n⚠️ This dataset is PRIVATE.")
        print("👉 You need to request access or be added as a collaborator on Kaggle.")
        exit(1)

except Exception as e:
    print("\n❌ Could not access dataset metadata.")
    print("👉 Possible reasons:")
    print("   - The dataset is private and you are not a collaborator.")
    print("   - You have not accepted the dataset’s terms of use on Kaggle.")
    print("   - The dataset slug is incorrect.")
    print(f"🔎 Error: {e}")
    exit(1)

# ✅ Proceed with download
print(f"\n⬇️ Downloading dataset '{dataset}' into {download_dir} ...")
api.dataset_download_files(dataset, path=download_dir, unzip=True)
print(f"✅ Dataset '{dataset}' downloaded successfully to {download_dir}")
