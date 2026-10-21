# 2026-10-21 Excel 函数与 SQL 维护记录

## 基本信息

- 实际学习时间：40 分钟
- Excel 工作簿：`practice/week02/day03/online_retail_sample_10k_restored.xlsx`
- 数据文件：`data/processed/online_retail_sample_10k_restored.csv`

## Excel 函数练习结果

| 题号 | 结果 |
|---|---|
| 1 | United Kingdom 且 Quantity > 10 的 Revenue：88,211.13 |
| 2 | France 且 UnitPrice > 1 的 Revenue：3,213.87 |
| 3 | United Kingdom 且 Quantity > 10 的记录数：2,077 |
| 4 | United Kingdom 且 Description 包含 BAG 的记录数：858 |
| 5 | StockCode 84406B 对应描述：CREAM CUPID HEARTS COAT HANGER；重复 9 次 |

## SQL 维护结果

- 第 1 题：日期区间查询正确，返回 4 行。
- 第 2 题：按 status 分组平均金额正确。
- 第 3 题：LEFT JOIN + COUNT(B.order_id) 正确，杭州订单数为 0。
- 第 4 题：按客户汇总 paid 金额，前 2 名为周八 300、张三 170。
- 第 5 题：订单总额大于 300 的城市为上海、北京。

## 仍然需要注意

- `LEFTJOIN` 必须写成 `LEFT JOIN`。
- 聚合题先确定分组粒度，再写 SELECT。
- 字符串条件使用单引号更稳妥。
