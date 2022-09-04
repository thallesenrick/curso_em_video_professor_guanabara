prec = float(input('Digite o valor do produto: '))
desconto = prec * (5/100)
valor_final = prec - desconto
print('O valor do produto é {}, e com desconto de {:.2f}, seu novo preço é {:.2f} .'
      .format(prec, desconto, valor_final))

preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, novo))
