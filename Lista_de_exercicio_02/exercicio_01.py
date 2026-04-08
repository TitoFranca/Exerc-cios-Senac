# Escreva o comando de seleção para cada uma das situações a seguir:
# a) Se X for maior que Y ou se Z for menor ou igual a 30, multiplique X por 2. Caso contrário, divida X por 2 e divida Z por 5;
# b) Se o desconto for menor que 25% e o preço do produto maior que R$25.000,00, apresentar o nome do produto.

x = float(input("Digite número x: "))
y = float(input("Digite número y: "))
z = float(input("Digite número z: "))

if x > y or z <= 30:
    x = x*2

else:
    x = x/2
    z = z/5
print(f"o resultado de x é {x:.2f}")
print(f"O resultado de z é {z:.2f}")        
    