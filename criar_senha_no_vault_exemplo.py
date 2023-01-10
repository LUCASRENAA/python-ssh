import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='token',
)

# Writing a secret


create_response = client.secrets.kv.v2.create_or_update_secret(
    path='10.11.11.11',
    secret=dict(password='root',user='root',port='22'),
)

print('Secret written successfully.')

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='10.11.11.11')

password = read_response['data']['data']['password']
user = read_response['data']['data']['user']

print(read_response)
print(password)
print(user)

print('Access granted!')