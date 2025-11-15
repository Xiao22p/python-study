prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True # 标志（flag)：在多种情况导致程序退出时，就可以使用标志
while active:
    message = input(prompt)

    if message =='quit':
        active = False
    else:
        print(message)


