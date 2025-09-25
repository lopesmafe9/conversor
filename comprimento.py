def converter_comprimento(valor, de, para):
    #base em metros
    fatores = {"m" : 1, "cm" : 0.01, "km" : 1000} 

    if de not in fatores or para not in fatores:
        return None

    valor_metros = valor * fatores[de]
    return valor valor_metros/fatores[para]