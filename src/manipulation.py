# Importação da biblioteca requests para realizarmos requisões a uma API, a fim de 
# retornarmos os dados que irão alimentar nosso banco de dados.
import requests
import logging

# O logging aqui podemos comparar ele com o print(), porém ele é mais esquematizado e rico em detalhes.
# Iniciamos aqui com as configurações principais, definindo o nível das informações a ser trabalhadas.
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Endpoint da aplicação
# Ponto de comunicação do nosso código com o servidor com o qual a api irá
# estabelecer conexão.
api_url = "https://brasilapi.com.br/api/cvm/corretoras/v1"

def data_extraction(url: str) -> list[dict]:
    # Processo Inicial do pipeline.
    # Extração de dados da API, trabalhamos aqui com a Brasil Api, que trará
    # dentro do dicionário que esta função retornará todas as corretoras presentes 
    # no Brasil, estejam elas ativas ou não.
    response = requests.get(api_url, timeout=10)

    # Aqui vamos usar o raise_for_status() para caso tenhamos um erro, seja na requisição 
    # ou na resposta, ele imediatamente lança um erro e interrompe o funcionamento do código.
    response.raise_for_status() 
    dados = response.json()
    logger.info("Extraída %d corretoras da API", len(dados))
    return dados

def data_transform(dados: list[dict]) -> list[tuple]:
    # Vamos converter cada um dos dicionários em tuplas para o banco de dados,
    # por isso usamos o -> list[tuple] aqui como o retorno da função.
    # Declaramos o di
    registros = []

    for item in dados:
        registros.append(
            item["nome_comercial"],
            item["email"],
            item["telefone"]
        )
        return registros
    
