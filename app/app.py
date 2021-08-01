from flask import Flask, Markup, render_template
from logic import square_of_number_plus_nine

# Create Flask's 'app' object
app = Flask(__name__)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)

@app.route("/logic")
def logic():
    value = square_of_number_plus_nine(5)
    return str(value)

@app.route("/markup")
def markup():
    return Markup("<h1>Hello World!</h1>")

@app.route("/template")
def hello_template():
    return render_template("index.html")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)