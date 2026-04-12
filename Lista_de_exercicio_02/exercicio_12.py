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
    
# print(pensionistas)

homem_solteiro_menor_idade = 0
mulher_solteira_menor_21 = 0

nomes_pensionistas = pensionistas.keys()
for nome in nomes_pensionistas:
    elemento = pensionistas.get(nome)
    # print(elemento) preferi que a saída não contivesse a lista

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
     

        
        



# praias = {} # dicionário é chaves
# continua = 0 # O zeroserve para iniciar o comando

# while continua == 0: #o zero servepara iniciar o comando. Para iniciar deverá ser o mesmo que foi atribuido a variável.
#     # receber informações da praia#
#     nome_praia = input ("Informe o nome da praia: ")
#     distancia_centro = float(input("Informe a distância da praia ao centro da cidade: "))
#     media_veranistas = float(input("Informe número de veranistas que vão à praia: "))
#     tipo_acesso = float(input("Informe o tipo de acesso à praia (0 - acesso não asfaltado; 1- acesso asfaltado): "))

#      #Inserindo no dicionário as informações do dicionário
#     praias[nome_praia] = [distancia_centro, media_veranistas,tipo_acesso] #Chave nome_praia

#     continua = int(input("Deseja cadastrar nova praia? (0 - Sim / Qualquer outro número - Não)"))
# """ print(praias) """


# #processamento
# numero_praias_15km = 0
# numero_veranistas_praia_nao_asfaltada = 0
# quantidade_numero_de_praias_acesso_nao_asfaltado = 0
# media_veranistas = 0
# praias_acesso_asfaltado_menos_10000_veranistas = {}

# nomes_praia = praias.keys()
# for nome in nomes_praia:
#     elemento = praias.get(nome)
#     print(elemento)

#     distancia_centro = elemento [0]
#     numero_veranistas = elemento [1]
#     tipo_acesso = elemento [2]

#     if distancia_centro > 15:
#         numero_praias_15km = numero_praias_15km +1

#     if tipo_acesso == 0:
#         numero_veranistas_praia_nao_asfaltada = numero_veranistas_praia_nao_asfaltada + numero_veranistas
#         quantidade_numero_de_praias_acesso_nao_asfaltado = quantidade_numero_de_praias_acesso_nao_asfaltado +1

#     if tipo_acesso == 1 and numero_veranistas <1000:
#         praias_acesso_asfaltado_menos_10000_veranistas [nome] = distancia_centro

# if quantidade_numero_de_praias_acesso_nao_asfaltado >0:
#     media_veranistas = numero_veranistas_praia_nao_asfaltada / quantidade_numero_de_praias_acesso_nao_asfaltado

# print(f" Número de praias mais de 15 km do centro: {numero_praias_15km}")
# print(f" Média de veraistas de praias com acesso não asfaltado: {media_veranistas}")    
# print(f" Praia com acesso asfaltado e com menos de 1000 veranistas: {praias_acesso_asfaltado_menos_10000_veranistas}")