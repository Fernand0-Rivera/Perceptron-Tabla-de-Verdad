import random
from tabulate import tabulate

# Función de activación
def activacion(suma_ponderada):
    if suma_ponderada > 0:
        return 1
    else:
        return -1

# Función para calcular la salida
def calcular_salida(x1, x2):
    suma_ponderada = w1 * x1 + w2 * x2 + umbral
    return activacion(suma_ponderada)

# Función para calcular la paridad de 4 bits
def calcular_paridad(bits):
    paridad = sum(bits) % 2
    return -1 if paridad == 0 else 1

# Función para entrenar el perceptrón
def entrenar_perceptron(conjunto_entrenamiento, opc):
    # Inicialización de los pesos y el umbral de manera aleatoria
    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)
    umbral = random.uniform(-1, 1)
    w3 = w4 = 0  # Inicializar w3 y w4 en caso de que se necesiten

    # Si la opción es 4 (paridad de 4 bits), necesitamos inicializar w3 y w4
    if opc == "4":
        w3 = random.uniform(-1, 1)
        w4 = random.uniform(-1, 1)
    elif opc == "5":
        w3 = random.uniform(-1, 1)
    # Entrenamiento del perceptrón
    num_iteraciones = 0
    while True:
        num_iteraciones += 1
        error_total = 0
        tabla = []
        for entrada, salida_deseada in conjunto_entrenamiento:
            x0, x1, x2 = 1, entrada[0], entrada[1]  # x0 siempre es 1
            if opc == "4":
                x3, x4 = entrada[2], entrada[3]
            elif opc == "5":
                x3 = entrada[2]
            else:
                x3 = x4 = 0  # Si no es la opción 4, establecer x3 y x4 en 0
            suma_ponderada = w1 * x1 + w2 * x2 + umbral * x0
            salida_obtenida = activacion(suma_ponderada)
            error = salida_deseada - salida_obtenida
            error_total += abs(error)
            # Actualización de los pesos y el umbral si es necesario
            if error != 0:
                w1 += error * x1
                w2 += error * x2
                umbral += error * x0
            clasificacion_correcta = "Sí" if salida_obtenida == salida_deseada else "No"
            # Agregar las variables correctas a la tabla según la opción
            if opc == "4":
                tabla.append([x1, x2, x3, x4, suma_ponderada, "Sí" if suma_ponderada > 0 else "No", salida_obtenida, salida_deseada, clasificacion_correcta])
            elif opc == "5":
                tabla.append([x1, x2, x3, suma_ponderada, "Sí" if suma_ponderada > 0 else "No", salida_obtenida, salida_deseada, clasificacion_correcta])
            else:
                tabla.append([x1, x2, suma_ponderada, "Sí" if suma_ponderada > 0 else "No", salida_obtenida, salida_deseada, clasificacion_correcta])
        print("\nIteración:", num_iteraciones)
        headers = ["x1", "x2"]
        if opc == "4":
            headers.extend(["x3", "x4"])  # Agregar x3 y x4 a los encabezados si es la opción 4
        elif opc == "5":
            headers.append("x3")  # Agregar x3 a los encabezados si es la opción 5
        headers.extend(["Suma ponderada", "Suma > 0", "Salida", "Salida deseada", "Clasificación correcta"])
        print(tabulate(tabla, headers=headers))
        if error_total == 0 or num_iteraciones >= 10:
            break

    # Resultados finales
    print("\nPesos finales:", w1, w2)
    print("Umbral final:", umbral)
    print("Número de iteraciones:", num_iteraciones)

# Menú principal
while True:
    print("\nSeleccione una opción:")
    print("1. Función lógica AND")
    print("2. Función lógica OR")
    print("3. Función lógica XOR")
    print("4. Paridad de 4 bits")
    print("5. Mayoría simple")
    print("6. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        print("\nFunción lógica AND:")
        conjunto_entrenamiento_and = [((-1, -1), -1), ((-1, 1), -1), ((1, -1), -1), ((1, 1), 1)]
        entrenar_perceptron(conjunto_entrenamiento_and, opcion)
    elif opcion == "2":
        print("\nFunción lógica OR:")
        conjunto_entrenamiento_or = [((-1, -1), -1), ((-1, 1), 1), ((1, -1), 1), ((1, 1), 1)]
        entrenar_perceptron(conjunto_entrenamiento_or, opcion)
    elif opcion == "3":
        print("\nFunción lógica XOR:")
        conjunto_entrenamiento_xor = [((-1, -1), -1), ((-1, 1), 1), ((1, -1), 1), ((1, 1), -1)]
        entrenar_perceptron(conjunto_entrenamiento_xor, opcion)
    elif opcion == "4":
        print("\nParidad de 4 bits:")
        conjunto_entrenamiento_paridad = [((-1, -1, -1, -1), 1),
                                          ((-1, -1, -1, 1), -1),
                                          ((-1, -1, 1, -1), -1),
                                          ((-1, -1, 1, 1), 1),
                                          ((-1, 1, -1, -1), -1),
                                          ((-1, 1, -1, 1), 1),
                                          ((-1, 1, 1, -1), 1),
                                          ((-1, 1, 1, 1), -1),
                                          ((1, -1, -1, -1), -1),
                                          ((1, -1, -1, 1), 1),
                                          ((1, -1, 1, -1), 1),
                                          ((1, -1, 1, 1), -1),
                                          ((1, 1, -1, -1), 1),
                                          ((1, 1, -1, 1), -1),
                                          ((1, 1, 1, -1), -1),
                                          ((1, 1, 1, 1), 1),
                                          ]
        entrenar_perceptron(conjunto_entrenamiento_paridad, opcion)
    elif opcion == "5":
        print("\nFunción Mayoría-Simple (3 entradas):")
        conjunto_entrenamiento_mayoria = [((0, 0, 0), -1),
                                          ((0, 0, 1), -1),
                                          ((0, 1, 0), -1),
                                          ((0, 1, 1), 1),
                                          ((1, 0, 0), -1),
                                          ((1, 0, 1), 1),
                                          ((1, 1, 0), 1),
                                          ((1, 1, 1), 1)]
        entrenar_perceptron(conjunto_entrenamiento_mayoria, opcion)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
