import csv
import os

def adicionar_dados(arquivo, dados):
    with open(arquivo, 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(dados)

def visualizar_dados(arquivo):
    with open(arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for linha in reader:
            print("Nome:", linha[0])
            print("Email:", linha[1])
            print("Telefone:", linha[2])
            print()

def buscar_dados(arquivo, chave):
    with open(arquivo, 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        encontrado = False
        for linha in reader:
            if chave.lower() in linha[0].lower():
                print("Cliente encontrado:")
                print("Nome:", linha[0])
                print("Email:", linha[1])
                print("Telefone:", linha[2])
                print()
                encontrado = True
                break

        if not encontrado:
            print("Cliente não encontrado.\n")

def main():
    arquivo_clientes = 'clientes.csv'

    while True:
        print("Selecione uma opção:")
        print("1. Adicionar cliente")
        print("2. Visualizar clientes")
        print("3. Buscar cliente por nome")
        print("4. Encerrar programa")

        opcao = input("Opção: ")

        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            adicionar_dados(arquivo_clientes, [nome, email, telefone])
            print("Cliente adicionado com sucesso!\n")

        elif opcao == '2':
            visualizar_dados(arquivo_clientes)

        elif opcao == '3':
            nome = input("Digite o nome do cliente que deseja buscar: ")
            buscar_dados(arquivo_clientes, nome)

        elif opcao == '4':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

if __name__ == "__main__":
    main()