from product_electronics import ProductElectronics
from product_book import ProductBook

from visitor_price import VisitorPrice
from visitor_tax import VisitorTax

if __name__ == "__main__":
    products = [
        ProductElectronics(15.99),
        ProductBook(299.99),
    ]

    price_visitor = VisitorPrice()
    tax_visitor = VisitorTax()

    for product in products:
        product.accept(price_visitor)
        product.accept(tax_visitor)