from flask import Flask

from flask import request
app = Flask(__name__)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():

        return '''
            <form action="/operasBas" method="POST">
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>

            <label>N2: </label>
            <input type="text" name="num2"/></br></br>

            <input type="summit" value="sumar"/>

            <input type="summit" value="restar"/>

            <input type="summit" value="multiplicar"/>

            <input type="summit" value="dividir"/>
            </form>
        '''

if __name__ == "_main_":
    app.run(debug=True)