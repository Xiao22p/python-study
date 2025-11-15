def greet_users(names): # 传递列表
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
        