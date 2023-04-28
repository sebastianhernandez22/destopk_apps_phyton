#-------------------------------------
# Desktop app No. 1
#-------------------------------------

# se import la libreria tkinter con todas sus fonciones
from tkinter import *

#-------------------------------------
# funciones de la app
#-------------------------------------

#-------------------------------------
# ventana principal de la app
#-------------------------------------

# se declara una variable llamado ventana_principal, que adquiere las caracteŕsticas de un objeto Tk()
ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title("Bandera de Suiza")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="red")

#-------------------------------------
# frama blanco
#-------------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white", width=100, height=300)
frame_blanco.place(x=200, y=100)

#-------------------------------------
# frama blanco2
#-------------------------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2.config(bg="white", width=300, height=100)
frame_blanco2.place(x=100, y=200)

# run
# se ejecuta el metodomanloop() de la case Tk() a travéz de la instancia ventana_principal. este metodo desplega la ventana en pantalla y queda a la espera de lo que el usuario haga(Click en un boton, escribir, etc). cada accion del usuario se conoce como un evento. El metodo mainloopa() es un bucle infinito.
ventana_principal.mainloop()
