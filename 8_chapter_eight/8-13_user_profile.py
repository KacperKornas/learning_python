def build_profile(first, last, **user_info):
    """Stores information about person."""
    profile = {}
    profile['name'] = first
    profile['surname'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('kacper', 'kornaś',
                             location='UP',
                             field='ETI')

print(user_profile)