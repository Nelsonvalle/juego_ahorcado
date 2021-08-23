from tkinter import *
#--------Frame de la calculadora---------
raiz= Tk()
frameCalculadora = Frame(raiz)
frameCalculadora.pack()

#-------------------Se crea la pantalla----------------------
pantalla = Entry(frameCalculadora)
pantalla.grid(row=1, column= 1,padx=10,pady=10,columnspan= 4)
pantalla.config(background="black",fg="#097cd4",justify="right")

#------------------Se crea la primera linea de botones de la calculadora----------------
boton7 = Button(frameCalculadora, text="7",width=3)
boton7.grid(row=2, column=1)
boton8 = Button(frameCalculadora, text="8",width=3)
boton8.grid(row=2,column=2)
boton9 = Button(frameCalculadora, text="9",width=3)
boton9.grid(row=2,column=3)
botondiv = Button(frameCalculadora, text="/",width=3)
botondiv.grid(row=2, column=4)

#------------------Se crea la segunda linea de botones de la calculadora----------------
boton4 = Button(frameCalculadora, text="4",width=3)
boton4.grid(row=3, column=1)
boton5 = Button(frameCalculadora, text="5",width=3)
boton5.grid(row=3,column=2)
boton6 = Button(frameCalculadora, text="6",width=3)
boton6.grid(row=3,column=3)
botonmult = Button(frameCalculadora, text="X",width=3)
botonmult.grid(row=3, column=4)

#------------------Se crea la tercera linea de botones de la calculadora----------------
boton1 = Button(frameCalculadora, text="1",width=3)
boton1.grid(row=4, column=1)
boton2 = Button(frameCalculadora, text="2",width=3)
boton2.grid(row=4,column=2)
boton3 = Button(frameCalculadora, text="3",width=3)
boton3.grid(row=4,column=3)
botonrestar = Button(frameCalculadora, text="-",width=3)
botonrestar.grid(row=4, column=4)

#------------------Se crea la cuarta linea de botones de la calculadora----------------
boton0 = Button(frameCalculadora, text="0",width=3)
boton0.grid(row=5, column=1)
botoncoma = Button(frameCalculadora, text=",",width=3)
botoncoma.grid(row=5,column=2)
botonigual = Button(frameCalculadora, text="=",width=3)
botonigual.grid(row=5,column=3)
botonsuma = Button(frameCalculadora, text="-",width=3)
botonsuma.grid(row=5, column=4)



raiz.mainloop()