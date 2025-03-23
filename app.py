import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Para manejar imágenes
import time
import os
from database import agregar_nota, obtener_notas, actualizar_nota, eliminar_nota

# Función para mostrar la pantalla de inicio
def splash_screen():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("400x300+500+250")  # Ajusta según tu pantalla

    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((200, 200))  # Ajustar tamaño del logo
        logo = ImageTk.PhotoImage(logo_img)

        label = tk.Label(splash, image=logo, bg="black")
        label.image = logo  # Evita que Python borre la referencia
        label.pack(expand=True)

        splash.update()
        time.sleep(2)  # Muestra el logo por 2 segundos
    else:
        print("⚠️ Logo no encontrado: ", logo_path)

    splash.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("📒 Aplicación de Notas Mejorada")
root.geometry("650x500")
root.configure(bg="#f0f0f0")

# Icono de la aplicación
icon_path = os.path.join(os.path.dirname(__file__), "logo.png")
if os.path.exists(icon_path):
    root.iconphoto(True, tk.PhotoImage(file=icon_path))

# Llamar la pantalla de inicio antes de cargar la interfaz
splash_screen()

# Estilos
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", padding=5)

# Funciones de la app
def agregar():
    titulo = entry_titulo.get()
    contenido = text_contenido.get("1.0", tk.END).strip()
    if titulo.strip() and contenido:
        agregar_nota(titulo, contenido)
        messagebox.showinfo("Éxito", "Nota agregada correctamente.")
        entry_titulo.delete(0, tk.END)
        text_contenido.delete("1.0", tk.END)
        cargar_notas()
    else:
        messagebox.showwarning("Error", "El título y el contenido no pueden estar vacíos.")

def cargar_notas():
    listbox_notas.delete(*listbox_notas.get_children())
    notas = obtener_notas()
    for nota in notas:
        listbox_notas.insert("", tk.END, values=(nota[0], nota[1], nota[2]))

def eliminar():
    seleccion = listbox_notas.selection()
    if not seleccion:
        messagebox.showwarning("Error", "Selecciona una nota para eliminar.")
        return
    id_nota = listbox_notas.item(seleccion[0], "values")[0]
    confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar esta nota?")
    if confirmacion:
        eliminar_nota(id_nota)
        messagebox.showinfo("Éxito", "Nota eliminada correctamente.")
        cargar_notas()

def buscar():
    termino = entry_busqueda.get().lower()
    listbox_notas.delete(*listbox_notas.get_children())
    notas = obtener_notas()
    for nota in notas:
        if termino in nota[1].lower() or termino in nota[2].lower():
            listbox_notas.insert("", tk.END, values=(nota[0], nota[1], nota[2]))

# Widgets
frame_top = tk.Frame(root, bg="#f0f0f0")
frame_top.pack(pady=10)

ttk.Label(frame_top, text="Título:").grid(row=0, column=0)
entry_titulo = ttk.Entry(frame_top, width=40)
entry_titulo.grid(row=0, column=1, padx=5)

ttk.Label(frame_top, text="Contenido:").grid(row=1, column=0)
text_contenido = tk.Text(frame_top, width=40, height=5, font=("Arial", 10))
text_contenido.grid(row=1, column=1, padx=5, pady=5)

btn_agregar = ttk.Button(root, text="Agregar Nota", command=agregar)
btn_agregar.pack(pady=5)

frame_busqueda = tk.Frame(root, bg="#f0f0f0")
frame_busqueda.pack()

ttk.Label(frame_busqueda, text="Buscar:").pack(side=tk.LEFT)
entry_busqueda = ttk.Entry(frame_busqueda, width=30)
entry_busqueda.pack(side=tk.LEFT, padx=5)
btn_buscar = ttk.Button(frame_busqueda, text="Buscar", command=buscar)
btn_buscar.pack(side=tk.LEFT)

# Tabla de notas
columns = ("ID", "Título", "Contenido")
listbox_notas = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    listbox_notas.heading(col, text=col)
listbox_notas.pack(pady=5)

btn_eliminar = ttk.Button(root, text="Eliminar Nota", command=eliminar)
btn_eliminar.pack(pady=5)

cargar_notas()
root.mainloop()
