from dataclasses import dataclass
from interfaces import IProduct


@dataclass
class ProductElectronics(IProduct):

    price: int | float
    name = "Electronics"

    def accept(self, visitor):
        visitor.visit(self)
