favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):  # 通过set()（集合）可以剔除重复的元素
    print(language.title())