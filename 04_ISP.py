"""
PRINCIPIO SOLID: I - Interface Segregation Principle
Segregación de Interfaces
"""
from abc import ABC, abstractmethod


class Impresora(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Escaner(ABC):
    @abstractmethod
    def escanear(self):
        pass


class ImpresoraSencilla(Impresora):
    def imprimir(self):
        return "Imprimiendo documento..."


class ImpresoraMultifuncional(Impresora, Escaner):
    def imprimir(self):
        return "Imprimiendo documento..."


    def escanear(self):
        return "Escaneando documento..."


# PRUEBA
if __name__ == "__main__":
    impresora = ImpresoraSencilla()
    multifuncional = ImpresoraMultifuncional()

    print("ISP - Prueba de interfaces")
    print(impresora.imprimir())
    print(multifuncional.imprimir())
    print(multifuncional.escanear())

    print("ISP probado correctamente.")
