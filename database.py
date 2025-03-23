import sqlite3

def conectar():
    conexion = sqlite3.connect("notas.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()

def agregar_nota(titulo, contenido):
    conexion = sqlite3.connect("notas.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO notas (titulo, contenido) VALUES (?, ?)", (titulo, contenido))
    conexion.commit()
    conexion.close()

def obtener_notas():
    conexion = sqlite3.connect("notas.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    conexion.close()
    return notas

def actualizar_nota(id_nota, titulo, contenido):
    conexion = sqlite3.connect("notas.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, contenido = ? WHERE id = ?", (titulo, contenido, id_nota))
    conexion.commit()
    conexion.close()

def eliminar_nota(id_nota):
    conexion = sqlite3.connect("notas.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM notas WHERE id = ?", (id_nota,))
    conexion.commit()
    conexion.close()

# Asegurar que la base de datos se crea al importar este módulo
conectar()
