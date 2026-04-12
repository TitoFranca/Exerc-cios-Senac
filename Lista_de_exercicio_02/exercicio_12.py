""""
Faça um algoritmo que a partir da leitura do nome, sexo, estado civil,
idade, salário do pai ou cônjuge, escreva o nome da pessoa e a pensão a que tem direito. 
Para definir o cálculo da pensão corretamente, utilize as seguintes regras:
a) Caso seja homem, tem direito a 15% do salário do pai, se for solteiro e menor que 18 anos;
b) Caso seja mulher, tem direito a 20% do salário do pai, se for solteira e menor de 21 anos,
e 30% do salário do marido, se for casada;
c) Nos demais casos, a pensão é zero.
"""
print("-"*40)
print("SISTEMA DE CÁLCULO DE PENSIONISTAS")
print("-"*40)

pensionistas = {}
continua = "S"

while continua == "S":
    nome_pensionista = input("Informe o nome do(a) pensionista: ")
    sexo_pensionista = input("Informe o sexo: [M]asculino ou [F]eminino: ")
    ecivil_pensionista = input("Informe o estado civil:\n[S]olteiro(a)\n[C]asado(a)\n[D]ivorciado(a)\n[V]iúvo(a)\n[E]nrolado(a)\n")
    idade_pensionista = int(input("Informe a idade: "))
    valor_pensionista = float(input("Informe o valor da pensão: "))
    
    pensionistas[nome_pensionista] = [sexo_pensionista, ecivil_pensionista, idade_pensionista, valor_pensionista]
    continua = input("Deseja Cadastrar Novo Pensionista? [S] Sim ou [N] Não ")
    
# print(pensionistas) usado para testar

homem_solteiro_menor_idade = 0
mulher_solteira_menor_21 = 0

nomes_pensionistas = pensionistas.keys()
for nome in nomes_pensionistas:
    elemento = pensionistas.get(nome)
    # print(elemento) Fiquei na dúvida se era pra ter a lista na saída. Achei mais estético que não tivesse. Retirei. Não me repreove..rs

    sexo_pensionista = elemento [0]
    ecivil_pensionista = elemento [1]
    idade_pensionista = elemento [2]
    valor_pensionista = elemento [3]
    
    if sexo_pensionista == "M" and ecivil_pensionista == "S" and idade_pensionista <18:
        valor_pensao = valor_pensionista * 0.15
    
    elif sexo_pensionista == "F" and ecivil_pensionista == "S" and idade_pensionista <21:
        valor_pensao = valor_pensionista * 0.2
    
    elif sexo_pensionista == "F" and ecivil_pensionista == "C":
        valor_pensao = valor_pensionista * 0.3
    
    else:
        valor_pensao = "0,00  Vai ter que trablhar bebê. ahuhuaahuahhuahauhu"
    
    print(f"\n O valor da pensão de {nome} é de R$ {valor_pensao}")
