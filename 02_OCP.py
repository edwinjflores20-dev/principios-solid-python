"""
PRINCIPIO SOLID: O - Open/Closed Principle
Abierto/Cerrado
"""

class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.80


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.90

class DescuentoEmpleado(Descuento):
    def aplicar(self, precio):
        return precio * 0.85


# PRUEBA
if __name__ == "__main__":
    precio = 100

    descuentos = [
        ("VIP", DescuentoVIP()),
        ("Estudiante", DescuentoEstudiante()),
        ("Empleado", DescuentoEmpleado())
    ]

    print("OCP - Prueba de descuentos")

    for nombre, descuento in descuentos:
        resultado = descuento.aplicar(precio)
        print(f"{nombre}: S/ {resultado:.2f}")

    print("OCP probado correctamente.")
