#pip install SpeechRecognition
#pip install pyaudio
#pip install pywinauto


import speech_recognition as sr
from pywinauto import application

command = 'open '

def retornar_texto(texto):
    texto = texto.lower()
    opciones = {
        command + "idea": "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.3.1\\bin\\idea64.exe",
        command + "opera": "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe www.google.com",
    }
    return opciones.get(texto, "Don't understand your message")
    
# Función para abrir una aplicación
def abrir_aplicacion(aplicacion):
    try:
        app = application.Application().start(aplicacion)
        print(f"Aplicación {aplicacion} abierta correctamente.")
    except Exception as e:
        print(f"No se pudo abrir la aplicación {aplicacion}. Error: {str(e)}")

# Inicializar el reconocimiento de voz
r = sr.Recognizer()

# Configurar el micrófono como fuente de audio
mic = sr.Microphone()

# Obtener entrada de voz
with mic as source:
    print("Diga el nombre de la aplicación que desea abrir:")
    r.adjust_for_ambient_noise(source)  # Ajustar al ruido ambiental
    audio = r.listen(source)

# Utilizar el reconocimiento de voz de Google para obtener el texto
try:
    aplicacion = r.recognize_google(audio)
    print(f"Texto reconocido: {aplicacion}")
    #abrir_aplicacion(aplicacion)
    abrir_aplicacion(retornar_texto(aplicacion))
except sr.UnknownValueError:
    print("No se pudo reconocer el comando de voz.")
except sr.RequestError:
    print("Error al conectarse al servicio de reconocimiento de voz.")
    
