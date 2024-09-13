from typing import Dict, Union

class HttpRequesterSpy:

    def __init__(self) -> None:     
        self.request_from_page_counter = 0  
        

    def request_from_page(self) -> Dict[str, Union[int, str]]:    
        self.request_from_page_counter += 1   
        return {
            "status_code": 200,
            "html": "<h1>OlaMundo</h1>"
        }
