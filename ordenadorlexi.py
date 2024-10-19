#Se usa selection sort para ordenar los nombres

def ordenar(lista):
    tamano_de_lista = len(lista)

    for posicion_actual in range(0, tamano_de_lista - 1):
        posicion_menor = posicion_actual
        nombre_menor = lista[posicion_menor]

        for posicion_buscar in range(posicion_actual, tamano_de_lista - 1):
            nombre_buscar = lista[posicion_buscar + 1]

            # Comparar en minúsculas para que no distinga entre mayúsculas y minúsculas
            if nombre_menor.lower() > nombre_buscar.lower():
                nombre_menor = nombre_buscar
                posicion_menor = posicion_buscar + 1

        if posicion_menor != posicion_actual:
            lista[posicion_menor], lista[posicion_actual] = lista[posicion_actual], lista[posicion_menor]

    return lista

def main():
    print("Introduce los nombres separados por comas:")
    print("Ejemplo: Ana,Emma,raul,alejandro,comas,Analise,Luis,Lucy,marco")
    nombres = input().split(",")  
    nombreslower = [nombre.strip() for nombre in nombres] 
    nombresort = ordenar(nombreslower)  
    nombres_str = ', '.join(nombresort)
    print(nombres_str)


# Llamada a la función main
if __name__ == "__main__":
    main()
