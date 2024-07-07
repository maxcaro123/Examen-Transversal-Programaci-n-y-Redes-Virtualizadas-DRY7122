# 1_MedirDistanciaChileArgentina.py

import random

def calcular_distancia(ciudad_origen, ciudad_destino):
    # Simular cálculo de distancia
    distancia_millas = random.randint(500, 2000)
    distancia_kms = distancia_millas * 1.60934
    duracion_horas = distancia_kms / random.randint(60, 100)

    return distancia_millas, distancia_kms, duracion_horas

def main():
    while True:
        print("\nBienvenido al calculador de distancia entre ciudades.")
        print("Por favor, ingrese la ciudad de origen en Chile y la ciudad de destino en Argentina en español.")
        ciudad_origen = input("Ciudad de Origen: ")
        ciudad_destino = input("Ciudad de Destino: ")

        distancia_millas, distancia_kms, duracion_horas = calcular_distancia(ciudad_origen, ciudad_destino)

        print(f"\nLa distancia entre {ciudad_origen} y {ciudad_destino} es:")
        print(f"- {distancia_millas} millas")
        print(f"- {distancia_kms:.2f} kilómetros")
        print(f"\nLa duración estimada del viaje es de aproximadamente {duracion_horas:.2f} horas.")

        # Simular narrativa del viaje
        narrativa = f"\nUsted está viajando desde {ciudad_origen} hacia {ciudad_destino}. Disfrute del paisaje."
        print(narrativa)

        # Permitir elegir tipo de medio de transporte
        opcion = input("\n¿Qué tipo de medio de transporte desea utilizar? (Avión, Auto, Bus, Tren): ").lower()
        print(f"\nHa elegido viajar en {opcion}. ¡Buen viaje!")

        salir = input("\n¿Desea salir del programa? (s para salir, cualquier otra tecla para continuar): ").lower()
        if salir == 's':
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
