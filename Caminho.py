import os
import shutil

# Define os caminhos das pastas de origem e destino
pasta_origem = input("Digite o caminho da pasta de origem: ")
pasta_destino_textos = input("Digite o caminho da pasta de destino para textos: ")
pasta_destino_imagens = input("Digite o caminho da pasta de destino para imagens: ")
pasta_destino_pdfs = input("Digite o caminho da pasta de destino para PDFs: ")
pasta_destino_outros = input("Digite o caminho da pasta de destino para outros arquivos: ")

# Verifica se as pastas de destino existem, caso contrário, cria-as
for pasta in [pasta_destino_textos, pasta_destino_imagens, pasta_destino_pdfs, pasta_destino_outros]:
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Lista todos os arquivos na pasta de origem
arquivos = os.listdir(pasta_origem)

# Para cada arquivo na pasta de origem
for arquivo in arquivos:
    caminho_arquivo = os.path.join(pasta_origem, arquivo)

    # Determina a extensão do arquivo
    extensao = os.path.splitext(arquivo)[1].lower()

    # Move o arquivo para a pasta de destino correspondente com base na extensão
    if extensao in [".txt", ".doc", ".docx"]:
        shutil.move(caminho_arquivo, pasta_destino_textos)
    elif extensao in [".jpg", ".png", ".gif"]:
        shutil.move(caminho_arquivo, pasta_destino_imagens)
    elif extensao == ".pdf":
        shutil.move(caminho_arquivo, pasta_destino_pdfs)
    else:
        shutil.move(caminho_arquivo, pasta_destino_outros)

print("Todos os arquivos foram movidos para as pastas de destino correspondentes.")