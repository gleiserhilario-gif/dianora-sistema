from flask import Flask, render_template
import sqlite3

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

@app.route("/")
def inicio():
    return render_template("formulario.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)