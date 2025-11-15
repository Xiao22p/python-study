from formatted_name1 import get_formatted_name


def get_valid_input():
    """循环提示输入姓名，直到输入quit，每次有效输入时调用格式化函数并打印问候"""
    while True:
        print("\n请告诉我你的姓名（输入'quit'退出）：")

        f_name = input('你的名是：')
        if f_name == 'quit':
            break

        l_name = input('你的姓是：')
        if l_name == 'quit':
            break


        name = get_formatted_name(f_name, l_name)
        print(f"你好，{name}！")


get_valid_input()