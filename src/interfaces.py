from abc import ABC, abstractmethod


class IVisitor(ABC):

    @abstractmethod
    def visit(self, product):
        raise NotImplementedError()


class IProduct(ABC):

    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError()
