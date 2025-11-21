import pandas as pd
import os
def process_data():

    print(">>> [2/3] ĐANG XỬ LÝ VÀ LÀM SẠCH DỮ LIỆU...")
    raw_path = 'data/raw'
    try:
        files = [f for f in os.listdir(raw_path) if f.endswith('.csv')]
        if not files:
            raise FileNotFoundError("Không tìm thấy file .csv!")

        file_path = os.path.join(raw_path, files[0])
        try:
            df = pd.read_csv(file_path, encoding='windows-1252')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='utf-8')

        df = df.drop_duplicates()

        df.columns = [col.strip().lower().replace('-', '_').replace(' ', '_') for col in df.columns]

        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

        df['month_year'] = df['order_date'].dt.to_period('M').astype(str)

        print(f"Xử lý xong. Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột.")
        return df

    except Exception as e:
        print(f"LỖI khi xử lý dữ liệu: {e}")
        exit()