from interfaces import IVisitor


class VisitorTax(IVisitor):

    def visit(self, product):
        tax = product.price * 0.1
        print(f"Налог на {product.name} ${round(tax, 2)}")
