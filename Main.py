alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direcction = input("escribir 'encode' para encriptar y 'decode' para desencritar:\n").lower()
text = input("Type your message:\n").lower() 
shift = int(input("Type the shift number:\n"))

# TODO 1- Crear una función 'encrypt()' que toma el valor inicial de una palabra y la convierte con 2 entradas
#
# TODO 2- Dentro de la funcion 'encrypt()', desplaza cada letra original el numero de veces que se indica
#
# hello , desplazo 2
def encript(original_text, shift_amount):
    cipher_text = ""
    
    for letter in original_text:
        shifted_position=  alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) #Hacemos modulo con el desplazamiento de la letra porque podemos pasarnos de la Z
        cipher_text += alphabet[ shifted_position]

    print(f"Aqui es el resultado codificado:{cipher_text}")

encript(original_text = text, shift_amount = shift)