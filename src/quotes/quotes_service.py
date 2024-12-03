from typing import Any

from .providers.provider_one import ProviderOne
from nest.core import Injectable

from ..models.stay import Stay


@Injectable
class QuotesService:
    providers = {}

    # providers list should come in module with useFactory
    def __init__(self, providers_list=[ProviderOne()]) -> None:
        for provider in providers_list:
            print('providername', provider.name)
            self.providers[provider.name] = provider

    def fetch_quote(self, provider: str, stay: Stay) -> Any:
        print('fetch_quote', stay)
        provider = self.providers[provider]
        print('provider', provider)
        return provider.fetch_quote(stay)
