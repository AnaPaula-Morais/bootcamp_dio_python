#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

valor_mercadoria = float(input("Qual o preço a mercadoria? "))
desconto = float(input("Qual o percentual de desconto? "))
valor_desconto = (desconto / 100) * 100
novo_valor = valor_mercadoria - valor_desconto

print(f"O valor do desconto foi R$ {valor_desconto}")
print(f"O novo valor da mercadoria com o desconto de R$ {valor_desconto} é R$ {novo_valor:.2f}")