from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# 🔹 Función para conectar a la base
def get_db_connection():
    conn = sqlite3.connect("ventas.db")
    conn.row_factory = sqlite3.Row
    return conn

# 🔹 Crear base de datos y tabla si no existen
def crear_base():
    conn = get_db_connection()
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()

# 🔹 Ruta principal (formulario)
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

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO ventas (fecha, prenda, cantidad, precio, movilidad, direccion, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (fecha, prenda, cantidad, precio, movilidad, direccion, estado))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("formulario.html")

# 🔹 Ruta admin (panel para ver registros)
@app.route("/admin")
def admin():
    conn = get_db_connection()
    ventas = conn.execute("SELECT * FROM ventas").fetchall()
    conn.close()

    return render_template("admin.html", ventas=ventas)

# 🔹 Inicializar aplicación
if __name__ == "__main__":
    crear_base()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
