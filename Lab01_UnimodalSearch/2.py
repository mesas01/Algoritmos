import random
import time
import matplotlib.pyplot as plt


def encontrar_pico_lineal(array):
    """
    Encuentra el elemento máximo (pico) en un array unimodal
    utilizando una búsqueda lineal. Complejidad O(n).

    Args:
        array: Una lista de números.

    Returns:
        El valor del pico del array.
    """
    if not array:
        return None
    pico_actual = array[0]
    for elemento in array:
        if elemento > pico_actual:
            pico_actual = elemento
    return pico_actual


def encontrar_pico_logaritmico(array, bajo, alto):
    """
    Encuentra el pico de un array unimodal en O(log n) utilizando
    una estrategia de divide y vencerás.

    Args:
        array: Una lista de números unimodal.
        bajo: El índice inicial del sub-array.
        alto: El índice final del sub-array.

    Returns:
        El valor del pico del array.
    """
    if bajo == alto:
        return array[bajo]

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


def generar_array_unimodal_aleatorio(tamano):
    """
    Genera un array unimodal de un tamaño dado.

    Args:
        tamano: El número de elementos en el array.

    Returns:
        Una lista de números que es unimodal.
    """
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


def ejecutar_simulacion():
    """
    Función principal para ejecutar la simulación, medir los tiempos
    y generar la gráfica comparativa.
    """
    # Tamaños de los arrays para la simulación, aumentando en órdenes de magnitud.
    tamanos_array = [10, 100, 1000, 10000, 100000, 1000000,10000000, 100000000]
    tiempos_lineal = []
    tiempos_logaritmico = []

    print("Iniciando simulación de tiempos...")

    for tamano in tamanos_array:
        print(f"Probando con un array de tamaño {tamano}...")

        # Generar un array unimodal para la prueba
        mi_array = generar_array_unimodal_aleatorio(tamano)

        # --- Medir el tiempo del algoritmo lineal ---
        start_time_lineal = time.time()
        encontrar_pico_lineal(mi_array)
        end_time_lineal = time.time()
        tiempo_ejecucion_lineal = (end_time_lineal - start_time_lineal) * 1000  # En milisegundos
        tiempos_lineal.append(tiempo_ejecucion_lineal)

        # --- Medir el tiempo del algoritmo logarítmico ---
        start_time_log = time.time()
        encontrar_pico_logaritmico(mi_array, 0, len(mi_array) - 1)
        end_time_log = time.time()
        tiempo_ejecucion_log = (end_time_log - start_time_log) * 1000  # En milisegundos
        tiempos_logaritmico.append(tiempo_ejecucion_log)

    print("Simulación completada. Generando gráfica...")

    # --- Generar la gráfica ---
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos_array, tiempos_lineal, label='Algoritmo Lineal (O(n))', marker='o', color='red')
    plt.plot(tamanos_array, tiempos_logaritmico, label='Algoritmo Logarítmico (O(log n))', marker='o', color='blue')

    plt.xscale('log')
    plt.title('Comparación de Tiempos de Ejecución de Algoritmos Unimodales')
    plt.xlabel('Tamaño del Array (escala logarítmica)')
    plt.ylabel('Tiempo de Ejecución (milisegundos)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    ejecutar_simulacion()
