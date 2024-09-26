from api import API

app = API()

def render_template(template, **kwargs):
    """Simple template rendering function."""
    for key, value in kwargs.items():
        template = template.replace(f"{{{{ {key} }}}}", value)
    return template

@app.route("/home")
def home(request, response):
    with open("home.html", "r") as file:
        template = file.read()
    
    # Call your function to get the message
    greeting = greet_from_python()
    
    # Render the template with the greeting
    response.text = render_template(template, greet_from_python=greeting)
    response.content_type = "text/html"  # Set the content type to HTML

@app.route("/about")
def about(request,response):
    response.text = "Hello from about!"