admins=['dmitriy', 'roman', 'alexandr', 'vladislav', 'nikolay']
users_admin=input("Enter name users: ")
for admin in admins:
    if admin in users_admin :
        print("Hello admin " + admin)
    else:
        print("You do have not administrator right")
    break