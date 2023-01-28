from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"


@app.route("/")
def hola():
    return "Hola todo"


@app.route("/")
def nueva():
    return "Hola todo"



if __name__ == "_main_":
    app.run(debug=True)