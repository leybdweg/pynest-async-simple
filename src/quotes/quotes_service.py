from typing import Any

from .quotes_model import Quotes
from nest.core import Injectable

from ..models.stay import Stay


@Injectable
class QuotesService:
    providers = {}

    def __init__(self, providers_list = []) -> None:
        for provider in providers_list:
            print('providername', provider.name)
            self.providers[provider.name] = provider

    def fetch_quote(self, provider: str, stay: Stay) -> Any:
        return self.providers[provider].fetch_quote(stay)
