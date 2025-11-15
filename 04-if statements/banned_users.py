banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:  # not in关键字：检查特定的值不在列表中
    print(f"{user.title()},you can post a response if you wish.")