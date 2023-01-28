from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    nombre="Homble Alaña"
    lista1=["Español","Ingles","Quimica"]
    return render_template("index.html",nombre=nombre,lista1=lista1)

@app.route("/usuarios")
def usuarios():
    return render_template("index2.html")

if __name__=="_main_":
    app.run(debug=True)