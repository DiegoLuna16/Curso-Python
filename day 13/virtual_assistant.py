import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
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
    
pedir_hora()