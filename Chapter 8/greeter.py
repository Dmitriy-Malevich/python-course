def get_formatted(first_name, last_name):
    """Возвращает аккуратно отформатированное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(ENTER 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted(f_name, l_name)
    print("\nHello, " + formatted_name + "!")