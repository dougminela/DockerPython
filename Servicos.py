import subprocess

# Obtém o nome do serviço que deseja verificar e iniciar
nome_servico = input("Digite o nome do serviço: ")

# Obtém o status do serviço especificado
status = subprocess.run(["sc", "query", nome_servico], capture_output=True, text=True)

# Verifica se o status do serviço indica que está em execução
if "RUNNING" not in status.stdout:
    # Inicia o serviço
    subprocess.run(["sc", "start", nome_servico])
    print(f"O serviço {nome_servico} foi iniciado com sucesso.")
else:
    print(f"O serviço {nome_servico} já está em execução.")