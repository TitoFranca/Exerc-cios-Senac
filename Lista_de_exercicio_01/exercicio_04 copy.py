print("-------- Cálculo de Bhaskara --------")
print()
a = int(input("Insira o vaor de a:\n"))
b = int(input("Insira o valor de b:\n"))
c = int(input("Insira o valor de c:\n"))
delta = ((b ** 2) - (4*a*c))
if delta <0:
    print("Com esses números o valor de Delta é negativo. Escolha outros.")
else:
    x1 = ((-b) + (delta)**0.5)/2*a
    x2 = ((-b) - (delta)**0.5)/2*a
    numeros = [a,b,c]
    maior = max(numeros)
    soma_outros = sum(numeros) - maior
if maior > soma_outros:
    print("="*40)
    print("\nEscolha outros números. Triângulo não representa condição de existência válida!\n")
    print("="*40)
else: 
    print(f" Valor de Delta será {delta}\n")
    print(f" Valor de X1 será {x1:.2f}\n")
    print(f" Valor de X2 será {x2:.2f}\n")
    
    

