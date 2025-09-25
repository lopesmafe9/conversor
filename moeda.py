taxas = {
    ("BRL", "USD"): 0.19,
    ("USD", "BRL"): 5.31,
    ("BRL", "EUR"): 0.16,
    ("EUR", "BRL"): 6.25,
    ("USD", "EUR"): 0.86,
    ("EUR", "USD"): 1.17
}

def converter_moeda (valor, de, para){
    if de == para:
        return valor
    if (de, para) in taxas:
        return valor * taxas [(de, para)]
    else:
        return None
}