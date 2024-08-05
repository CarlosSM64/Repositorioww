def main():
    
    cantidad_temperaturas = int(input("Ingresar Temperatura: "))

    temperaturas = []

    for i in range(cantidad_temperaturas):
        temperatura = float(input(f"Ingresa la temperatura {i+1}: "))
        temperaturas.append(temperatura)

    if cantidad_temperaturas > 0:
        media = sum(temperaturas) / cantidad_temperaturas
        print(f"La media de las temperaturas es: {media:.2f}")

        conteo_superiores_o_iguales = sum(1 for temp in temperaturas if temp >= media)
        print(f"Cantidad de temperaturas superiores o iguales a la media: {conteo_superiores_o_iguales}")
    else:
        print("No se ingresaron temperaturas.")

if __name__ == "__main__":
    main()