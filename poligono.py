def is_point_on_segment(px, py, x1, y1, x2, y2):
    """Verifica si el punto (px, py) está sobre el segmento definido por (x1, y1) y (x2, y2)."""
    # Verificar si el punto está dentro de los límites del segmento
    if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
        # Calcular la pendiente y verificar si coincide
        if (x2 - x1) == 0:  # Caso vertical
            return px == x1  # El punto debe estar en la línea vertical
        if (y2 - y1) == 0:  # Caso horizontal
            return py == y1  # El punto debe estar en la línea horizontal
        # Usar la fórmula de la pendiente para determinar si el punto está sobre el segmento
        return (py - y1) * (x2 - x1) == (y2 - y1) * (px - x1)  # Comprobar si son colineales
    
    return False

def ray_casting(point, polygon):
    x, y = point
    num_vertices = len(polygon)
    crossings = 0

    for i in range(num_vertices):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % num_vertices]
        
        # Comprobar si el punto está sobre el segmento
        if is_point_on_segment(x, y, x1, y1, x2, y2):
            return True  # El punto está sobre el borde del polígono
        
        # Comprobar si el punto está entre las alturas de los dos vértices
        if (y1 <= y < y2) or (y2 <= y < y1):
            # Calcular la intersección del segmento con la línea horizontal en y
            x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_intersect:  # Si el punto está a la izquierda de la intersección
                crossings += 1

    return crossings % 2 == 1  # True si es impar, es decir, dentro del polígono


def main():
    lineas = []
    print("Introduce las líneas (deja una línea en blanco para terminar):")
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    
    # Leer el número de vértices del polígono (n) y el número de puntos a evaluar (m)
    n, m = map(int, lineas[0].split())  
    lineas.remove(lineas[0])  # Eliminar la primera línea ya que la hemos procesado
    
    poligono = []
    puntos = []

    # Leer los vértices del polígono
    for i in range(n):
        xp, yp = map(int, lineas[i].split())
        poligono.append((xp, yp))

    # Leer los puntos a evaluar
    for i in range(m):
        x, y = map(int, lineas[n + i].split())
        puntos.append((x, y))

    # Evaluar cuántos puntos están dentro del polígono
    count = 0
    for punto in puntos:
        if ray_casting(punto, poligono):
            count += 1

    print("Número de puntos dentro del polígono:", count)


# Llamada a la función main
if __name__ == "__main__":
    main()
