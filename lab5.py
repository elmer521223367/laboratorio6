import matplotlib.pyplot as plt

def obtener_cantidad_numeros():
    while True:
        try:
            num_count = int(input("Ingrese la cantidad de números que necesita sumar (debe ser entero positivo): "))
            if num_count > 0:
                return num_count
            else:
                print("Ingrese un entero positivo.")
        except ValueError:
            print("Ingrese un entero positivo válido.")

def obtener_numeros(num_count):
    numbers = []
    for i in range(num_count):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Ingrese un entero positivo válido.")
    return numbers

def calcular_suma_acumulativa(numbers):
    cumulative_sums = [sum(numbers[:i+1]) for i in range(len(numbers))]
    return cumulative_sums

def mostrar_suma_acumulativa(cumulative_sums):
    print("Suma acumulativa:")
    for i, sum in enumerate(cumulative_sums):
        print(f"Número {i+1}: {sum}")

def crear_grafico_barras(cumulative_sums):
    plt.bar(range(1, len(cumulative_sums) + 1), cumulative_sums)
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Suma Acumulativa")
    plt.show()

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")
    
    num_count = obtener_cantidad_numeros()
    numbers = obtener_numeros(num_count)
    cumulative_sums = calcular_suma_acumulativa(numbers)
    
    mostrar_suma_acumulativa(cumulative_sums)
    crear_grafico_barras(cumulative_sums)

if __name__ == "__main__":
    main()
