def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Luis",
        "lastname": "Santamaria"
    }

    super_list = [
        {"firstname": "Luis", "lastname": "Santamaria"},
        {"firstname": "Andres", "lastname": "Ramirez"},
        {"firstname": "Pepe", "lastname": "Torres"},
        {"firstname": "Susana", "lastname": "Rodelo"},
        {"firstname": "Jose", "lastname": "Martinez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, " ", value)

    for i in super_list:
        for key, values in i.items():
            print(key, "-", values)



if __name__ == "__main__":
    main()