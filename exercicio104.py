valores = {
    "PR": 0.0190,
    "AC": 0.02, "ES": 0.02, "SC": 0.02,
    "PE": 0.024,
    "MA": 0.025, "PA": 0.025, "PB": 0.025, "SE": 0.025,
    "AL": 0.03, "AM": 0.03, "AP": 0.03, "BA": 0.03, "DF": 0.03, "MS": 0.03,
    "MT": 0.03, "PI": 0.03, "RN": 0.03, "RO": 0.03, "RR": 0.03, "RS": 0.03,
    "CE": 0.035, "TO": 0.035,
    "GO": 0.0375,
    "MG": 0.04, "RJ": 0.04, "SP": 0.04,
}

print("Programa para calcular o valor a pagar de IPVA")
print()

estado = input("Informe a sigla do estado onde o veículo está registrado: ").upper()
valor = float(input("Informe o valor do carro: "))

print()
if estado in valores:
    valor_calculado = valores[estado] * valor
    print(f"O valor a pagar pelo IPVA, no {estado}, é de {valor_calculado:.2f}")
else:
    print(f"O estado {estado} é inválido")
