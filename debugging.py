def divisors(num):
    divisors = []
    for i in range(1, num + 1):
    # if num % i == 1:
        if num % i == 0:
            divisors.append(i)
    return divisors




def run():
    try:
        num = int(input("Ingresa un número: "))
        if (num < 0):
            raise ValueError(str(num) + " --> Ingresa un numero positivo")
        print(divisors(num))
        print("Program ends")
    except ValueError as re:
        print(re)



if __name__ == "__main__":
    run()