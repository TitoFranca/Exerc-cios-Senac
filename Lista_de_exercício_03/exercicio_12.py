""""
Considere que uma pesquisa de opinião na cidade de Florianópolis solicitou de cada entrevistado as informações a seguir:
Entre os clubes a seguir, qual o de sua preferência?
a) Figueirense
b) Marcílio Dias
c) Outros clubes
Qual o valor de seu salário?
Qual o local de nascimento?
a) Florianópolis
b) Outras cidades
Construa um algoritmo que, considerando as fornecidas, determine e mostre:
a) Número de torcedores por clube;
b) Média salarial da torcida do Figueirense;
c) Número de pessoas nascidas em Florianópolis e que torcem pelo Marcílio Dias;
d) Número de pessoas nascidas em outras cidades e que torcem pelo Figueirense.
"""
print("-"*40)
print("PESQUISA FLORIPA")
print("-"*40)

entrevistados = []
continua = "S"

while continua == "S": #só funciona com "S" maiúsculo. Tentei usar "S" or "s" mas não funcionou. Triste :(
    clube_preferido = input("Informe seu clube preferido:\na) Figueirense\nb) Marcílio Dias\nc) Outro\n")
    salario = float(input("Qual o valor de seu salário? "))
    local_nascimento = input("Informe o local de seu nascimento:\na)Florianópolis\nb)Outra cidade\n ")
    
    entrevistados.append([clube_preferido,salario, local_nascimento])
    continua = input("Deseja inserir novo dado? [S] Sim ou [N] Não ")

torcedores_figueirense = 0
torcedores_marcilio_dias = 0
torcedores_outros = 0
salario_figueirense = 0
torcedores_marcilio_dias_florianopolis = 0
torcedores_figueirense_outras_cidades = 0

for torcedores in entrevistados:
    clube_preferido = torcedores [0]
    salario = torcedores [1]
    local_nascimento = torcedores [2]

    if clube_preferido == "a":
        torcedores_figueirense = torcedores_figueirense + 1
        salario_figueirense = salario_figueirense + salario
        if local_nascimento == "b":
            torcedores_figueirense_outras_cidades = torcedores_figueirense_outras_cidades +1
    
    elif torcedores == "b":
        torcedores_marcilio_dias = torcedores_marcilio_dias + 1
        if local_nascimento == "a":
            torcedores_marcilio_dias_florianopolis = torcedores_marcilio_dias_florianopolis +1
    
    else:
        torcedores_outros = torcedores_outros + 1
media_salaria_figueirense = 0
if torcedores_figueirense>0:
    media_salaria_figueirense = salario_figueirense / torcedores_figueirense
    
print("="*40)
print(f"Quantidade de Torcedores Figueirense: {torcedores_figueirense} ")
print(f"Quantidade de Torcedores Marcílio Dias: {torcedores_marcilio_dias} ")
print(f"Quantidade de Torcedores Outros Times: {torcedores_outros} ")
print(f"Média Salaria dos Torcedores do Figueirense: R$ {media_salaria_figueirense:.2f}")
print(f"Torcedores do Marcílcio Dias que nasceram em Florianópolis: {torcedores_marcilio_dias_florianopolis}")
print(f"Torcedores do Figueirense que são de fora de Florianópolis: {torcedores_figueirense_outras_cidades}")
print("="*40)
