import logging
import requests
import pprint

class ExtractData:

    def get_data(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                csv_data = response.content.decode(encoding="latin1")
                return csv_data
            logging.error(f"Não foi possivel obter o arquivo. Response code {response.status_code}")
        except Exception as e:
            logging.error(f"Houve um erro ao tentar obter o arquivo na url: {url}")
            logging.error(f"Erro ao tentar obter o arquivo: {e}")
