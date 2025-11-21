# Import các module tự viết
from src.download import download_dataset
from src.process import process_data
from src.visualize import create_visualizations


def main():
    print("=== HỆ THỐNG PHÂN TÍCH DỮ LIỆU SUPERSTORE ===")

    # Bước 1: Tải dữ liệu
    download_dataset()

    # Bước 2: Làm sạch dữ liệu
    df_clean = process_data()

    # Bước 3: Vẽ báo cáo
    create_visualizations(df_clean)

    print("\n=== CHƯƠNG TRÌNH KẾT THÚC THÀNH CÔNG ===")
    print("Vui lòng mở thư mục 'reports/figures' để xem kết quả.")


if __name__ == "__main__":
    main()