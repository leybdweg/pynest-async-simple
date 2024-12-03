from nest.core import PyNestFactory, Module
from .app_controller import AppController
from .app_service import AppService
from src.quotes.quotes_module import QuotesModule


@Module(imports=[QuotesModule], controllers=[AppController], providers=[AppService])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()
