from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_PATH = BASE_DIR / "data" / "processed" / "online_retail.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("原始数据 shape:", df.shape)
print("缺失值:", df.isna().sum().to_dict())

# 基础清洗：只保留正向销售记录
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
df["Hour"] = df["InvoiceDate"].dt.hour
df["Weekday"] = df["InvoiceDate"].dt.day_name()

print("清洗后 shape:", df.shape)
print("日期范围:", df["InvoiceDate"].min(), "至", df["InvoiceDate"].max())

# 通用示例，不是任何一题的答案：
# grouped = df.groupby("某个分类列")["Revenue"].sum()
# grouped.plot(kind="bar")
# plt.title("标题")
# plt.xlabel("x 轴")
# plt.ylabel("y 轴")
# plt.tight_layout()
# plt.savefig(OUTPUT_DIR / "example.png", dpi=150)
# plt.close()

# TODO 1：月度收入趋势图
# 提示：按 InvoiceMonth 分组，对 Revenue 求和


# TODO 2：收入最高的 10 个国家
# 提示：按 Country 分组求和，排序后取前 10


# TODO 3：收入最高的 10 个商品
# 提示：按 Description 分组求和，排序后取前 10


# TODO 4：按小时的收入分布
# 提示：按 Hour 分组，对 Revenue 求和


# TODO 5：订单金额分布直方图
# 提示：先按 InvoiceNo 汇总每单 Revenue，再画 hist


# TODO 6：把 3 条业务发现写到下面，或保存到 reports 文件

print("开始完成 5 张图。")
