(print("Cálculo de Desconto"))
(print("------------------------------------------"))
valor_produto = float(input("Escreva o valor do produto:\n"))
desconto = valor_produto * 0.10 
valor_c_desconto = valor_produto - desconto
(print("="*40))
(print(f"O Valor do desconto é: {desconto}"))
print(f"Valor do Produto com desconto é R$ {valor_c_desconto:.2f}")
(print("="*40))
