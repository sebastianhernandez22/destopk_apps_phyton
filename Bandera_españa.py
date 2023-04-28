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
ventana_principal.title("Bandera de España")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=150)
frame_rojo.place(x=0, y=0)

#-------------------------------------
# frama amarillo
#-------------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=475)
frame_amarillo.place(x=0, y=150)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=150)
frame_rojo.place(x=0, y=350)

# run
# se ejecuta el metodomanloop() de la case Tk() a travéz de la instancia ventana_principal. este metodo desplega la ventana en pantalla y queda a la espera de lo que el usuario haga(Click en un boton, escribir, etc). cada accion del usuario se conoce como un evento. El metodo mainloopa() es un bucle infinito.
ventana_principal.mainloop()
