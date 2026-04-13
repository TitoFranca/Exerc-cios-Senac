print("-"*40)
print("CÁLCULO MUITO IMPORTANTE")
print("-"*40)

soma_positivos = 0
quantidade_negativos = 0
for i in range (50):  #Testei o range com 7. Funcionou.....Mas como o exercício pede 50
    valores = int(input("Digite um número: ")) # o exercício pede valores inteiros
    if valores > 0:
        soma_positivos = soma_positivos + valores
    else:
        quantidade_negativos = quantidade_negativos +1
print("="*30)
print(f"A soma dos valores positivos é {soma_positivos}")
print(f"A quantidade de números negativo é: {quantidade_negativos}")
print("="*30)
