from tkinter import *
#--------Frame de la calculadora---------
raiz= Tk()
frameCalculadora = Frame(raiz)
frameCalculadora.pack()
operacion = ""
resultado=0
#-------------------Se crea la pantalla----------------------

numeroPantalla= StringVar()
pantalla = Entry(frameCalculadora,textvariable=numeroPantalla)
pantalla.grid(row=1, column= 1,padx=10,pady=10,columnspan= 4)
pantalla.config(background="black",fg="#0ae75d",justify="right")

#---------------Pulsaciones teclado----------------------------
def numeroPulsado(num):
    global operacion
    if (operacion != ""):
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#-------funcion suma---------------------------------
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion= "suma"
    numeroPantalla.set(resultado)
#------------funcion el resultado para utilizar el boton =----------
def elResultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0

#------------------Se crea la cuarta linea de botones de la calculadora----------------
botonBorrar = Button(frameCalculadora, text="CE",width=4)
botonBorrar.grid(row=2, column=2,sticky= "e")
botonBorrarUltimo = Button(frameCalculadora, text="C",width=4)
botonBorrarUltimo.grid(row=2,column=3,sticky= "e")


#------------------Se crea la primera linea de botones de la calculadora----------------
boton7 = Button(frameCalculadora, text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)
boton8 = Button(frameCalculadora, text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=3,column=2)
boton9 = Button(frameCalculadora, text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=3,column=3)
botondiv = Button(frameCalculadora, text="/",width=3)
botondiv.grid(row=3, column=4)

#------------------Se crea la segunda linea de botones de la calculadora----------------
boton4 = Button(frameCalculadora, text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)
boton5 = Button(frameCalculadora, text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=4,column=2)
boton6 = Button(frameCalculadora, text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=4,column=3)
botonmult = Button(frameCalculadora, text="X",width=3)
botonmult.grid(row=4, column=4)

#------------------Se crea la tercera linea de botones de la calculadora----------------
boton1 = Button(frameCalculadora, text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton2 = Button(frameCalculadora, text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=5,column=2)
boton3 = Button(frameCalculadora, text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=5,column=3)
botonrestar = Button(frameCalculadora, text="-",width=3)
botonrestar.grid(row=5, column=4)

#------------------Se crea la cuarta linea de botones de la calculadora----------------
botoncero = Button(frameCalculadora, text="0",width=3,command=lambda:numeroPulsado("0"))
botoncero.grid(row=6, column=1)
botoncoma = Button(frameCalculadora, text=",",width=3,command=lambda:numeroPulsado("."))
botoncoma.grid(row=6,column=2)
botonigual = Button(frameCalculadora, text="=",width=3,command=lambda:elResultado())
botonigual.grid(row=6,column=3)
botonsuma = Button(frameCalculadora, text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonsuma.grid(row=6, column=4)



raiz.mainloop()