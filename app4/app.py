from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return "Hello World!"

@app.route("/api/v1/users/", methods=['GET', 'POST', 'PUT'])
def users():
    #... Logic goes here

@app.route('/user/,username')
def profile(username):
    #... Logic goes here

@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    #... Logic goes here

if __name__ == '__main__':
    app.run(host='0.0.0.0', post=5003, debug=True)

