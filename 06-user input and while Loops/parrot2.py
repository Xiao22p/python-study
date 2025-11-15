prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = '' # 提供让Python首次执行while循环所需的比较
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



