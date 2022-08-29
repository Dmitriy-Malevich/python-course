
current_users=['dmitriy', 'roman', 'alexandr', 'vladislav', 'nikolay']
new_users=['Dmitriy', 'vladislav', 'petr', 'ivan', 'egor']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This name " + new_user + " is taken!, choose another")
    else:
        print("You are registrated " + new_user)

