from typing import Dict, Union # usado para retornar um dicionário
import requests
from .interfaces.http_requester import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):

    def __init__(self) -> None:
        # __url: __ no começo significa que é um atributo privado
        self.__url = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"
        
    # Dict [key_type, value]: A dictionary with keys and values of various types 
    # can be represented using the Union, Dict[key_type, Union[value_type, ...]]
    def request_from_page(self) -> Dict[str, Union[int, str]]:
        response = requests.get(self.__url, timeout=5)
        return {
            "status_code": response.status_code,
            "html": response.text
        }

