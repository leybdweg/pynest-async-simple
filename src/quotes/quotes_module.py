from nest.core import Module
from .quotes_controller import QuotesController
from .quotes_service import QuotesService


@Module(
    controllers=[],
    providers=[QuotesService],
    imports=[]
)   
class QuotesModule:
    pass

    