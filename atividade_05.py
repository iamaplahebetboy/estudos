#Moedas disponiveis
taxas_de_cambio = {
    'USD': 1.0,       # Dólar 
    'EUR': 0.85,      # Euro
    'BRL': 1.5,       # Real
}

#Comando para a conversão
def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem not in taxas_de_cambio or moeda_destino not in taxas_de_cambio:
        return "Moeda não suportada."
    
    taxa_origem = taxas_de_cambio[moeda_origem]
    taxa_destino = taxas_de_cambio[moeda_destino]
    
    valor_convertido = valor * (taxa_destino / taxa_origem)
    return valor_convertido

#Conversão final
while True:
    print("\nConversor de Moedas")
    print("Moedas suportadas: USD, EUR, BRL")
    moeda_origem = input("Digite a moeda de origem: ").upper()
    moeda_destino = input("Digite a moeda de destino: ").upper()

    if moeda_origem == moeda_destino:
        print("As moedas de origem e destino são as mesmas.")
    else:
        valor = float(input(f"Digite o valor em {moeda_origem}: "))
        valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino)
        if valor_convertido == "Moeda não suportada.":
            print(valor_convertido)
        else:
            print(f"Valor convertido em {moeda_destino}: {valor_convertido:.2f}")

    continuar = input("Deseja fazer outra conversão? (S/N): ").upper()
    if continuar != 'S':
        print("Obrigado por usar o Conversor de Moedas. Até logo!")
        break
