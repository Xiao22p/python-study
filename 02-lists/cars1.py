# 使用sorted()函数对列表进行临时排列
cars = ['bmw','audi','toyota','subara']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the sorted list again:")
print(sorted(cars,reverse=True)) # 向sorted()函数转递reverse=True按字母顺序临时排列