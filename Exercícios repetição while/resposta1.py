while True:
    login1 = input("Qual seu login? ")
    senha1 = input("Qual sua senha? ")
    if login1 != senha1:
        while True:
            login2 = input("Qual o login da pessoa 2? ")
            senha2 = input("Qual sua senha? ")

            if login2 != senha2 and login1 != login2:
                break
            else:
                print("Login e senha iguais ou o login é o mesmo da 1ª pessoa\n")
        break
    else:
        print("Login e senha iguais\n")
