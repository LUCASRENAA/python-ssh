# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import  datetime, timezone, timedelta

import paramiko
from scp import SCPClient
import ipaddress




class arquivo_classe:
    def __init__(self, usuarios, nome):
        self.usuarios = usuarios
        self.nome = nome


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


def verificarIP():

    try:
        ipaddress.ip_address(ip)
    except KeyError as e:
        raise RuntimeError("Isso não é um ip, ERRO") from e
    os.system(f'mkdir {ip}')


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

    data_agora = dataAtual()

    
    ips = pegarIps()
    #ips = ["10.191.3.47","10.191.3.48","10.191.3.49"]

    for ip in ips:
        verificarIP()
        for _, _, arquivos in os.walk(f'ips/{ip}'):
            usuarios_lista = []
            for arquivo in arquivos:
                ref_arquivo = open(f"ips/{ip}/{arquivo}","r")
                linha = ref_arquivo.readline()
                usuarios = []
                while linha:
                    usuario = linha.split(':')[0]
                    #print(usuario)
                    linha = ref_arquivo.readline()
                    usuarios.append(usuario)
                ref_arquivo.close()
                objeto = arquivo_classe(usuarios,arquivo)
                usuarios_lista.append(objeto)


        #print(usuarios_lista)
        usuario1 = []
        usuario2 = []
        usuarios_lista.reverse()
        for usuario in usuarios_lista:
            if usuario1 == []:
                usuario1 = usuario.usuarios
                nome_arquivo = usuario.nome
                continue
            else:
                usuario2 = usuario.usuarios





                print("Arquivo: "  + str(nome_arquivo))
                print("Arquivo2: "  + str(usuario.nome))


                difference_1 = set(usuario1).difference(set(usuario2))
                difference_2 = set(usuario2).difference(set(usuario1))


                validar = 0
                for a in difference_2:
                    print(f'O usuário: {a} foi acrescentado')
                    validar = 1
                
                for a in difference_1:
                    print(f'O usuário: {a} foi removido!')
                    validar  = 1

                if validar == 0:
                    print("Não ocorreu mudanças entre os dois arquivos " + str(nome_arquivo) + ": " + str(usuario.nome))

                        

                usuario1 = usuario.usuarios
                nome_arquivo = usuario.nome

                

            

        exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
