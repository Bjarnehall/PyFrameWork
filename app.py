from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from home!"

@app.route("/about")
def about(request,response):
    response.text = "Hello from about!"