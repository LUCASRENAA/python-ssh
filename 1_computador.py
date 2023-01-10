# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import paramiko
from scp import SCPClient
from datetime import  datetime, timezone, timedelta

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def dataAtual():
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    #print(data_e_hora_sao_paulo)
    return data_e_hora_sao_paulo

def verificarDados():
    import os

    try:
        usuario = os.environ["usuario_ssh"]
        senha = os.environ["senha_ssh"]
        ip = os.environ["ip_usuario"]

    except KeyError as e:
        raise RuntimeError("Could not find a user or password in environment") from e
    
    return usuario,senha,ip
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import os
    
    data_agora = dataAtual()
    print("Iniciando o script de: " + str(data_agora))


    usuario,senha,ip = verificarDados()


    ssh = createSSHClient(ip, 22, usuario, senha)
    scp = SCPClient(ssh.get_transport())


    arquivo_baixar = '/etc/shadow'
    nome_do_arquivo_saida = f'ips/{ip}/shadow'+str(data_agora)
    scp.get(arquivo_baixar,nome_do_arquivo_saida)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
