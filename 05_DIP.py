"""
PRINCIPIO SOLID: D - Dependency Inversion Principle
Inversión de Dependencias
"""

from abc import ABC, abstractmethod

# ABSTRACCIÓN

class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

class ServicioSMS(ServicioMensaje):
    def enviar(self, mensaje):
        return f"SMS: {mensaje}"


class ServicioEmail(ServicioMensaje):
    def enviar(self, mensaje):
        return f"Email: {mensaje}"


# CLASE DE ALTO NIVEL

class Notificador:
    def __init__(self, servicio):
        self.servicio = servicio

    def enviar_alerta(self, mensaje):
        return self.servicio.enviar(mensaje)


# PRUEBA
if __name__ == "__main__":
    mensaje = "Alerta: stock mínimo alcanzado."

    notificador_sms = Notificador(ServicioSMS())
    notificador_email = Notificador(ServicioEmail())

    print("DIP - Prueba de inversión de dependencias")
    print(notificador_sms.enviar_alerta(mensaje))
    print(notificador_email.enviar_alerta(mensaje))

    print("DIP probado correctamente.")
