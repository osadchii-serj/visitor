from interfaces import IVisitor


class VisitorPrice(IVisitor):

    def visit(self, product):
        print(f"Цена на {product.name}  ${product.price}")