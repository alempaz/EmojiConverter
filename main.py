#Hacer un programa que pida al usuario un texto. Debe regresar el mismo texto y si escribe un emoji en texto, cambiar este a un emoji real

mensaje = input('>')
palabras = mensaje.split(' ')               # .split / Crea una lista con cada dato ingresado en un input, especificando el limitador de cada dato. (En este caso un ' ' (Espacio))
respuesta = ''

emojis = {
':)':'😀',':(':'😔',
':@':'🤬',';)':'😉'
}

for palabra in palabras:
    respuesta += emojis.get(palabra, palabra) + ' '
print(respuesta)