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

        if opcao == "1":
            valor = float(input("digite o valor: "))
            de = input("de (C/F/K): ").upper()
            para = input("para (C/F/K): ").upper()
            resultado = converter_temperatura(valor, de, para)
            if resultado is not None:
                conversao = f"{valor} {de} = {resultado:.2f} {para}"
                print(conversao)
                historico.append(conversao)
                time.sleep(5)
                os.system('cls')
            else:
                print("conversão inválida!")

        elif opcao == "2":
            valor = float(input("digite o valor: "))
            de = input("de (BRL/USD/EUR): ").upper()
            para = input("para (BRL/USD/EUR): ").upper()
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
            valor = float(input("digite o valor: "))
            de = input("de (m/cm/km): ").lower()
            para = input("para (m/cm/km): ").lower()
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