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

#converte de kelvin para o destino
    if para == "C":
        return valor_k - 274.15
    elif para == "F":
        return (valor_k - 273.15) * 9/5 + 32
    elif para == "K":
        return valor_k
    else:
        return None
