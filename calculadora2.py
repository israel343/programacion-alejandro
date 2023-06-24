import tkinter as tk

def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="Resultado: " + str(resultado))
    
def resta():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="Resultado: " + str(resultado))
    
def multi():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="Resultado: " + str(resultado))
    
def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 / num2
    label_resultado.config(text="Resultado: " + str(resultado))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")

# Crear los widgets
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

btn_sumar = tk.Button(ventana, text="Sumar", command=sumar)
btn_sumar.pack()

btn_resta = tk.Button(ventana, text="Restar", command=resta)
btn_resta.pack()

btn_mu = tk.Button(ventana, text="Multiplicación", command=multi)
btn_mu.pack()

btn_di = tk.Button(ventana, text="División", command=dividir)
btn_di.pack()

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

#TAREA
#Crear una calculadora
# git add .
# git commit -m "mensaje"
# git push


#git pull
#git checkout