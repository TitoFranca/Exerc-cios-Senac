# 2. Construa o fluxo de dados e, em seguida, o algoritmo que leia o dia da semana informado e apresente a 
# mensagem “Casa” para os sábados e os domingos e “Trabalho” para demais outros dias. Considere que os dias
# da semana são definidos: “Segunda”, “Terca”, “Quarta”, “Quinta”, “Sexta”, “Sábado” e “Domingo”.

### Forma 1

# dia_semana = input("Escreva um dia da semana: ")
# if dia_semana == "Sabado" or dia_semana == "Domingo": 
#     local = "Casa"
# else:
#     local = "Trabalho"
# print(f"Neste dia da semana você estará aqui: {local}")

dia_semana = input("Escreva um dia da semana: ")
lista_fds = ["Sábado", "Sabado", "sabado", "sábado", "domingo","Domingo"]
if dia_semana in lista_fds:
    local = "Casa"
else:
    local = "Trabalho"
print("="*40)
print( f"Nesse dia da semana você estará aqui: {local}")
print("="*40)