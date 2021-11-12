def divisors(num):
    divisors = []
    for i in range(1, num + 1):
    # if num % i == 1:
        if num % i == 0:
            divisors.append(i)
    return divisors




def run():
        num = input("Ingresa un número: ")
        #assert num.isnumeric() & 
        assert num.isnumeric() > 0, "Debes ingresar un numero y que sea mayor a 0"
        #assert num.isnumeric() > 0, "Ingresa un numero positivo"
        print(divisors(int(num)))
        print("Program ends")



if __name__ == "__main__":
    run()