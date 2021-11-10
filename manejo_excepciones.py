def run():
    # try, except----------------

    # def palindrome(string):
    #     if (string == string[::-1]):
    #         print("Es palindromo")
    #     else:
    #         print("No es palindromo")
    # try:
    #     palindrome(1)
    # except TypeError:
    #     print("Solo se pueden ingresar string")

    # raise-----------------------
    def palindrome(string):
        try:
            if len(string) == 0:
                raise ValueError("No se puede ingresar una cadena vacia")
            return string == string[::-1]
        except ValueError as ve:
            print(ve)
            return False
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")

    
    # finally
    try:
        f = open("archivo.txt")
            # hacer cualquier cosa con nuestro archivo
    finally:
        f.close()



if __name__ == "__main__":
    run()