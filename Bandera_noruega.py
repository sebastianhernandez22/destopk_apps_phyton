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
ventana_principal.title("Bandera de Noruega")

# tamaño de la ventana
ventana_principal.geometry("800x600")

# desabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana

#-------------------------------------
# frama azul
#-------------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue4", width=800, height=80)
frame_azul.place(x=0, y=270)

#-------------------------------------
# frama azul
#-------------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue4", width=80, height=600)
frame_azul.place(x=270, y=0)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=250, height=100)
frame_rojo.place(x=0, y=500)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=250, height=200)
frame_rojo.place(x=0, y=370)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=250, height=250)
frame_rojo.place(x=0, y=0)

#-------------------------------------
# frama rojo
#-------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=200, height=100)
frame_rojo.place(x=0, y=0)

#------------------------------------
# frama rojo
#------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=500, height=250)
frame_rojo.place(x=370, y=0)

#------------------------------------
# frama rojo
#------------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red4", width=600, height=600)
frame_rojo.place(x=370, y=370)

# run
# se ejecuta el metodomanloop() de la case Tk() a travéz de la instancia ventana_principal. este metodo desplega la ventana en pantalla y queda a la espera de lo que el usuario haga(Click en un boton, escribir, etc). cada accion del usuario se conoce como un evento. El metodo mainloopa() es un bucle infinito.
ventana_principal.mainloop()