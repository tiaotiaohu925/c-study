# 第 2 周第 3 天：Excel 函数练习

## 数据文件

`data/processed/online_retail_sample_10k_restored.csv`

字段：

| 列 | 字段 | 含义 |
|---|---|---|
| A | InvoiceNo | 订单号 |
| B | StockCode | 商品编码 |
| C | Description | 商品描述 |
| D | Quantity | 数量 |
| E | InvoiceDate | 订单时间 |
| F | UnitPrice | 单价 |
| G | CustomerID | 客户编号 |
| H | Country | 国家 |
| I | Revenue | 收入，Quantity × UnitPrice |

数据预览：

| InvoiceNo | StockCode | Description | Quantity | UnitPrice | Country | Revenue |
|---|---|---|---:|---:|---|---:|
| 536365 | 84406B | CREAM CUPID HEARTS COAT HANGER | 8 | 2.75 | United Kingdom | 22.00 |
| 536370 | 10002 | INFLATABLE POLITICAL GLOBE | 48 | 0.85 | France | 40.80 |
| 536373 | 37370 | RETRO COFFEE MUGS ASSORTED | 6 | 1.06 | United Kingdom | 6.36 |
| 536378 | 85071B | RED CHARLIE+LOLA PERSONAL DOORSIGN | 96 | 0.38 | United Kingdom | 36.48 |
| 536381 | 22083 | PAPER CHAIN KIT RETROSPOT | 1 | 2.95 | United Kingdom | 2.95 |

## 一、SUMIFS：多条件求和

语法：

```excel
=SUMIFS(求和范围, 条件范围1, 条件1, 条件范围2, 条件2, ...)
```

示例，使用另一组演示数据：

```excel
=SUMIFS(D2:D100, B2:B100, "East", C2:C100, ">10")
```

这表示：在 B 列等于 `East` 且 C 列大于 10 时，对 D 列求和。

注意事项：

- 求和范围和每个条件范围必须大小一致。
- 文本条件要加双引号。
- 数字比较条件写成 `">10"`。
- 条件可以来自单元格，例如 `H2`。

## 二、COUNTIFS：多条件计数

语法：

```excel
=COUNTIFS(条件范围1, 条件1, 条件范围2, 条件2, ...)
```

示例：

```excel
=COUNTIFS(B2:B100, "East", C2:C100, ">10")
```

这表示：统计 B 列为 `East` 且 C 列大于 10 的行数。

## 三、XLOOKUP：查找并返回列

语法：

```excel
=XLOOKUP(查找值, 查找数组, 返回数组, [如果未找到])
```

示例：

```excel
=XLOOKUP("A001", A2:A100, C2:C100, "Not found")
```

注意事项：

- 默认是精确匹配。
- 查找数组和返回数组必须大小一致。
- 如果查找值重复，默认返回第一个匹配项。
- 用于业务表时，先确认查找键是否唯一。

## 四、练习

使用 `online_retail_sample_10k_restored.csv`，写出公式并计算结果：

1. 用 `SUMIFS` 计算 `Country = United Kingdom` 且 `Quantity > 10` 的 `Revenue` 总和。
2. 用 `SUMIFS` 计算 `Country = France` 且 `UnitPrice > 1` 的 `Revenue` 总和。
3. 用 `COUNTIFS` 统计 `Country = United Kingdom` 且 `Quantity > 10` 的记录数。
4. 用 `COUNTIFS` 统计 `Country = United Kingdom` 且 `Description` 包含 `BAG` 的记录数。
5. 用 `XLOOKUP` 查找 `StockCode = 84406B` 对应的 `Description`；再用 `COUNTIF` 检查 `84406B` 是否重复。

## 五、提交要求

每题提交：

- 公式原文。
- 计算结果。
- 第 5 题说明该商品编码是否唯一。

先自己写公式，不要直接筛选数据后手填数字。
