
admins=['dmitriy', 'roman', 'alexandr', 'vladislav', 'nikolay']
users_admin=[str(input("Enter name users: "))]
for admin in users_admin:
    if admin in admins :
        print("Hello admin " + admin)
    else:
        print("You do have not administrator right")
    #break