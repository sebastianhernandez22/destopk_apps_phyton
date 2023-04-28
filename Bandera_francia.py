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
ventana_principal.title("Bandera de Francia")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana

#-------------------------------------
# frama azul
#-------------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=200, height=600)
frame_azul.place(x=0, y=0)

#-------------------------------------
# frama blanco
#-------------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white", width=200, height=600)
frame_blanco.place(x=200, y=0)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=200, height=600)
frame_rojo.place(x=400, y=0)

# run
# se ejecuta el metodomanloop() de la case Tk() a travéz de la instancia ventana_principal. este metodo desplega la ventana en pantalla y queda a la espera de lo que el usuario haga(Click en un boton, escribir, etc). cada accion del usuario se conoce como un evento. El metodo mainloopa() es un bucle infinito.
ventana_principal.mainloop()
