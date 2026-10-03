# Principios SOLID en Python

## Descripción

Este proyecto demuestra mediante ejemplos prácticos en Python los cinco principios SOLID de diseño de software:

- **S - Single Responsibility Principle (Responsabilidad Única)**
- **O - Open/Closed Principle (Abierto/Cerrado)**
- **L - Liskov Substitution Principle (Sustitución de Liskov)**
- **I - Interface Segregation Principle (Segregación de Interfaces)**
- **D - Dependency Inversion Principle (Inversión de Dependencias)**

El proyecto está basado en el material proporcionado sobre los principios SOLID.

## Objetivo

Probar cada uno de los principios SOLID mediante programas independientes en Python, mostrando una implementación correcta y, cuando corresponde, una situación incorrecta.

## Requisitos

- Python 3.x
- No se requieren librerías externas.

## Estructura del proyecto

```text
principios-solid-python/
│
├── README.md
├── 01_SRP.py
├── 02_OCP.py
├── 03_LSP.py
├── 04_ISP.py
└── 05_DIP.py
```

## Cómo ejecutar los programas

Desde la carpeta del proyecto, ejecutar:

```bash
python 01_SRP.py
python 02_OCP.py
python 03_LSP.py
python 04_ISP.py
python 05_DIP.py
```

También se pueden ejecutar individualmente desde Visual Studio Code, IDLE u otro editor compatible con Python.

## Resultados esperados

### SRP
Se crea un archivo llamado `reporte_srp.txt` y se muestra:

```text
SRP probado correctamente.
```

### OCP
Se muestran diferentes tipos de descuento:

```text
OCP - Prueba de descuentos
VIP: S/ 80.00
Estudiante: S/ 90.00
Empleado: S/ 85.00
OCP probado correctamente.
```

### LSP
Se demuestra que las aves con capacidades diferentes pueden tener comportamientos apropiados:

```text
LSP - Prueba de sustitución
Ave voladora: Volando...
Pingüino: Nadando...
LSP probado correctamente.
```

### ISP
Se demuestra la separación entre las capacidades de imprimir y escanear:

```text
ISP - Prueba de interfaces
Imprimiendo documento...
Imprimiendo documento...
Escaneando documento...
ISP probado correctamente.
```

### DIP
Se demuestra que `Notificador` puede trabajar con diferentes servicios mediante una abstracción:

```text
DIP - Prueba de inversión de dependencias
SMS: Alerta: stock mínimo alcanzado.
Email: Alerta: stock mínimo alcanzado.
DIP probado correctamente.
```

## Conclusión

Los ejemplos muestran cómo los principios SOLID ayudan a organizar el código, separar responsabilidades, facilitar las extensiones y reducir el acoplamiento entre componentes del software.

## Autor

Trabajo académico - Principios SOLID en Python.
