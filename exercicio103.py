print("Programa para conversão de moedas")
print()

# Entrada de dados / Leitura do arquivo
moedas = {}
with open("moedas.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        if len(dados) == 4:
            sigla = dados[0]
            nome_pt = dados[2]
            taxa = float(dados[3])
            moedas[sigla] = {"nome": nome_pt, "taxa": taxa}
            moedas[nome_pt] = {"nome": nome_pt, "taxa": taxa}

valor_reais = float(input("Informe o valor em R$: "))
destino = input("Informe a moeda de destino (ex: USD, EUR, Euro, Dólar dos Estados Unidos): ")
print()

# Processamento e Saída de dados
if destino in moedas:
    valor_convertido = valor_reais / moedas[destino]["taxa"]
    print(f"Moeda: {moedas[destino]['nome']}")
    print(f"Valor convertido: {valor_convertido:.2f}")
else:
    print("Moeda não encontrada no arquivo!")
print()