from tkinter import *

raiz= Tk()
raiz.title("VENTANA DE PRUEBA")
raiz.resizable(1,1)
#raiz.geometry("600x300")
raiz.config(bg= "green")  #bg = background
# Aqui se crea el Frame
framePrincipal= Frame(raiz)
framePrincipal.pack(side= "left", anchor= "s") #para ubicar el frame en alguna posicion (derecha,izquierda)
framePrincipal.config(width= "600", height= "350")
framePrincipal.config(bg= "red")
framePrincipal.config(bd= 20)  #bd= border
framePrincipal.config(relief = "groove")
framePrincipal.config(cursor= "hand2")

#Aqui se introducen label, cuadro txt

labelMenu = Label(framePrincipal,text= "Menú Principal",fg="blue",font=(18)).grid(row= 0, column= 2)
labelAdminFrase = Label(framePrincipal,text= "Boton-->",fg="black",font=(12)).grid(row= 3, column= 0,sticky= "e",padx=10,pady=10)
#txtAdminFrase = Entry(framePrincipal,fg="black",font=(12)).grid(row= 3, column= 1) #fg:color letra
labelAdminJuego = Label(framePrincipal,text= "Boton-->",fg="black",font=(12)).grid(row= 3, column= 2,sticky= "e",padx=10,pady=10)
#txtAdminJuego = Entry(framePrincipal,fg="black",font=(12)).grid(row= 3, column= 3,padx=10,pady=10) #fg:color letra
labelAdminJugadores = Label(framePrincipal,text= "Boton-->",fg="black",font=(12)).grid(row= 4, column= 0,sticky= "e",padx=10,pady=10)
#txtAdminJugadores = Entry(framePrincipal,fg="black",font=(2)).grid(row= 4, column= 1) #fg:color letra
labelsalir = Label(framePrincipal,text= "Boton-->",fg="black",font=(12)).grid(row= 4, column= 2,sticky= "e",padx=10,pady=10)
#txtSalir = Entry(framePrincipal,fg="black",font=(12)).grid(row= 4, column= 3,padx=10,pady=10) #fg:color letra

#Aquis se agregan botones
botonAdminFrase = Button(framePrincipal,text= "Admin Frases").grid(row= 3, column= 1)
botonAdminJuego = Button(framePrincipal,text= "Admin Juego").grid(row= 3, column= 3,padx=10,pady=10)
botonAdminJugadores = Button(framePrincipal,text= "Admin Jugadores").grid(row= 4, column= 1)
botonsalir = Button(framePrincipal,text= "Salir").grid(row= 4, column= 3,padx=10,pady=10)


raiz.mainloop()