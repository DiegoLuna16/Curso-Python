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
        
if __name__ == "__main__":
    transformar_audio_en_texto()