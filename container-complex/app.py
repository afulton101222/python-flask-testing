from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the main page for a dockerized python container. <h1>HELLO!<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')