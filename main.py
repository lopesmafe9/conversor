from temperatura import converter_temperatura
from moeda import converter_moeda
from comprimento import converter_comprimento

def menu():
    while True:
        print("\n*.*.* conversor de unidades *.*.*")
        print("1. temperatura")
        print("2. moeda")
        print("3. comprimento")
        print("4. peso")
        print("5. histórico de conversões")
        print("0. sair")

        opcao = input("escolha uma opção: ")

        if opcao == "1":
            valor = float(input("digite o valor: "))
            de = input("de (C/F/K): ").upper()
            para = input("para (C/F/K): ").upper()
            resultado = converter_temperatura(valor, de, para)
            if resultado is not None:
                print(f"{valor} {de} = {resultado:.2f} {para}")
            else:
                print("conversão inválida!")

        elif opcao == "2":
            valor = float(input("digite o valor: "))
            de = input("de (BRL/USD/EUR): ").upper()
            para = input("para (BRL/USD/EUR): ").upper()
            resultado = converter_moeda(valor, de, para)
            if resultado is not None:
                print(f"{valor} {de} = {resultado:.2f} {para}")
            else:
                print("conversão inválida!")
        
        elif opcao == "3":
            valor = float(input("digite o valor: "))
            de = input("de (m/cm/km): ").lower()
            para = input("para (m/cm/km): ").lower()
            resultado = converter_comprimento(valor, de, para)
            if resultado is not None:
                print(f"{valor} {de} = {resultado:.2f} {para}")
            else:
                print("conversão inválida!")
            
        elif opcao == "0":
            print("saindo...")
            break
        else:
            print("opção inválida.")

if __name__ == "__main__":
    menu()