from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Crear base de datos
def crear_base():
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            prenda TEXT,
            cantidad INTEGER,
            precio REAL,
            movilidad REAL,
            direccion TEXT,
            estado TEXT
        )
    """)

    conexion.commit()
    conexion.close()

crear_base()

@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":
        fecha = request.form["fecha"]
        prenda = request.form["prenda"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]
        movilidad = request.form["movilidad"]
        direccion = request.form["direccion"]
        estado = request.form["estado"]

        conexion = sqlite3.connect("ventas.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO ventas (fecha, prenda, cantidad, precio, movilidad, direccion, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (fecha, prenda, cantidad, precio, movilidad, direccion, estado))

        conexion.commit()
        conexion.close()

    return render_template("formulario.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
