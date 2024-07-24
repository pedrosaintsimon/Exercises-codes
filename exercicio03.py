# 3
print("Exercício 03 - Calcule o seu produto com desconto aplicado")
print(" ")
preco_produto = input('Quanto custa o seu produto? ')
desconto = input("Quanto o valor do desconto (em %)? ")

# Converter entradas para float
preco_produto_float = float(preco_produto)
desconto_float = float(desconto)

# Calcular valor do desconto
desconto_decimal = desconto_float / 100
valor_desconto = preco_produto_float * desconto_decimal

# Calcular preço final
preco_final = preco_produto_float - valor_desconto

# Exibir resultado
print(f"O preço final com desconto é: R${preco_final:.2f}")
