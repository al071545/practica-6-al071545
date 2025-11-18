import tkinter as tk
from tkinter import ttk, messagebox
import time

# ---------------------------------------------------------
# FUNCIONES DEL CÁLCULO
# ---------------------------------------------------------

def calcular_area(a, b, h):
    return h * (a + b) / 2

def calcular_perimetro(a, b, h):
    lado = (h*2 + ((b - a)/2)**2)**0.5
    return a + b + 2 * lado

def calcular_radio(A, P):
    return A / P

def calcular_manning(n, A, R, S):
    return (1 / n) * A * (R*(2/3)) * (S*0.5)

# Tabla de valores n
tabla_n = {
    "Canal de tierra en mal estado (n=0.025)": 0.025,
    "Canal de tierra en buen estado (n=0.020)": 0.020,
    "Concreto nuevo (n=0.015)": 0.015,
    "Concreto desgastado (n=0.017)": 0.017,
    "Tubería PVC o PEAD (n=0.013)": 0.013
}

# ---------------------------------------------------------
# ANIMACIÓN DEL TÍTULO
# ---------------------------------------------------------

colores = ["#1a73e8", "#0a9396", "#ee9b00", "#9b2226"]

def animar_titulo():
    actual = colores.pop(0)
    colores.append(actual)
    titulo.config(fg=actual)
    ventana.after(600, animar_titulo)

# ---------------------------------------------------------
# FUNCIÓN PARA BOTÓN
# ---------------------------------------------------------

def ejecutar_calculo():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        h = float(entry_h.get())
        S = float(entry_S.get())

        if a <= 0 or b <= 0 or h <= 0 or S <= 0:
            messagebox.showerror("Error", "Todos los valores deben ser mayores que cero.")
            return

        tipo_seleccionado = combo_n.get()
        if tipo_seleccionado not in tabla_n:
            messagebox.showerror("Error", "Selecciona un tipo de canal.")
            return

        n = tabla_n[tipo_seleccionado]

        # Cálculos
        A = calcular_area(a, b, h)
        P = calcular_perimetro(a, b, h)
        R = calcular_radio(A, P)
        Q = calcular_manning(n, A, R, S)

        # Mostrar resultados en interfaz
        resultado_text.config(state="normal")
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "📊 RESULTADOS\n\n")
        resultado_text.insert(tk.END, f"Tipo de canal: {tipo_seleccionado}\n")
        resultado_text.insert(tk.END, f"Coeficiente n: {n}\n\n")
        resultado_text.insert(tk.END, f"Área A = {A:.4f} m²\n")
        resultado_text.insert(tk.END, f"Perímetro mojado P = {P:.4f} m\n")
        resultado_text.insert(tk.END, f"Radio hidráulico R = {R:.4f} m\n")
        resultado_text.insert(tk.END, f"Caudal Q = {Q:.4f} m³/s\n")
        resultado_text.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Introduce solo números válidos.")

# ---------------------------------------------------------
# INTERFAZ GRÁFICA
# ---------------------------------------------------------

ventana = tk.Tk()
ventana.title("Cálculo de Caudal - Manning")
ventana.geometry("520x650")
ventana.configure(bg="#e9ecef")

# TÍTULO ANIMADO
titulo = tk.Label(ventana, text="Cálculo del Caudal (Manning)", 
                  font=("Arial", 20, "bold"), bg="#e9ecef")
titulo.pack(pady=20)

animar_titulo()

# FRAME PRINCIPAL
frame = tk.Frame(ventana, bg="#ffffff", relief="solid", bd=2)
frame.pack(pady=10, padx=10, fill="both")

# Entradas
tk.Label(frame, text="Base superior a (m):", bg="#ffffff").grid(row=0, column=0, pady=8, padx=8, sticky="w")
entry_a = tk.Entry(frame, width=20)
entry_a.grid(row=0, column=1)

tk.Label(frame, text="Base inferior b (m):", bg="#ffffff").grid(row=1, column=0, pady=8, padx=8, sticky="w")
entry_b = tk.Entry(frame, width=20)
entry_b.grid(row=1, column=1)

tk.Label(frame, text="Profundidad h (m):", bg="#ffffff").grid(row=2, column=0, pady=8, padx=8, sticky="w")
entry_h = tk.Entry(frame, width=20)
entry_h.grid(row=2, column=1)

tk.Label(frame, text="Pendiente S:", bg="#ffffff").grid(row=3, column=0, pady=8, padx=8, sticky="w")
entry_S = tk.Entry(frame, width=20)
entry_S.grid(row=3, column=1)

# Combobox
tk.Label(frame, text="Coeficiente n:", bg="#ffffff").grid(row=4, column=0, pady=8, padx=8, sticky="w")
combo_n = ttk.Combobox(frame, values=list(tabla_n.keys()), width=35)
combo_n.grid(row=4, column=1)

# Animación del botón
def on_enter(e):
    boton.config(bg="#2a9d8f")

def on_leave(e):
    boton.config(bg="#4CAF50")

boton = tk.Button(ventana, text="Calcular", command=ejecutar_calculo, 
                  bg="#4CAF50", fg="white", font=("Arial", 14), width=15)
boton.pack(pady=15)
boton.bind("<Enter>", on_enter)
boton.bind("<Leave>", on_leave)

# Resultados
tk.Label(ventana, text="Resultados:", bg="#e9ecef", 
         font=("Arial", 14, "bold")).pack()

resultado_text = tk.Text(ventana, height=13, width=60, state="disabled", bg="#ffffff", bd=2, relief="solid")
resultado_text.pack(pady=10)

ventana.mainloop()