from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/multiplicar/")
def multiplicar():

    return render_template("multipicar.html")

@app.route("/resultado", methods=["POST"])
def resultado():

    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    res=int(n1)*int(n2)
    return render_template("resultado.html", n1=n1,n2=n2,res=res)

if __name__=="_main_":
    app.run(debug=True)