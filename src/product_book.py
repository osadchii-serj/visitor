from dataclasses import dataclass
from interfaces import IProduct


@dataclass
class ProductBook(IProduct):

    price: int | float
    name = "Book"

    def accept(self, visitor):
        visitor.visit(self)
