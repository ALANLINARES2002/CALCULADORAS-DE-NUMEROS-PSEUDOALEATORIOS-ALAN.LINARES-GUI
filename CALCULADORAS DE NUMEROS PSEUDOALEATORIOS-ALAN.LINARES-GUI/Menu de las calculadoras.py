import tkinter as tk
from tkinter import ttk, messagebox

# ✅ Cambia los nombres de los módulos según los archivos reales
from cuadrados_medios1 import CuadradosMediosApp  # <-- Nombre real del archivo
from Productos_Medios2 import ProductosMediosApp   # <-- Nombre real del archivo
from Multiplicador_Constante3 import MultiplicadorConstanteApp  # <-- Nombre real del archivo

class MenuCalculadorasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULADORAS DE NUMEROS PSEUDOALEATORIOS")
        self.root.geometry("600x400")
        self.root.configure(bg="#007BFF")  # Azul claro

        # Estilo personalizado
        style = ttk.Style()
        style.theme_use('clam')

        # Colores
        azul = "#007BFF"     # Fondo principal (azul)
        turquesa = "#00BCD4" # Botones y encabezados (turquesa)
        blanco = "white"

        # Configurar estilos
        style.configure("TButton", background=turquesa, foreground="white", font=("Arial", 12, "bold"))
        style.map("TButton", background=[('active', '#0096C7')])

        # Título central
        title_label = tk.Label(
            self.root,
            text="CALCULADORAS DE NUMEROS PSEUDOALEATORIOS",
            font=("Arial", 18, "bold"),
            bg=azul,
            fg="white"
        )
        title_label.pack(pady=20)

        # Frame para los botones
        button_frame = tk.Frame(self.root, bg=azul)
        button_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=20)

        # Botón 1: Cuadrados Medios
        ttk.Button(
            button_frame,
            text="1. Algoritmo de Cuadrados Medios",
            command=self.abrir_cuadrados_medios,
            style="TButton"
        ).pack(pady=15, fill=tk.X, padx=20)

        # Botón 2: Productos Medios
        ttk.Button(
            button_frame,
            text="2. Algoritmo de Productos Medios",
            command=self.abrir_productos_medios,
            style="TButton"
        ).pack(pady=15, fill=tk.X, padx=20)

        # Botón 3: Multiplicador Constante
        ttk.Button(
            button_frame,
            text="3. Algoritmo de Multiplicador Constante",
            command=self.abrir_multiplicador_constante,
            style="TButton"
        ).pack(pady=15, fill=tk.X, padx=20)

        # Botón Salir
        ttk.Button(
            button_frame,
            text="❌ Salir",
            command=self.root.quit,
            style="TButton"
        ).pack(pady=20, fill=tk.X, padx=20)

    def abrir_cuadrados_medios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Cuadrados Medios")
        app = CuadradosMediosApp(ventana)

    def abrir_productos_medios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Productos Medios")
        app = ProductosMediosApp(ventana)

    def abrir_multiplicador_constante(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Multiplicador Constante")
        app = MultiplicadorConstanteApp(ventana)


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuCalculadorasApp(root)
    root.mainloop()