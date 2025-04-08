import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import reduce

# Lista de materias y aspectosa evaluar
materias = [
    "Programación web",
    "Inteligencia Artificial",
    "Administración de redes",
    "Redes"
]
aspectos = [
    "Contenido",
    "complejidad",
    "Herramientas",
    "Prácticas"
]

# Funciones
def promedio(valores):
    return reduce(lambda x, y: x + y, valores) / len(valores)

def total(valores):
    return reduce(lambda x, y: x + y, valores)

def maximo(valores):
    return reduce(lambda x, y: x if x > y else y, valores)

def minimo(valores):
    return reduce(lambda x, y: x if x < y else y, valores)

# Filtros
def filtro_materia(encuestas, materia):
    return list(filter(lambda e: e["materia"] == materia, encuestas))

def filtro_alumno(encuestas, nombre):
    return list(filter(lambda e: e["nombre"].lower() == nombre.lower(), encuestas))

def obtener_valores(encuestas_local, aspecto_key):
    return list(map(lambda e: e[aspecto_key], encuestas_local))

# Resultados por aspecto
def resultados(encuesta):
    resultado = {}
    for aspecto in aspectos:
        valores = obtener_valores(encuesta, aspecto)
        resultado[aspecto] = {
            "promedio": promedio(valores),
            "total": total(valores),
            "maximo": maximo(valores),
            "minimo": minimo(valores)
        }
    return resultado

# Mostrar resultados recursivamente por materia
def mostrar_resultados(encuestas, i=0):
    if i >= len(materias):
        return
    materia = materias[i]
    encuestas_materia = filtro_materia(encuestas, materia)
    if encuestas_materia:
        resultado = resultados(encuestas_materia)
        messagebox.showinfo(f"Resultados para {materia}", format_resultado(resultado))
    mostrar_resultados(encuestas, i + 1)

# Validación de calificaciones
def validar(valores):
    return len(list(filter(lambda x: x < 1 or x > 5, valores))) == 0

def format_resultado(diccionario):
    texto = ""
    for aspecto, datos in diccionario.items():
        texto += f"{aspecto}:\n"
        for k, v in datos.items():
            texto += f"   {k.capitalize()}: {v:.2f}\n"
    return texto

# -GUI 
class EncuestaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluación de Asignaturas")
        self.encuestas = []

        self.nombre_var = tk.StringVar()
        self.materia_var = tk.StringVar()
        self.calificaciones = {}

        tk.Label(root, text="Nombre del Alumno:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1)

        tk.Label(root, text="Materia:").grid(row=1, column=0)
        self.materia_menu = tk.OptionMenu(root, self.materia_var, *materias)
        self.materia_menu.grid(row=1, column=1)

        self.entries = {}
        for i, aspecto in enumerate(aspectos):
            tk.Label(root, text=aspecto).grid(row=i + 2, column=0)
            var = tk.IntVar()
            self.entries[aspecto] = tk.Entry(root)
            self.entries[aspecto].grid(row=i + 2, column=1)

        tk.Button(root, text="Enviar evaluación", command=self.enviar).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Mostrar resultados", command=lambda: mostrar_resultados(self.encuestas)).grid(row=7, column=0, columnspan=2)

    def enviar(self):
        nombre = self.nombre_var.get().strip()
        materia = self.materia_var.get().strip()
        try:
            calificaciones = [int(self.entries[a].get()) for a in aspectos]
        except ValueError:
            messagebox.showerror("Error", "Todas las calificaciones deben ser números enteros.")
            return

        if not nombre or not materia:
            messagebox.showerror("Error", "Por favor completa tu nombre y selecciona una materia.")
            return

        if not validar(calificaciones):
            messagebox.showerror("Error", "Las calificaciones deben estar entre 1 y 5.")
            return

        encuesta = {
            "nombre": nombre,
            "materia": materia
        }
        for i, aspecto in enumerate(aspectos):
            encuesta[aspecto] = calificaciones[i]

        self.encuestas.append(encuesta)
        messagebox.showinfo("Éxito", "Encuesta registrada exitosamente.")
        self.limpiar()

    def limpiar(self):
        self.nombre_var.set("")
        self.materia_var.set("")
        for entry in self.entries.values():
            entry.delete(0, tk.END)

#Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = EncuestaGUI(root)
    root.mainloop()
