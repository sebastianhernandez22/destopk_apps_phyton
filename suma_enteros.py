from tkinter import *
from tkinter import messagebox

# funciones de la app

# sumar
def sumar():
    pass

# borrar
def borrar():
    pass

# salir
def salir():
    messagebox.showinfo("Suma Enteros 1.0" "La appp se va a cerrar")
    ventana_principal.destroy()

#Suma enteros
ventana_principal = Tk()

# ventana
ventana_principal.title("Suma de enteros")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="blue")

#----------------------------------
# variables globales
#----------------------------------

x = StringVar()
y = StringVar()

# frame entrada
Frame_entrada= Frame(ventana_principal)
Frame_entrada.config(bg="white", width=480, height=180)
Frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(Frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)


# titulo de la app
titulo = Label(Frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg="white", fg="blue", font=("Arial", 16))
titulo.place(x=240, y=10)

# etiqueta para valor de entrada
lb_x = Label(Frame_entrada, text = "x = ")
lb_x.config(bg="white", fg="blue", font=("Arial,14"))
lb_x.place(x=240, y=60)

# caja de texto para valor x
Entry_x = Entry(Frame_entrada, textvariable=x)
Entry_x.config(bg="white", fg="blue", font=("Times new Roman", 18), width=6)
Entry_x.focus_set()
Entry_x.place(x=290,y=50)

# etiqueta para valor de entrada
lb_y = Label(Frame_entrada, text = "y = ")
lb_y.config(bg="white", fg="blue", font=("Arial,14"))
lb_y.place(x=240, y=120)

# caja de texto para valor y
Entry_y = Entry(Frame_entrada, text = "y =")
Entry_y.config(bg="white", fg="blue", font=("Times new Roman", 18), width=6)
Entry_y.place(x=290,y=120)

# frame operaciones
Frame_operaciones = Frame(ventana_principal)
Frame_operaciones.config(bg="white", width=480, height=100)
Frame_operaciones.place(x=10, y=200)

#Boton para sumar
bt_sumar = Button(Frame_operaciones,text= "sumar", command=sumar)
bt_sumar.place(x=45, y=35, width=100, height=30)

#Boton para borrar
bt_borrar = Button(Frame_operaciones,text= "borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

#Boton para salir
bt_salir = Button(Frame_operaciones,text= "salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

# frame resultados
Frame_resultados = Frame(ventana_principal)
Frame_resultados.config(bg="white", width=480, height=180)
Frame_resultados.place(x=10, y=310)

# area de texto para resultados
t_resultados = Text(Frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier",20))
t_resultados.place(x=10, y=10, width=460, height=160)

# run
ventana_principal.mainloop()