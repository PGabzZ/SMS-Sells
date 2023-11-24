import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_mes = pd.read_excel(f'{mes}.xlsx')

    if (tabela_mes['Vendas'] > 55000).any() :
        vendedor = tabela_mes.loc[tabela_mes['Vendas'] > 55000,'Vendedor'].values[0]
        venda = tabela_mes.loc[tabela_mes['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {venda}')
        message = client.messages.create(
                to="+551100000000",
                from_="Your Account Number from Twilio",
                body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {venda}')
        print(message.sid)








