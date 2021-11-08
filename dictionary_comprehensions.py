def run():
    # my_dict = {}
    rango = 1000 + 1
    # for i in range(rango):
    #     my_dict[i] = i ** 3
    # print(my_dict)

    # for i in range(rango):
    #     if (i % 3 != 0):
    #         my_dict[i] == i ** 3

    # print(" ")
    # print(" ")
    # print("Dictionary comprehensions")
    # print(" ")
    # my_dict = {i: i ** 3 for i in range(rango) if (i % 3 != 0)}
    # print(" " + str(my_dict))
    print(" ")
    print(" ")
    print("Reto")
    reto = {i: i ** 0.5 for i in range(rango) if (i < rango)}
    print(" " + str(reto))

if __name__ == "__main__":
    run()