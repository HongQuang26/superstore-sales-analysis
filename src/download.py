import os
from kaggle.api.kaggle_api_extended import KaggleApi


def download_dataset():
    print(">>> [1/3] BẮT ĐẦU TẢI DỮ LIỆU TỪ KAGGLE...")
    download_path = 'data/raw'
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    dataset_name = 'vivek468/superstore-dataset-final'

    try:
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(dataset_name, path=download_path, unzip=True)
        print(f"Đã tải và giải nén dữ liệu thành công tại: {download_path}")
        files = os.listdir(download_path)
        print(f"Các file hiện có: {files}")

    except Exception as e:
        print(f"LỖI khi tải dữ liệu: {e}")
        print("Hãy chắc chắn bạn đã cấu hình file kaggle.json trong thư mục ~/.kaggle/")
        exit()