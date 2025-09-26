import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体大小（适合学术图表）
plt.rcParams.update({
    'font.size': 14,          # 全局字体大小
    'axes.titlesize': 16,     # 标题大小
    'axes.labelsize': 15,     # 坐标轴标签大小
    'xtick.labelsize': 12,    # X轴刻度标签大小
    'ytick.labelsize': 12,    # Y轴刻度标签大小
    'legend.fontsize': 12,    # 图例字体大小
})

# 读取 Excel 文件
file_path = 'GNN1.xlsx'  # 替换为你的文件路径
data1 = pd.read_excel(file_path, 3)
data2 = pd.read_excel(file_path, 4)
data3 = pd.read_excel(file_path, 5)
data4 = pd.read_excel(file_path, 6)

# 提取数据
x = data1.iloc[:, 0]  # 第一列
y1 = data1.iloc[:, 1]  # 第二列
y2 = data2.iloc[:, 1]
y3 = data3.iloc[:, 1]
y4 = data4.iloc[:, 1]

# 创建图表
plt.figure(figsize=(10, 6))  # 调整图表大小

# 使用适合色盲的调色板（如 "viridis" 或 "colorblind"）
colors = plt.cm.viridis([0.2, 0.4, 0.6, 0.8])  # 4种颜色

# 绘制曲线（调整标记大小和线条样式）
plt.plot(x, y1, marker='o', markersize=8, linestyle='-', linewidth=2, color=colors[0], label='domain10')
plt.plot(x, y2, marker='s', markersize=8, linestyle='--', linewidth=2, color=colors[1], label='domain15')
plt.plot(x, y3, marker='^', markersize=8, linestyle='-.', linewidth=2, color=colors[2], label='domain20')
plt.plot(x, y4, marker='x', markersize=8, linestyle=':', linewidth=2, color=colors[3], label='bayes')

# 设置坐标轴标签和标题
plt.xlabel('TV Distance', fontweight='bold')
plt.ylabel('Accuracy', fontweight='bold')
# plt.title('TV Distance vs Accuracy', fontweight='bold', pad=20)  # pad 增加标题与图表的间距

# 添加图例（调整位置和样式）
plt.legend(loc='best', framealpha=1, shadow=True)

# 调整坐标轴范围（可选）
plt.xlim(left=min(x), right=max(x))  # 自动计算X轴范围


# 添加网格线（虚线样式）
plt.grid(True, linestyle='--', alpha=0.5)

# 自动调整布局
plt.tight_layout()

# 保存高清图片（适合论文）
plt.savefig('TV_distance_accuracy_colorblind.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()