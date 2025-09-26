def converter_peso(valor, de, para):
    if de == 'g' and para == 'kg':
        total = valor * 0.001
        return total
    elif de == 'g' and para == 'g':
        print("Valor já está no peso correspondente!")
        return valor
    elif de == 'kg' and para == 'g':
        total = valor * 1000
        return total
    elif de == 'kg' and para == 'kg':
        print("Valor já está no peso correspondente!")
        return valor
    elif de == 'mg' and para == 'g':
        total = valor * 0.001
        return total
    elif de == 'mg' and para == 'mg':
        print("Valor já está no peso correspondente!")
        return valor
    elif de == 'g' and para == 'mg':
        total = valor * 1000
        return total
    elif de == 'kg' and para == 'mg':
        total = valor * 1000000
        return total
    elif de == 'mg' and para == 'kg':
        total = valor / 1000000
        return total
    else:
        return None