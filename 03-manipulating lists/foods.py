# 复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] # 提取一个切片，创建列表副本，将该副本赋给变量friend_foods

print('My favourite foods are:')
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)