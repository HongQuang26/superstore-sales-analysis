import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def save_figure(fig, file_name):
    path = os.path.join('reports/figures', file_name)
    fig.savefig(path, bbox_inches='tight', dpi=300)
    print(f"Đã lưu biểu đồ: {path}")


def create_visualizations(df):
    print(">>> [3/3] ĐANG VẼ VÀ LƯU BIỂU ĐỒ...")

    if not os.path.exists('reports/figures'):
        os.makedirs('reports/figures')

    trend_data = df.groupby('month_year')['sales'].sum()

    plt.figure()
    plt.plot(trend_data.index, trend_data.values, marker='o', color='#2c3e50', linewidth=2)
    plt.title('Biến Động Doanh Số Theo Tháng', fontsize=14, fontweight='bold')
    plt.xticks(rotation=90, fontsize=8)
    plt.ylabel('Doanh Số (USD)')
    plt.tight_layout()
    save_figure(plt, 'sales_trend.png')
    plt.close()


    cat_profit = df.groupby('category')['profit'].sum().sort_values(ascending=False).reset_index()
    plt.figure()
    sns.barplot(data=cat_profit, x='category', y='profit', hue='category', legend=False, palette='viridis')
    plt.title('Tổng Lợi Nhuận Theo Ngành Hàng', fontsize=14, fontweight='bold')
    plt.ylabel('Lợi Nhuận (USD)')
    save_figure(plt, 'category_profit.png')
    plt.close()


    plt.figure()
    sns.scatterplot(data=df, x='discount', y='profit', alpha=0.5, color='#e74c3c')
    plt.title('Tương Quan: Mức Giảm Giá vs. Lợi Nhuận', fontsize=14, fontweight='bold')
    save_figure(plt, 'discount_vs_profit.png')
    plt.close()

    print("Hoàn tất toàn bộ quy trình!")