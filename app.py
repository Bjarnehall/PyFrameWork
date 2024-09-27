from api import API
from functions import greet_from_python
app = API()

# Makes is possible to render template
def render_template(template, **kwargs):
    for key, value in kwargs.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template


# Home takes a html template and uses information from functions.py
@app.route("/home")
def home(request, response):
    with open("home.html", "r") as file:
        template = file.read()
    
    greeting = greet_from_python()
    
    response.text = render_template(template, greet_from_python=greeting)
    response.content_type = "text/html"

@app.route("/about")
def about(request,response):
    response.text = "Hello from about!"