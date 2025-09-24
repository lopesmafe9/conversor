def converter_temperatura (valor, de, para):
    #normaliza entrada para kelvin
    if de == "C":
        valor_k = valor + 273.15
    elif de == "F":
        valor_k = (valor - 32) * 5/9 + 273.15
    elif de == "K":
        valor_k = valor
    else:
        return None
