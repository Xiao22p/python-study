prompt = "If you share you name, we can personalize the message you see."
prompt += "\nWhat is your first name?" # 运算符+=可以给变量prompt的字符串末尾追加一个新字符串（+=：创建多行字符串的方式）

name = input(prompt)
print(f"\nHello,{name}!")
