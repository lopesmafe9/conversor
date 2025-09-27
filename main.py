from temperatura import converter_temperatura
from moeda import converter_moeda
from comprimento import converter_comprimento
from peso import converter_peso
import os
import time

def menu():
    historico = []
    while True:
        print("\n*.*.* conversor de unidades *.*.*")
        print("1. temperatura")
        print("2. moeda")
        print("3. comprimento")
        print("4. peso")
        print("5. histórico de conversões")
        print("0. sair")

        opcao = input("escolha uma opção: ")
        os.system("cls")

        if opcao == "1":
            print("*.*.* Converter Temperatura*.*.* \n")
            while True:
                try:
                    valor = float(input("Digite o valor: "))
                    break
                except ValueError:
                    print("Valor inválido! Digite um número.")

            while True:
                de = input("de (C/F/K): ").upper()
                if de in ["C", "F", "K"]:
                    break
                print("Unidade inválida! Digite C, F ou K.")

            while True:
                para = input("para (C/F/K): ").upper()
                if para in ["C", "F", "K"]:
                    break
                print("Unidade inválida! Digite C, F ou K.")

            resultado = converter_temperatura(valor, de, para)

            if resultado is not None:
                conversao = f"{valor} {de} = {resultado:.2f} {para}"
                print(conversao)
                historico.append(conversao)
                time.sleep(5)
                os.system('cls')
            else:
                print("Conversão inválida!")

        elif opcao == "2":
            while True:
                try:
                    valor = float(input("digite o valor: "))
                    break
                except ValueError:
                    print("Valor inválido! Digite um número.")
            while True:
                de = input("de (BRL/USD/EUR): ").upper()
                if de in ["BRL", "USD", "EUR"]:
                    break
                print("Unidade inválida! Digite BRL, USD ou EUR.")
            
            while True:
                para = input("para (BRL/USD/EUR): ").upper()
                if para in ["BRL", "USD", "EUR"]:
                    break
                print("Unidade inválida! Digite BRL, USD ou EUR.")
                
            resultado = converter_moeda(valor, de, para)
            if resultado is not None:
                conversao = f"{valor} {de} = {resultado:.2f} {para}"
                print(conversao)
                historico.append(conversao)
                time.sleep(5)
                os.system('cls')
            else:
                print("conversão inválida!")
        
        elif opcao == "3":
            while True:
                try:
                    valor = float(input("digite o valor: "))
                    break
                except ValueError:
                    print("Valor inválido! Digite um número.")
            
            while True:
                de = input("de (m/cm/km): ").lower()
                if de in ["m", "cm", "km"]:
                    break
                print("Unidade inválida! Digite m, cm ou km.")
                
            while True:
                para = input("para (m/cm/km): ").lower()
                if para in ["m", "cm", "km"]:
                    break
                print("Unidade inválida! Digite m, cm ou km.")
                
            resultado = converter_comprimento(valor, de, para)
            
            if resultado is not None:
                conversao = f"{valor} {de} = {resultado:.2f} {para}"
                print(conversao)
                historico.append(conversao)
                time.sleep(5)
                os.system('cls')
            else:
                print("conversão inválida!")
        
        elif opcao == '4':
            while True: 
                valor = float(input("digite o valor: "))
                de = input("de (g/kg/mg): ").lower()
                para = input("para (g/kg/mg): ").lower()
                resultado = converter_peso(valor, de, para)
                if resultado is not None:
                    conversao = f"{valor} {de} = {resultado:.8f} {para}"
                    print(conversao)
                    historico.append(conversao)
                    time.sleep(5)
                    os.system('cls')
                else:
                    print("Conversão inválida!")
            
        elif opcao == '5':
            os.system('cls')
            print("\n*.*.*Histórico de Conversões*.*.*")
            if historico:
                for i, item in enumerate(historico, start=1):
                    print(f'{i}. {item}')
                input("\nPressione qualquer tecla para voltar ao menu...")
                os.system('cls')
            else:
                print("Faça uma conversão para visualizar o histórico")
                time.sleep(5)
                os.system('cls')
            
        elif opcao == "0":
            print("saindo...")
            break
        else:
            print("opção inválida.")

if __name__ == "__main__":
    menu()