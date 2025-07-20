from flask import Flask, render_template, request, redirect, url_for
from models.cola import ColaTarjetas
from models.pila import PilaApoyos

app = Flask(__name__)

cola = ColaTarjetas()
pila = PilaApoyos()

@app.route("/")
@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/cola", methods=["GET", "POST"])
def vista_cola():
    mensaje = ""
    if request.method == "POST":
        if "agregar" in request.form:
            nombre = request.form.get("nombre")
            if nombre:
                cola.encolar(nombre)
        elif "atender" in request.form:
            mensaje = cola.desencolar()
    return render_template("cola.html", cola=cola.mostrar(), mensaje=mensaje)

@app.route("/pila", methods=["GET", "POST"])
def vista_pila():
    mensaje = ""
    if request.method == "POST":
        if "agregar" in request.form:
            apoyo = request.form.get("apoyo")
            if apoyo:
                pila.empilar(apoyo)
        elif "quitar" in request.form:
            mensaje = pila.desempilar()
    return render_template("pila.html", pila=pila.mostrar(), mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
