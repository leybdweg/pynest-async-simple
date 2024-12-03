from nest.core import Module

from src.quotes.providers.provider_one import ProviderOne
from .quotes_service import QuotesService


@Module(
    controllers=[],
    providers=[QuotesService, ProviderOne],
    exports=[QuotesService],
    imports=[],
)
class QuotesModule:
    pass

    