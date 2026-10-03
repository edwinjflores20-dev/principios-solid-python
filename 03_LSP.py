"""
PRINCIPIO SOLID: L - Liskov Substitution Principle
Sustitución de Liskov
"""

# INCORRECTO:

class AveIncorrecta:
    def volar(self):
        return "Volando..."


class PinguinoIncorrecto(AveIncorrecta):
    def volar(self):
        raise Exception("Los pingüinos no pueden volar.")


# CORRECTO:

class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Volando..."


class Pinguino(Ave):
    def nadar(self):
        return "Nadando..."


# PRUEBA
if __name__ == "__main__":
    condor = AveVoladora()
    pinguino = Pinguino()

    print("LSP - Prueba de sustitución")
    print("Ave voladora:", condor.volar())
    print("Pingüino:", pinguino.nadar())

    print("LSP probado correctamente.")
