import random

def generar_laberinto(n):
    # Inicializamos el laberinto como una lista vacía
    laberinto = []
    # Crear bordes de asteriscos
    for i in range(n):
        fila = []
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                fila.append('*')
            else:
                fila.append(' ')
        laberinto.append(fila)

    # Rellenar el interior del laberinto con paredes conectadas
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if random.random() < 0.5:  # 50% de probabilidad de ser pared
                laberinto[i][j] = '*'

    return laberinto


def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(''.join(fila))


def encontrar_rutas(laberinto, x, y, salida_x, salida_y, ruta_actual, rutas):
    #Salida o entrada se salen del laberinto
    if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
        return
    if laberinto[x][y] == '*' or laberinto[x][y] == '1':
        return
    if x == salida_x and y == salida_y:
        rutas.append(ruta_actual.copy())
        return

    laberinto[x][y] = '1'  # Marcar como visitado
    ruta_actual.append((x, y))

    # Moverse en las 4 direcciones posibles
    encontrar_rutas(laberinto, x + 1, y, salida_x, salida_y, ruta_actual, rutas)
    encontrar_rutas(laberinto, x - 1, y, salida_x, salida_y, ruta_actual, rutas)
    encontrar_rutas(laberinto, x, y + 1, salida_x, salida_y, ruta_actual, rutas)
    encontrar_rutas(laberinto, x, y - 1, salida_x, salida_y, ruta_actual, rutas)

    laberinto[x][y] = ' '  # Desmarcar
    ruta_actual.pop()


def marcar_ruta(laberinto, ruta, numero_ruta):
    # Copiar el laberinto para no modificar el original
    laberinto_copia = []
    for fila in laberinto:
        nueva_fila = fila.copy()  # Copiar cada fila
        laberinto_copia.append(nueva_fila)

    # Marcar la ruta en el laberinto copiado
    for x, y in ruta:
        laberinto_copia[x][y] = str(numero_ruta)

    return laberinto_copia

def solicitar_tamano_laberinto():
    while True:
        n = int(input("Ingrese el tamaño del laberinto: "))
        if n > 0:
            return n
        print("Tamaño de laberinto inválido. Intente nuevamente.")


def solicitar_coordenadas(n, mensaje):
    while True:
        try:
            x, y = map(int, input(mensaje).split())
            if 0 <= x < n and 0 <= y < n:
                return x, y
            else:
                print(f"Coordenadas inválidas. Asegúrate de que estén dentro del rango [0, {n-1}].")
        except ValueError:
            print("Entrada inválida. Ingresa dos números separados por un espacio.")


def main():
    #Laberinto para Testing
    #laberinto = [
    #    ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
    #    ['*', ' ', '*', 'P', ' ', ' ', '*', ' ', '*'],
    #    ['*', ' ', '*', '*', '*', ' ', '*', ' ', 'S'],
    #    ['*', ' ', ' ', ' ', '*', ' ', '*', ' ', '*'],
    #    ['*', '*', '*', ' ', '*', ' ', ' ', ' ', '*'],
    #    ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*'],
    #    ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*'],
    #    ['*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
    #    ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    #]
    #entrada_x, entrada_y = 1, 3  # Coordenadas de 'P'
    #salida_x, salida_y = 2, 8  # Coordenadas de 'S'

    ## Solicitar tamaño del laberinto
    n = solicitar_tamano_laberinto()
    laberinto = generar_laberinto(n)

    # Solicitar coordenadas de entrada y salida
    print("\nCoordenadas de entrada:")
    entrada_x, entrada_y = solicitar_coordenadas(n, "Ingrese las coordenadas de entrada (x y): ")
    print("\nCoordenadas de salida:")
    salida_x, salida_y = solicitar_coordenadas(n, "Ingrese las coordenadas de salida (x y): ")

    laberinto[entrada_x][entrada_y] = 'P'
    laberinto[salida_x][salida_y] = 'S'

    print("Laberinto inicial:")
    imprimir_laberinto(laberinto)

    rutas = []
    encontrar_rutas(laberinto, entrada_x, entrada_y, salida_x, salida_y, [], rutas)

    if not rutas:
        print("No hay rutas posibles.")
    else:
        print(f"Se encontraron {len(rutas)} rutas posibles.")
        for i, ruta in enumerate(rutas):
            print(f"\nRuta {i + 1}:")
            laberinto_ruta = marcar_ruta(laberinto, ruta, i + 1)
            imprimir_laberinto(laberinto_ruta)


if __name__ == "__main__":
    main()