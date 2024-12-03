from typing import Any

from src.models.stay import Stay
from nest.core import Injectable


@Injectable
class ProviderOne:  # TODO: set interface (ProviderInterface):

    name = "ProviderOne"

    def __init__(self):
        # connect / get auth
        pass

    def fetch_quote(self, stay: Stay) -> Any:
        print('staaaay', stay)
        return {"stay": stay, 'aa': 123}
