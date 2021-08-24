from tkinter import *

#Creacion raiz:
raiz= Tk()
raiz.title("Ventana Principal")
raiz.resizable(1,1)
# Aqui se crea el Frame
framePrincipal= Frame()
framePrincipal.pack
framePrincipal.pack(side= "left", anchor= "s") #para ubicar el frame en alguna posicion (derecha,izquierda)
framePrincipal.config(width= "600", height= "350")
framePrincipal.config(bg= "#374a75")
framePrincipal.config(bd= 10)  #bd= border
framePrincipal.config(relief = "groove")
framePrincipal.config(cursor= "hand2")

#---------------Creacion label titulo ventana principal--------------------------
labVentanaPrincipal = Label(framePrincipal,text= "Menú Juego",fg="Black",font=(12),background="#08e2ff")\
    .grid(row= 1, column= 1,padx=10,pady=10,columnspan= 2)


#---------------Creacion botones ventana principal--------------------------
botonJuego = Button(framePrincipal, text="Jugar",width=8,background="#86fff8",fg="black")
botonJuego.grid(row=3, column=1,sticky= "e",padx=10,pady=10)
botonJugadores = Button(framePrincipal, text="Jugadores",width=8,background="#86fff8")
botonJugadores.grid(row=3,column=2,sticky= "e",padx=10,pady=10)
botonEstadisticas = Button(framePrincipal, text="Estadisticas",width=8,background="#86fff8")
botonEstadisticas.grid(row=4,column=1,sticky= "e",padx=10,pady=10)
botonSalir = Button(framePrincipal, text="Salir",width=8,background="#86fff8")
botonSalir.grid(row=4, column=2,sticky= "e",padx=10,pady=10)

raiz.mainloop()

# .color1 {color: #121d25;}
# .color2 {color: #374a75;}
# .color3 {color: #08e2ff;}
# .color4 {color: #0ffff8;}
# .color5 {color: #86fff8;}