from flask import Flask

app = Flask(__name__)

@app.route("/user/<string:user>")
def user(user):
    return "Hola Mundo " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {1} nombre:{0}".format(id,name)


if __name__ == "_main_":
    app.run(debug=True)