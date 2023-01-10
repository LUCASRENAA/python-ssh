# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import  datetime, timezone, timedelta

import paramiko
from scp import SCPClient
import ipaddress
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

def verificarToken():
    try:
        token = os.environ["token_vault"]
    except KeyError as e:
        raise RuntimeError("Could not find a token in environment") from e
    
    return token
# Press the green button in the gutter to run the script.
def seConectarNoVault(url,token):
    client = hvac.Client(
        url=url,
        token=token,
    )
    return client


def verificarIP():

    try:
        ipaddress.ip_address(ip)
    except KeyError as e:
        raise RuntimeError("Isso não é um ip, ERRO") from e
    os.system(f'mkdir ips/{ip}')


def pegarIps():
    import csv
    ips = []
    with open('ips.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                ips.append(row[0])
                line_count += 1

    return ips
if __name__ == '__main__':
    import os

    import hvac
    import sys


    data_agora = dataAtual()


    token = verificarToken()
    url = "http://127.0.0.1:8200"
    

    client = seConectarNoVault(url, token)

    
    ips = pegarIps()
    #ips = ["10.191.3.47","10.191.3.48","10.191.3.49"]

    for ip in ips:
        verificarIP()
        
        read_response = client.secrets.kv.read_secret_version(path=ip)


        password = read_response['data']['data']['password']
        user = read_response['data']['data']['user']
        port = read_response['data']['data']['port']


        ssh = createSSHClient(ip, int(port), user, password)
        scp = SCPClient(ssh.get_transport())
        scp.get('/etc/shadow',f'ips/{ip}/shadow' + str(data_agora))

        print(scp)
        exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
