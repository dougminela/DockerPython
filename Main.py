import os
import shutil
import subprocess
import sys

class MAIN:
    @staticmethod
    def mover_arquivos(pasta_origem, pasta_destino_textos, pasta_destino_imagens, pasta_destino_pdfs, pasta_destino_outros):
        for pasta in [pasta_destino_textos, pasta_destino_imagens, pasta_destino_pdfs, pasta_destino_outros]:
            if not os.path.exists(pasta):
                os.makedirs(pasta)

        arquivos = os.listdir(pasta_origem)
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao in [".txt", ".doc", ".docx"]:
                shutil.move(caminho_arquivo, pasta_destino_textos)
            elif extensao in [".jpg", ".png", ".gif"]:
                shutil.move(caminho_arquivo, pasta_destino_imagens)
            elif extensao == ".pdf":
                shutil.move(caminho_arquivo, pasta_destino_pdfs)
            else:
                shutil.move(caminho_arquivo, pasta_destino_outros)

        print("Todos os arquivos foram movidos para as pastas de destino correspondentes.")

    @staticmethod
    def manipular_txt():
        arquivo_clientes = 'clientes.txt'

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
                MAIN.adicionar_dados(arquivo_clientes, f"{nome},{email},{telefone}\n")
                print("Cliente adicionado com sucesso!\n")

            elif opcao == '2':
                MAIN.visualizar_dados(arquivo_clientes)

            elif opcao == '3':
                nome = input("Digite o nome do cliente que deseja buscar: ")
                MAIN.buscar_dados(arquivo_clientes, nome)

            elif opcao == '4':
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.\n")

    @staticmethod
    def adicionar_dados(arquivo, dados):
        with open(arquivo, 'a') as arquivo_txt:
            arquivo_txt.write(dados)

    @staticmethod
    def visualizar_dados(arquivo):
        with open(arquivo, 'r') as arquivo_txt:
            for linha in arquivo_txt:
                nome, email, telefone = linha.strip().split(',')
                print("Nome:", nome)
                print("Email:", email)
                print("Telefone:", telefone)
                print()

    @staticmethod
    def buscar_dados(arquivo, chave):
        with open(arquivo, 'r') as arquivo_txt:
            encontrado = False
            for linha in arquivo_txt:
                nome, email, telefone = linha.strip().split(',')
                if chave.lower() in nome.lower():
                    print("Cliente encontrado:")
                    print("Nome:", nome)
                    print("Email:", email)
                    print("Telefone:", telefone)
                    print()
                    encontrado = True

            if not encontrado:
                print("Cliente não encontrado.\n")

    @staticmethod
    def verificar_servico():
        nome_servico = input("Digite o nome do serviço: ")
        status = subprocess.run(["sc", "query", nome_servico], capture_output=True, text=True)

        if "RUNNING" not in status.stdout:
            subprocess.run(["sc", "start", nome_servico])
            print(f"O serviço {nome_servico} foi iniciado com sucesso.")
        else:
            print(f"O serviço {nome_servico} já está em execução.")

    @staticmethod
    def main():
        if len(sys.argv) < 6:
            print("Uso: python main.py <caminho_da_pasta_de_origem> <caminho_da_pasta_de_textos> <caminho_da_pasta_de_imagens> <caminho_da_pasta_de_pdfs> <caminho_da_pasta_de_outros>")
            sys.exit(1)

        pasta_origem = sys.argv[1]
        pasta_destino_textos = sys.argv[2]
        pasta_destino_imagens = sys.argv[3]
        pasta_destino_pdfs = sys.argv[4]
        pasta_destino_outros = sys.argv[5]

        print("Movendo arquivos...")
        MAIN.mover_arquivos(pasta_origem, pasta_destino_textos, pasta_destino_imagens, pasta_destino_pdfs, pasta_destino_outros)
        
        print("Manipulando TXT...")
        MAIN.manipular_txt()
        
        print("Verificando serviço...")
        MAIN.verificar_servico()

if __name__ == "__main__":
    MAIN.main()
