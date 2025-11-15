# 使用pop()方法打印一条消息
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"The last motorcycles I owned was a {first_owned.title()}") # 也可以使用pop()方法删除（弹出）列表中任意位置的元素
print(f"The last motorcycles I owned was a {last_owned.title()}")
