max_value = 120 #determinar com variável para mudar apenas o valor da variável

for i in range(max_value +1): #utilizar o +1 para utilizar o número da variável
    if i  % 3 == 0 and i % 4 == 0: # i % 12 == 0 faz o mesmo resultado
        print(f"{i} é divisível por 3 e por 4")
    