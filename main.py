from src.download import download_dataset
from src.process import process_data
from src.visualize import create_visualizations

def main():
    print(" HỆ THỐNG PHÂN TÍCH DỮ LIỆU SUPERSTORE ")
    download_dataset()
    df_clean = process_data()
    create_visualizations(df_clean)
    print("Mở thư mục 'reports/figures' để xem kết quả.")


if __name__ == "__main__":
    main()
