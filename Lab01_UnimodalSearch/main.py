import random
import time


#  Algoritmo de Búsqueda Lineal (O(n))
def encontrar_pico_lineal(array):
    if not array:
        return None
    pico_actual = array[0]
    for elemento in array:
        if elemento > pico_actual:
            pico_actual = elemento
    return pico_actual


# Algoritmo de Búsqueda Logarítmica (O(log n))
def encontrar_pico_logaritmico(array, bajo, alto):
    """
    Encuentra el pico de un array unimodal en O(log n) dividiendo y venceiendo.
    """
    if bajo == alto:
        return array[bajo]

    # Manejamos el caso de 2 elementos
    if alto == bajo + 1:
        return max(array[bajo], array[alto])

    medio = (bajo + alto) // 2

    # El pico está en el medio
    if array[medio] > array[medio - 1] and array[medio] > array[medio + 1]:
        return array[medio]

    # El pico está en la parte creciente del array (a la derecha)
    if array[medio] > array[medio - 1] and array[medio] < array[medio + 1]:
        return encontrar_pico_logaritmico(array, medio + 1, alto)

    # El pico está en la parte decreciente del array (a la izquierda)
    return encontrar_pico_logaritmico(array, bajo, medio - 1)


#  Generador de Array Unimodal
#  Un array unimodal es aquel que, tras un posible pre-ordenamiento,
#  presenta una secuencia ascendente seguida de una secuencia descendente
def generar_array_unimodal_aleatorio(tamano):
    if tamano < 1:
        return []
    punto_pico = random.randint(0, tamano - 1)
    parte_creciente = sorted(random.sample(range(1, tamano * 2), punto_pico + 1))

    pico_valor = parte_creciente[-1]

    parte_decreciente = []
    if punto_pico < tamano - 1:
        elementos_decrecientes = sorted(random.sample(range(1, pico_valor), tamano - 1 - punto_pico), reverse=True)
        parte_decreciente = elementos_decrecientes

    array_generado = parte_creciente + parte_decreciente
    return array_generado


#  Función para ejecutar y medir un algoritmo
def ejecutar_algoritmo(algoritmo_func, array):
    start_time = time.time()
    if algoritmo_func.__name__ == 'encontrar_pico_logaritmico':
        pico = algoritmo_func(array, 0, len(array) - 1)
    else:
        pico = algoritmo_func(array)
    end_time = time.time()
    tiempo_ejecucion = (end_time - start_time) * 1000  # En milisegundos
    return pico, tiempo_ejecucion


#  menú
def menu():
    while True:
        print("-------------------------------------------------")
        print("  Laboratorio 1: Análisis de Algoritmos Unimodales")
        print("-------------------------------------------------")
        print("Seleccione una opción:")
        print("1. Probar Algoritmo Lineal (O(n))")
        print("2. Probar Algoritmo Logarítmico (O(log n))")
        print("3. Comparar ambos algoritmos")
        print("4. Salir")

        opcion = input("Ingrese su elección (1-4): ")

        if opcion == '4':
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        try:
            tamano_array = int(input("Ingrese el tamaño del array a generar: "))
            if tamano_array <= 0:
                print("Por favor, ingrese un tamaño mayor que 0.")
                continue

            mi_array = generar_array_unimodal_aleatorio(tamano_array)

            if opcion == '1':
                print(f"\n--- Probando Algoritmo Lineal con un array de tamaño {tamano_array} ---")
                pico, tiempo = ejecutar_algoritmo(encontrar_pico_lineal, mi_array)
                print(f"Pico encontrado: {pico}")
                print(f"Tiempo de ejecución: {tiempo:.6f} ms")

            elif opcion == '2':
                print(f"\n--- Probando Algoritmo Logarítmico con un array de tamaño {tamano_array} ---")
                pico, tiempo = ejecutar_algoritmo(encontrar_pico_logaritmico, mi_array)
                print(f"Pico encontrado: {pico}")
                print(f"Tiempo de ejecución: {tiempo:.6f} ms")

            elif opcion == '3':
                print(f"\n--- Comparando Algoritmos con un array de tamaño {tamano_array} ---")

                # Ejecutar y medir el algoritmo lineal
                pico_lineal, tiempo_lineal = ejecutar_algoritmo(encontrar_pico_lineal, mi_array)
                print(f"\nAlgoritmo Lineal (O(n)):")
                print(f"  Pico encontrado: {pico_lineal}")
                print(f"  Tiempo de ejecución: {tiempo_lineal:.6f} ms")

                # Ejecutar y medir el algoritmo logarítmico
                pico_log, tiempo_log = ejecutar_algoritmo(encontrar_pico_logaritmico, mi_array)
                print(f"\nAlgoritmo Logarítmico (O(log n)):")
                print(f"  Pico encontrado: {pico_log}")
                print(f"  Tiempo de ejecución: {tiempo_log:.6f} ms")

                print("\n--- Conclusión de la comparación ---")
                if tiempo_lineal > tiempo_log:
                    print(f"El algoritmo logarítmico fue {tiempo_lineal / tiempo_log:.2f} veces más rápido.")
                else:
                    print("El algoritmo lineal fue más rápido (esto es común con arrays muy pequeños).")

            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

        except ValueError:
            print("\nEntrada no válida. Por favor, ingrese un número entero.")


if __name__ == "__main__":
    menu()