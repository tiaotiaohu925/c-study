# 第 2 天：Python 基础练习
# 完成后运行：
# python D:\Codex\study\practice\week01\day02\python_practice.py

# 练习 1：创建三个变量
# name 保存你的名字，city 保存上海，hours 保存今天学习的小时数
# TODO: 在这里写代码
name = "郭昊"
city = "上海"
hours = 1.5

print("练习 1：", name, city, hours)


# 练习 2：创建列表
# amounts = [120, 80, 200, 150, 90, 300]
# TODO: 创建 amounts 列表
amounts = [120, 80, 200, 150, 90, 300]

print("练习 2：", amounts)


# 练习 3：循环打印大于 100 的金额
# TODO: 遍历 amounts，打印大于 100 的数字
print("练习 3：")
# 在这里写循环 
for amount in amounts:
    if amount > 100:
        print(amount)



# 练习 4：写一个函数 total(numbers)，返回 numbers 的总和
# TODO: 定义函数并打印 amounts 的总和
print("练习 4：")
# 在这里写函数 
def total(numbers):

    return sum(numbers)

print(total(amounts))


# 练习 5：使用 pandas 筛选 paid 订单并求和
# orders 数据如下，status 为 paid 的 amount 是 [120, 80, 150, 90, 300]
# TODO: 创建 DataFrame，筛选 paid，打印 paid 订单和总金额
print("练习 5：")
# 在这里写 pandas 代码
import pandas as pd
orders = pd.DataFrame({"status": ["paid", "paid", "refunded", "paid", "paid", "paid"],
                      "amount": [120, 80, 200, 150, 90, 300]})
paid_orders = orders[orders["status"] == "paid"]
print(paid_orders)
print(paid_orders["amount"].sum())
