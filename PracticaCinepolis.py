from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def cinepolis():
    return render_template("cinepolis.html")

@app.route("/total", methods=["POST"])
def total():

    n1 = request.form.get("txtCantidadCompradores")
    n2 = request.form.get("txtBoletos")
    precioBoleto = 12
    

    if int(n2)>5:
        resultado = (int(n2)*precioBoleto)/1.15 

    elif ((int(n2)>2) and (int(n2) < 6)):
        resultado = (int(n2)*precioBoleto)/1.10 

    else:
        resultado = (int(n2)*precioBoleto) 

    return render_template("cinepolis.html", cant=n1, boletos=n2,resultado=resultado)



if __name__=="_main_":
    app.run(debug=True)