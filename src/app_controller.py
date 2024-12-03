from nest.core import Controller, Get, Post
from .models.stay import Stay
from .quotes.quotes_service import QuotesService


@Controller("/")
class AppController:

    def __init__(self, quote_service: QuotesService):
        self.quote_service = quote_service

    @Post("/")
    def create_stay(self, stay: Stay):
        print("aaaaa")
        return self.quote_service.fetch_quote(provider="ProviderOne", stay=stay)
