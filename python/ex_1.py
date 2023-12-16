valorReal = float(input("Digite o valor em real: "))

#faz o calculo de cada moeda
cotacaoDolar = valorReal * 0.20

cotacaoEuro = valorReal * 0.19

cotacaoLibraEstrelina = valorReal * 0.16

cotacaoDolarCanadense = valorReal * 0.27

cotacaoPesoArgentino = valorReal * 160.11

cotacaoPesoChileno = valorReal * 176.05



#escreve na tela o valor de cada uma das moedas convertidas
print("\n", valorReal, " reais serão convertido em:") 

print("\n", "USD: U$",cotacaoDolar) 

print("\n", "EUR: €",cotacaoEuro)

print("\n", "GBP: £", cotacaoLibraEstrelina)

print("\n", "CAD: C$", cotacaoDolarCanadense)

print("\n", "ARS: ARS", cotacaoPesoArgentino)

print("\n", "CLP: CLP", cotacaoPesoChileno)
