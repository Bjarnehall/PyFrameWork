from functions import greet_from_python, snake_menu
from api import API

app = API()

# Makes is possible to render template
def render_template(template, **kwargs):
    for key, value in kwargs.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template


# Home takes a html template and uses information from functions.py
@app.route("/")
def home(request, response):
    with open("home.html", "r") as file:
        template = file.read()

    greeting = greet_from_python()
    nav_menu = snake_menu()
    
    response.text = render_template(template, greet_from_python=greeting, snake_menu=nav_menu)
    response.content_type = "text/html"

@app.route("/About")
def about(request,response):
    response.text = "Hello from about!"

@app.route("/Contact")
def contact(request,response):
    response.text = "Hello from contact!"
