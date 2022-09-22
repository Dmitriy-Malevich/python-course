from unicodedata import name


def get_formatted_name(first, last, middle = ''):
    """Строит полное отформатированное имя."""
    if middle:
        full_name = first + " " + last + " " + middle
    else:
        full_name = first + " " + last
    return full_name.title() 