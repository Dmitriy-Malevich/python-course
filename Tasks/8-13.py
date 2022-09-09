def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
user_profile = build_profile('dmitriy', 'malevich', location = 'minsk')
print(user_profile)