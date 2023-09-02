from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for language in set(sorted(favorite_languages.values())):
    print(language.title())
