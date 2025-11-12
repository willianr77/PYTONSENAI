valor = float (input("Digite o valor da compra: R$ "))
print(" Formas de pagamento:")
print("1 - À vista Dinheiro (10% de desconto)")
print("2 - À vista Cartão (2% de desconto)")
print("3 - À vista PIX (25% de desconto)")
print("4 - 2x no Cartão (preço normal)")
print("5 - 3x ou mais no Cartão (20% de juros)")

opcao = int(input("Escolha a opção de pagamento (1 a 5): "))
if opcao == 1:
    valor_final = valor * 0.90
    descricao = "À vista Dinheiro (10% de desconto)"
elif opcao == 2:
    valor_final = valor * 0.95
    descricao = "À vista Cartão (5% de desconto)"
elif opcao == 3:
    valor_final = valor * 0.90
    descricao = "À vista PIX (10% de desconto)"
elif opcao == 4:
    valor_final = valor
    descricao = "2x no Cartão (preço normal)"
    parcela = valor_final / 2
    print(f"\n Valor de cada parcela: R${parcela:.2f}")
elif opcao == 5:
    valor_final = valor * 1.20
    descricao = "3x ou mais no Cartão (20% de juros)"
    total_parcelas = int(input("Digite o número de parcelas (3 ou mais): "))
    parcela = valor_final / total_parcelas
    print(f"\n Valor de cada parcela: R${parcela:.2f}")
else:
    print("\n Opção inválida! Pagamento cancelado.")
    valor_final = 0
    descricao = "Nenhum"

    if valor_final > 0:

    print(f" Valor final a pagar: R${valor_final:.2f}")

    
   
    

