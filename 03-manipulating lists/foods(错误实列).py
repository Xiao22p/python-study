my_foods = ['pizza','falafel','carrot cake']

# 这是行不通的：
friend_foods = my_foods # 直接关联friend_foods,并没有创建my_foods的副本，所以其实是同一个列表

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favourite foods ars:')
print(my_foods)

print("\nMy friend's favourite are:")
print(friend_foods)

