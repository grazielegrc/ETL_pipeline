from abc import ABC, abstractmethod
from typing import Dict, Union

class HttpRequesterInterface(ABC):
    
    @abstractmethod
    def request_from_page(self) -> Dict[str, Union[int, str]]:
        pass
