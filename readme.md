Структура классов

    Visitor: базовый интерфейс для всех посетителей (например, для расчета цен и налогов).

    VisitorPrice: конкретный посетитель для расчета цены товара.

    VisitorTax: конкретный посетитель для расчета налога на товар.

    Product: базовый класс для всех товаров с методом accept().

    ProductBook: конкретный класс для книги.

    ProductElectronics: конкретный класс для электроники.


Описание классов и методов

    Visitor: базовый интерфейс для всех посетителей с методом visit(), который должен быть реализован в конкретных классах посетителей.

    VisitorPrice: реализует метод visit(), который выводит цену товара.

    VisitorTax: реализует метод visit(), который вычисляет и выводит налог на товар (предполагается 10%).

    Product: базовый класс для всех товаров с методом accept(), который принимает посетителя.

    ProductBook и ProductElectronics: конкретные реализации товаров, которые реализуют метод accept(), вызывая метод visit() у переданного посетителя.