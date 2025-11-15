users = {
    'phh': {
        'first': 'peng',
        'last': 'haohui',
        'age': 21,
    },
    'pjy': {
        'first': 'peng',
        'last': 'jieying',
        'age': 17
    },
}

for username,user_info in users.items():
    print(f"\nUsername: {username}")  # 这一步是显示出用户名：phhh和pjy
    full_name = f"{user_info['first']} {user_info['last']}"
    age = f"{user_info['age']}"

    print(f"\tFullname: {full_name.title()}")
    print(f"\tAge: {age}")
