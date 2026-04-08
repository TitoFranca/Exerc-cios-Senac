""" numero_01 = float(input("Digite número 1:\n"))
peso_numero_01 = int(input("Peso do Numéro 1:\n"))
numero_02 = float(input("Digite número 2:\n"))
peso_numero_02 = int(input("Peso do Número 2:\n"))
numero_03 = float(input("Digite número 3:\n"))
peso_numero_03 = int(input("Peso do Número 3:\n"))
numero_04 = float(input("Digite número 4:\n"))
peso_numero_04 = int(input("Peso do Número 4:\n"))
calculo_numeros = (numero_01 * peso_numero_01) + (numero_02 * peso_numero_02) + (numero_03 * peso_numero_03) + (numero_04 * peso_numero_04)
peso = (peso_numero_01 + peso_numero_02 + peso_numero_03 + peso_numero_04)
media_ponderada = calculo_numeros / peso
print("="*40)
print(f"A média ponderada é {media_ponderada}")
print("="*40) """
# Outra Forma de Fazer o mesmo exercício #
soma_produtos = 0
soma_pesos = 0
for i in range (1, 5):
    num = float(input(f"Digite o número {i}:\n"))
    peso = int(input(f"Digite o peso do número {i}:\n"))
    soma_produtos += (num * peso)
    soma_pesos += peso
media_ponderada = soma_produtos / soma_pesos

print("="*40)
print(f"A média ponderada é: {media_ponderada:.2f}")
print("="*40)