A = 0
B = 0
i = 0

n = int(input("Informe a quantidade de vezes que irá apertar o interruptor: "))

if n >= 2 or n <= 10 ** 5:
    while i < n:
        num = int(input("Informe qual interruptor apertou agora (1 ou 2): "))

        if num == 1:
            if A == 0:
                A = 1
            elif  A == 1:
                A = 0
            i += 1
        elif num == 2:
            if  A == 0 and B == 0:
                A = 1
                B = 1
            elif A == 1 and B == 1:
                A = 0
                B = 0
            elif A == 0 and B == 1:
                A = 1
                B = 0
            elif A == 1 and B == 0:
                A = 0
                B = 1 
            i += 1
        else:
            print("Número incorreto, digite novamente!")

    print(f"Lâmpada A = {A} \nLâmpada B = {B}")
else:
    print("Quantidade não aceita. Digite outro número!")