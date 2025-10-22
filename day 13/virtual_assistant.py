import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():
    
    #almacenar recognizer en variable
    r = sr.Recognizer()
    
    #configurar el microfono
    with sr.Microphone() as origen:
        
        #tiempo de espera
        r.pause_threshold = 0.8
        
        # informar que comenzo la grabacion 
        print('Ya puedes hablar')
        
        #guardar lo que escuche como audio
        audio = r.listen(origen)
        
        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-MX")
            
            # prueba de que pudo ingresar
            print('Dijiste: ' + pedido)
            
            #devolver pedido
            return pedido
        
        except sr.UnknownValueError:
            
            #prueba de que no comprendio el audio
            print('ups, no entendi')

            # devolver error
            return 'sigo esperando'
        
        except sr.RequestError:
            
            #prueba de que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return 'sigo esperando'
        
        except :
            
            #prueba de que no comprendio el audio
            print('ups, algo ha salido mal')

            # devolver error
            return 'sigo esperando'
        
#funcion para el asistente puede ser escuchado
def hablar(mensaje):
    
    #encender el motor de pyttsx3
    engine = pyttsx3.init()
    
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar dia de la semana 

def pedir_dia():
    #crear varible con datos de hoy
    
    dia = datetime.datetime.today()
    print(dia)
    
    #crear variable para el dia de la semana
    dia_semana = dia.weekday()
    
    #calendario
    calendario={0:'Lunes',
               1:'Martes',
               2:'Miércoles',
               3:'Jueves',
               4:'Viernes',
               5:'Sábado',
               6:'Domingo'}
    
    #decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')
    
# informar que hora es
def pedir_hora():
    
    #crear variable con los datos de la hora
    hora = datetime.datetime.now()
    
    # decir la hora 
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    hablar(hora)
    
def saludo_inicial():
    
    #crear variable con datos de hora
    
    hora = datetime.datetime.now()
    
    if hora.hour < 6 or hora.hour > 19:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 12:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    
    #decir el saludo
    hablar(f"{momento}, soy Siri, tu asistente personal. Por favor, dime en que te puedo ayudar.")

#funcion central del asistente
def pedir_cosas():
    
    #activar saludo incial
    saludo_inicial()
    
    #variable de corte
    
    comenzar = True
    
    #loop central
    
    while comenzar:
        
        #activar el micro y guardar el pedido en un string 
        pedido = transformar_audio_en_texto().lower()
        print(pedido)
        
        if  'abrir youtube' in pedido:
            hablar('con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences = 1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'repite' in pedido:
            pedido = pedido.replace('repite','')
            hablar(pedido)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo lo busco')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar('Esto es lo que encontré')
            continue
        elif 'reproduce' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pedido = pedido.replace('reproduce','')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no lo he encontrado')
                continue
        elif 'salir' in pedido:
            hablar('Hasta luego')
            comenzar = False
            
pedir_cosas()