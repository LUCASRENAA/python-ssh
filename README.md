# python-ssh


# Dependencias para o primeiro script

### Crie um arquivo chamado .keys e coloque o usuário,senha e ip (como no exemplo a baixo)

```
export usuario_ssh='root'
export senha_ssh='root'
export ip_usuario='10.11.11.11'
```

### E para colocar esses valores na variavel de ambiente do sistema, utilize o seguinte comando


```
source .keys
```


Pronto, agora é só executar o programa


# Dependencias para o segundo script
## Instale o vault
https://developer.hashicorp.com/vault/downloads?host=www.vaultproject.io

### Depois de instalar o vault, rode o vault na sua máquina (Não esqueça de mudar o token para o seu token)
```
vault server -dev -dev-root-token-id="token"
```



### Crie um arquivo chamado .keys_2  (Não esqueça de mudar o token para o seu token)

e coloque algo como 

```
export token_vault='token'
```

E para colocar a senha na variavel de ambiente rode o seguinte comando


```
source .keys_2
```


Pronto, agora é só executar o programa
