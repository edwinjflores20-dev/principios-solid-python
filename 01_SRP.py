"""
PRINCIPIO SOLID: S - Single Responsibility Principle
Responsabilidad Única
"""

# INCORRECTO:

class ReporteIncorrecto:
    def __init__(self, contenido):
        self.contenido = contenido

    def guardar_en_archivo(self, ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(self.contenido)


# CORRECTO:

class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido


class GuardadorReporte:
    def guardar(self, reporte, ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(reporte.contenido)

# PRUEBA
if __name__ == "__main__":
    reporte = Reporte("Reporte de prueba del principio SRP.")
    guardador = GuardadorReporte()

    ruta = "reporte_srp.txt"
    guardador.guardar(reporte, ruta)

    print("SRP probado correctamente.")
    print(f"Reporte guardado en: {ruta}")
