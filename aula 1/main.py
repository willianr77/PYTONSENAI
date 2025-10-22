nome_filme  = 'homem aranha'

duracao = 90
quantidade_de_pessoas =  300
valor_ingresso = 49.99 
valor_ingresso_meia = valor_ingresso / 2
sala_cinema = "herois"
print(f'venha assistir ao filme {nome_filme} na sala de cinema { sala_cinema}') 
print(f"este filme  tem  duracao de {duracao} min e o valor do ingresso inteiro é de r$ {valor_ingresso}") 
print(f" e o valor do ingresso como meia é de R$ {valor_ingresso_meia}")
quantidade__ingressos = input (" quantos ingressos voce quer comprar:") 
quantidade__ingressos = int( quantidade__ingressos)
valor_final = quantidade__ingressos * valor_ingresso 
print(f" voce comprou {quantidade__ingressos} ingressos por R$ { valor_final}")