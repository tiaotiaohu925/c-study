from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 中文字体：避免标题/标签显示成方框
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

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
monthly_revenue = df.groupby("InvoiceMonth")["Revenue"].sum()
monthly_revenue.plot(kind="bar")
plt.title("月度收入趋势")
plt.xlabel("InvoiceMonth")
plt.ylabel("Revenue (GBP)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150)
plt.close()

# TODO 2：收入最高的 10 个国家
# 提示：按 Country 分组求和，排序后取前 10
# 口径：包含英国（英国收入约 902 万，远高于其余国家，市场高度集中）
top_countries = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)
top_countries.sort_values().plot(kind="barh")
plt.title("收入最高的 10 个国家（含英国）")
plt.xlabel("Revenue (GBP)")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_countries.png", dpi=150)
plt.close()


# TODO 3：收入最高的 10 个商品
# 提示：按 Description 分组求和，排序后取前 10
# 口径：排除运费/人工等非商品项，避免污染商品排名
non_product = ["DOTCOM POSTAGE", "POSTAGE", "Manual"]
top_products = (
    df[~df["Description"].isin(non_product)]
    .groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
top_products.sort_values().plot(kind="barh")
plt.title("收入最高的 10 个商品（已排除运费/人工项）")
plt.xlabel("Revenue (GBP)")
plt.ylabel("Description")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_products.png", dpi=150)
plt.close()



# TODO 4：按小时的收入分布
# 提示：按 Hour 分组，对 Revenue 求和
hourly_revenue = df.groupby("Hour")["Revenue"].sum()
hourly_revenue.plot(kind="bar")
plt.title("按小时的收入分布")
plt.xlabel("Hour")
plt.ylabel("Revenue (GBP)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "hourly_revenue.png", dpi=150)
plt.close()



# TODO 5：订单金额分布直方图
# 提示：先按 InvoiceNo 汇总每单 Revenue，再画 hist
# 口径：剔除最高 1% 的订单，避免极端大单让分布不可读
# 注意：不要用 clip(upper=...) —— 那会把所有高于 99% 分位的订单堆到同一个柱子里，
# 形成最右侧的假尖峰。这里直接剔除，才是真实分布。
order_revenue = df.groupby("InvoiceNo")["Revenue"].sum()
order_revenue_clean = order_revenue[order_revenue <= order_revenue.quantile(0.99)]
order_revenue_clean.hist(bins=50)
plt.title("订单金额分布（剔除最高 1%）")
plt.xlabel("Order Revenue (GBP)")
plt.ylabel("Order Count")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "order_revenue.png", dpi=150)
plt.close()



# TODO 6：把 3 条业务发现写到下面，或保存到 reports 文件
# 1. 月度收入：最高是 2011-11（约 1,509,496），其次 2011-10（约 1,154,979）、
#    2011-09（约 1,058,590），Q4 明显季节性上升，2011-12 回落，并非指数增长。
# 2. 国家收入：英国一家独大（约 9,025,222），市场高度集中；荷兰、爱尔兰、德国、
#    法国等其余国家收入远低于英国，意大利不在前 10。
# 3. 商品收入：排除运费/人工等非商品项（DOTCOM POSTAGE / Manual / POSTAGE）后，
#    排名靠前的是家居装饰类商品（如 REGENCY CAKESTAND 3 TIER），并非电子产品。

print("开始完成 5 张图。")
