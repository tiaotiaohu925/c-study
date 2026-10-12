import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer": ["张三", "李四", "王五", "赵六", "孙七", "周八"],
    "city": ["上海", "北京", "上海", "上海", "深圳", "北京"],
    "amount": [120, 80, 200, 150, 90, 300],
    "status": ["paid", "paid", "refunded", "paid", "paid", "paid"],
})

paid_orders = orders[orders["status"] == "paid"]
paid_total = paid_orders["amount"].sum()
city_total = orders.groupby("city")["amount"].sum()

print("全部订单：")
print(orders.to_string(index=False))
print()
print("paid 订单：")
print(paid_orders.to_string(index=False))
print()
print("paid 总金额：", paid_total)
print()
print("各城市订单金额：")
print(city_total)
