# Importação da biblioteca requests para realizarmos requisões a uma API, a fim de 
# retornarmos os dados que irão alimentar nosso banco de dados.
import requests

# Endpoint da aplicação
# Ponto de comunicação do nosso código com o servidor com o qual a api irá
# estabelecer conexão.
try:
    api_url = "https://brasilapi.com.br/api/cvm/corretoras/v1"
    response = requests.get(api_url)

except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP (Status Code): {e}")
