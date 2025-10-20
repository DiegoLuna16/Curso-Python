from tkinter import *

#iniciar tkinter
app = Tk()

#tamaño de la pantalla
app.geometry('1020x630+700+350')

# evitar maximizar 

app.resizable(0,0)

#titulo de la ventana 
app.title('Mi restaurante - Sistema de facturacion')

#color de la ventana

app.config(bg='burlywood')

#panel superior 
panel_superior = Frame(app, bd=1,relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='azure4'
                        ,font=('Dosis',58), bg='burlywood',width=22)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo 
panel_izquierdo = Frame(app,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas 
panel_comidas = LabelFrame(panel_izquierdo,text='Comidas', font=('Dosis', 19, 'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas 
panel_bebidas = LabelFrame(panel_izquierdo,text='Bedidas', font=('Dosis', 19, 'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres 
panel_postres = LabelFrame(panel_izquierdo,text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(app,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo','tacos','salmon','quesadillas','papa rellena','sopes','chilaquiles','enchiladas']
lista_bebidas = ['Coca Cola','Pepsi','Fanta','Manzanita','Seven up','Agua de Horchata', 'Agua de Jamaica', 'Agua de limon']
lista_postres = ['Flan','Pay de queso','Pastel de 3 leches','Pastel de chocolate','Gelatina','Nieve de limon','Nieve de vainilla','Jericalla']

#generar items comida
variables_comida = []

contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis',13,'bold'),
                         onvalue=1, offvalue=0,variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
#generar items bebida
variables_bebida = []
contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis',13,'bold'),
                         onvalue=1, offvalue=0,variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
#generar items postres
variables_postre = []
contador = 0

for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis',13,'bold'),
                         onvalue=1, offvalue=0,variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1

#evitar que la pantalla se cierre
app.mainloop()
