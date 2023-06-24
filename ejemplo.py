def retornar_texto(texto):
    texto = texto.lower()
    opciones = {
        "idea": "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.3.1\\bin\\idea64.exe",
        "opera": "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\launcher.exe www.google.com",
        "spotify": "C:\\Users\\USER\\AppData\\Local\\Programs\\Opera GX\\spotify.exe",
    }
    return opciones.get(texto, "Don't understand your message")

# print(retornar_texto('idea'))



def elpepe(str):
    array1 = str.split(' ')
    array1.remove('open')
    array1.remove('and')
    
    array3 = []
    
    for i in array1:
        array3.append(retornar_texto(i))
        
    return array3
    
print(elpepe("open idea opera and spotify"))