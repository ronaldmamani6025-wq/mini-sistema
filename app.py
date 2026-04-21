from flask import Flask, request, redirect

app = Flask(__name__)

empleados = []

@app.route("/")
def inicio():
    lista = ""
    for e in empleados:
        lista += f"<li>{e}</li>"

    return f"""
    <h2>Registro de Empleados</h2>

    <form method="POST" action="/agregar">
        Nombre: <input name="nombre">
        <button>Agregar</button>
    </form>

    <h3>Lista:</h3>
    <ul>{lista}</ul>
    """

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    empleados.append(nombre)
    return redirect("/")

app.run(host="0.0.0.0", port=10000)