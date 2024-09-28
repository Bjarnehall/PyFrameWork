# functions.py
def greet_from_python():
    return "Hello from backend"

def snake_menu():
    menu_items = ["Home", "About", "Contact"]

    menu = "<ul>"
    for item in menu_items:
        if item == "Home":
            menu += f"<li><a href='/'>{item}</a></li>"
        else:
            menu += f"<li><a href='{item}'>{item}</a></li>"
    menu += "</ul>"
    return menu

