from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parents[3]
DATA_PATH = BASE_DIR / "data" / "raw" / "tips.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# 先观察数据
print("shape:", df.shape)
print("columns:", list(df.columns))
print("missing:", df.isna().sum().to_dict())
print(df.head())

# 提示：小费率 = tip / total_bill
# df["tip_rate"] = df["tip"] / df["total_bill"]

# TODO 1：每天总账单金额柱状图


# TODO 2：每天平均小费率柱状图


# TODO 3：午餐和晚餐账单总额对比


# TODO 4：total_bill 与 tip 的散点图


# TODO 5：total_bill 分布直方图


# TODO 6：把 3 条业务发现写到下面，或者写到 reports 文件里

print("开始完成 5 张图。")
