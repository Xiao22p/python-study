age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')

age_1 = 18

if age_1 < 4:
    price = 0
elif age_1 < 18:
    price = 25
else:
    price = 40

print(f"\nYour admission cost is ${price}.")