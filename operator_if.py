favorite_languages = {
    'jen' : 'python',
    'sarah' : 'C',
    'edward' : 'ruby',
    'phil' : 'python',
    }
print("The folowwing languages have been mentioned: ")
for language in set(sorted(favorite_languages.values())):
    print(language.title())
