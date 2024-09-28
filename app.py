from functions import greet_from_python
from api import API

app = API()

# All menu pages go here
menu_items = [
    {
        "name": "Home",
        "route": "/"
    },
    {
        "name": "About",
        "route": "/about"
    },
    {
        "name": "Contact",
        "route": "/contact"
    }
]

# Makes is possible to render template
def render_template(template, **kwargs):
    for key, value in kwargs.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template

def snake_menu():
    menu = "<ul>"
    for item in menu_items:
        menu += f"<li><a href='{item['route']}'>{item['name']}</a></li>"
    menu += "</ul>"
    return menu

def create_routes(app, menu_items):
    for item in menu_items:
        route = item["route"]
        name = item["name"].lower()

        @app.route(route)
        def dynamic_route(request, response, name=name):
            try:
                with open(f"{name}.html", "r") as file:
                    template = file.read()
                greeting = greet_from_python()
                nav_menu = snake_menu()
                response.text = render_template(template, greet_from_python=greeting, snake_menu=nav_menu)
                response.content_type = "text/html"
            except FileNotFoundError:
                response.text = f"Hello from {name.lower()}!"
                response.content_type = "text/html"

create_routes(app, menu_items)
