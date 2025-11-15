favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")