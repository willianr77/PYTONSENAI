nome_cliente = input (" qual é o seu nome:").title()
nome_filme = "cats"
ingresso_inteira = 49.99
ingresso_meia = ingresso_inteira /2
idade = input("digite a sua idade ")
idade= int(idade)

print(f"seja bem vindo (a){nome_cliente}")
print(f"o filme que esta em cartaz é {nome_filme}")
print(f" o ingresso inteira esta R$ {ingresso_inteira} e o ingresso meia esta R$ {ingresso_meia:.2f}")
quantidade_ingressos = input (" digite quantos ingressos voce deseja:") 
quantidade_ingressos = int (quantidade_ingressos)




if idade <= 24 or idade >= 60:
    valor_final = quantidade_ingressos * ingresso_meia
    
else:
    valor_final = quantidade_ingressos * ingresso_inteira
if  quantidade_ingressos <=3:   
    valor_final *= 0.05
elif quantidade_ingressos <= 5: valor_final *= 0.10
elif quantidade_ingressos <=10: valor_final *= 0.20
else  :valor_final*= 0.30
print (f" sua compra saiu o total de R${valor_final:.2f}")