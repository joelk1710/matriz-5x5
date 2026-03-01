matriz = [[0 for i in range(5)]for j in range(5)]
for i in range (5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posicion [{i},{j}]:"))
        matriz[i][j] = valor

print("\nMATRIZ INGRESADA:")
for i in range(5):
        for j in range(5):
            print(matriz[i][j],end="\t")
        print()