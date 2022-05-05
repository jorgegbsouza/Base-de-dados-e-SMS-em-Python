# importando a biblioteca PANDAS para o projeto
import pandas as pd
# importando da biblioteca TWILIO a função CLIENT para o projeto
from twilio.rest import Client
# O SID da sua conta do twilio.com/console
account_sid = "seu_SID"
# O seu Auth Token do twilio.com/console
auth_token = "seu_token"

# Abrindo os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
# Lendo os arquivos Excel
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #Verificando na coluna VENDAS se tem algum valor > 55000
    if (tabela_vendas['Vendas'] > 55000).any():#.any() é usado para dizer que 55000 é um valor
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        # .values[0] é usado para pegar apenas o valor quando usado o .loc
        print(f'Vendedor: {vendedor}\nValor da Venda: R$ {vendas}')

# Enviando um SMS informando que a meta foi batida
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="numero_para_quem_vai_a_mensagem",
    from_="numero_de_quem_vai_enviar_a_mensagem",
    body="mensagem")
#print(message.sid)
