def main():
    exponente = 2
    num_limite = 10 + 1
    lista = []
    for num in range(num_limite):
        if (num < num_limite):
            lista.append(num ** exponente)
    print(" ")
    print("Lista de numeros naturales del 1 al 100 al cuadrado")
    print("    " + str(lista))
    print(" ")
    print(" ")
    print("Lista de numeros naturales del 1 al 100 al cuadrado exceptuando multiplos de 3")
    for num in range(num_limite):
        if (num < num_limite):
            if(num % 3 != 0):
                lista.append(num ** exponente)
    print("    " + str(lista))
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("LIST COMPREHENSION------------------")
    print(" ")
    reto = [i for i in range(1, 100000) if i % 36 == 0]
    print("Lista con Comprehension de todos los numeros multiplos de 4 que a la vez son multiplos de 6 y 9, hasta de 5 digitos")
    print(" ")
    print("    " + str(reto))



if __name__ == "__main__":
    main()