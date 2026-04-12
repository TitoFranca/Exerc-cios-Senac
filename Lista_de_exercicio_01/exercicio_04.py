print("-------- Cálculadora de Bhaskara para passar na Prova --------")
print()
a = int(input("Insira o vaor de a:\n"))
b = int(input("Insira o valor de b:\n"))
c = int(input("Insira o valor de c:\n"))
delta = ((b ** 2) - (4*a*c)) # Para que Bhaskara seja calculada, delta não pode ser nagativa
x1 = ((-b) + (delta)**0.5)/2*a
x2 = ((-b) - (delta)**0.5)/2*a
if delta <0:
    print("Com esses números o valor de Delta é negativo. Verifique!")
else:
    print(f" Valor de Delta será {delta}\n")
    print(f" Valor de X1 será {x1:.2f}\n")
    print(f" Valor de X2 será {x2:.2f}\n")
    
    

