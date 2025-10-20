from tkinter import *

operador = ''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)
    
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)
    
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''

#iniciar tkinter
app = Tk()

#tamaño de la pantalla
app.geometry('1195x500+700+350')

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
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='black'
                        ,font=('Dosis',58,'italic'), bg='burlywood',width=25)
etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo 
panel_izquierdo = Frame(app,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT, bg='azure4',padx=40)
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
lista_comidas = [
    'pollo', 'tacos', 'quesadillas',
    'papa rellena', 'sopes', 'chilaquiles', 'enchiladas',
    'pozole'
]

lista_bebidas = [
    'Coca Cola', 'Pepsi', 'Manzanita',
    'Agua de Horchata', 'Agua de Jamaica', 'Agua de limon',
    'Té helado', 'Chocolate caliente'
]

lista_postres = [
    'Flan', 'Pay de queso', 'Pastel de 3 leches', 'Pastel de chocolate',
     'Nieve de limon', 'Nieve de vainilla',
    'Churros', 'Brownie'
]


#generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []


contador = 0
for comida in lista_comidas:
    #crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)
    
    #crear los cuadros de entrada 
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',15,'bold'),
                                     bd=1,
                                     width=4,
                                     state=DISABLED,
                                     relief='raised',
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1
    
#generar items bebida
variables_bebida = []
contador = 0
cuadros_bebida = []
texto_bebida = []

for bebida in lista_bebidas:
    
    #crear checkbuttons
    
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)
    
    #crear los cuadros de entrada 
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis',15,'bold'),
                                     bd=1,
                                     width=4,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1
    
#generar items postre
variables_postre = []
contador = 0
cuadros_postre = []
texto_postre = []

for postre in lista_postres:
    
    #crear checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)
    
    #crear los cuadros de entrada 
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis',15,'bold'),
                                     bd=1,
                                     width=4,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

# etiquetas de costo y campos de entrada

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuesto = Label(panel_costos,
                              text='Costo Impuestos',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_impuesto)

texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Costo Total',
                              font=('Dosis',13,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis',13,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_total)

texto_total.grid(row=2, column=3, padx=41)

#botones 
botones = ['total','recibo','guardar','resetear']

columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Helvetica',14,'bold'),
                   fg='black',
                   bg='#3c3c3c',
                   bd=1,
                   width=6)
    boton.grid(row=0,
               column=columnas)
    
    columnas += 1
    
#area de recibo 
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=35,
                    height=10)

texto_recibo.grid(row=0, column=0)

#calculadora 
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis','16','bold'),
                          width=28
                          )

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       'R','B','0','/']

botones_guardados = []

fila = 1
columa = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='black',
                   bg='azure4',
                   width=6)
    
    botones_guardados.append(boton)
    
    boton.grid(row=fila,column=columa)
    if columa == 3:
        fila +=1
    
    columa += 1    
    
    if columa == 4:    
        columa = 0
        
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

#evitar que la pantalla se cierre
app.mainloop()
