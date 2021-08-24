from tkinter import *

#Creacion raiz:
raiz= Tk()
raiz.title("Ventana Frases")
raiz.resizable(1,1)
# Aqui se crea el Frame
frameFrases= Frame(raiz)
frameFrases.pack
frameFrases.pack(side= "left", anchor= "s") #para ubicar el frame en alguna posicion (derecha,izquierda)
frameFrases.config(width= "600", height= "350")
frameFrases.config(bg= "#374a75")
frameFrases.config(bd= 10)  #bd= border
frameFrases.config(relief = "groove")
# frameFrases.config(cursor= "hand2")

#---------------Creacion label titulo ventana principal--------------------------
labVentanaFrases = Label(frameFrases,text= "Administracion De Frases",fg="Black",font=(12),background="#08e2ff",height=2)\
    .grid(row= 1, column= 1,padx=10,pady=10,columnspan= 3)


#-----------------------Creacion Lista de Frases-------------------------------
listaFrases= Listbox(frameFrases,fg="black",bg="#08e2ff",selectborderwidth=5,width= 50)
listaFrases.insert(0,"id,frase,enunciado")
listaFrases.insert(1,"1,perro,animal")
listaFrases.insert(2,"2,gato,animal")
listaFrases.grid(row=3, column=1,padx=10,pady=10,columnspan= 3)


#---------------Creacion botones ventana principal--------------------------
botonEditar = Button(frameFrases, text="Editar",width=8,height=2,background="#86fff8",fg="black")
botonEditar.grid(row=4, column=1,sticky= "w",padx=10,pady=10)
botonEliminar = Button(frameFrases, text="Eliminar",width=8,height=2,background="#86fff8",fg="black")
botonEliminar.grid(row=4,column=3,sticky= "e",padx=10,pady=10)
botonVolver = Button(frameFrases, text="Volver",width=8,height=2,background="#86fff8")
botonVolver.grid(row=4,column=2,sticky= "e",padx=10,pady=10)
# botonSalir = Button(framePrincipal, text="Salir",width=8,background="#86fff8")
# botonSalir.grid(row=4, column=2,sticky= "e",padx=10,pady=10)

raiz.mainloop()

# .color1 {color: #121d25;}
# .color2 {color: #374a75;}
# .color3 {color: #08e2ff;}
# .color4 {color: #0ffff8;}
# .color5 {color: #86fff8;}