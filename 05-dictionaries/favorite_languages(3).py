favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# 按特定顺序遍历字典的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")