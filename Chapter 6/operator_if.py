favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['C'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name + " favorite language is " + str(languages))
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())