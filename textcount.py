def contar_caracteres(texto):
    # Crear un diccionario para almacenar el conteo de cada carácter
    conteo = {}
    
    # Recorrer cada carácter en el texto
    for caracter in texto:
        # Si el carácter ya está en el diccionario, incrementa su conteo
        if caracter in conteo:
            conteo[caracter] += 1
        # Si no está, agrégalo con un conteo inicial de 1
        else:
            conteo[caracter] = 1
    
    return conteo

# Pedir al usuario que ingrese el texto
texto = input("Ingresa el texto: ")

# Obtener el conteo de caracteres
conteo_resultado = contar_caracteres(texto)

# Mostrar los caracteres y sus respectivos conteos
for caracter, cantidad in conteo_resultado.items():
    print(f"'{caracter}': {cantidad}")