# Sistema de Gestión de Viaje - Balneario Camboriú ✈️🏖️

Este proyecto es un trabajo integrador de Programación Orientada a Objetos (POO).  
El objetivo es modelar una situación real utilizando clases, atributos, métodos, constructor `__init__` y encapsulamiento, demostrando el manejo de estado interno y operaciones sobre dicho estado.

---

## 📌 Descripción del programa

El sistema simula la gestión de un viaje turístico al destino **Balneario Camboriú (Brasil)**, permitiendo administrar pasajeros y excursiones durante el viaje.

Mediante un menú interactivo en consola, el usuario puede:

- Registrar nuevos pasajeros con un saldo inicial
- Consultar los pasajeros cargados y sus excursiones adquiridas
- Ver el listado de excursiones disponibles
- Vender una excursión a un pasajero (validando que tenga saldo suficiente)
- Agregar nuevas excursiones al sistema

El programa realiza validaciones básicas (como evitar números negativos o campos vacíos) y muestra resultados claros al usuario.

---

## 🧱 Modelado con Clases

Para representar la situación real se utilizaron tres clases:

### ✅ Clase `Pasajero`
- Atributos: nombre, DNI, **saldo encapsulado**, excursiones (lista)
- Métodos de consulta y modificación de estado (pagar, agregar excursión, ver información del pasajero)

### ✅ Clase `Excursion`
- Atributos: nombre, precio, descripción
- Método para visualizar la información de la excursión

### ✅ Clase `Viaje`
- Atributos: destino, lista de pasajeros, lista de excursiones disponibles
- Métodos para administrar el sistema (agregar pasajeros, listar, comprar excursiones, etc.)

El saldo del pasajero está encapsulado mediante `__saldo`, garantizando seguridad en la manipulación del valor.

---

## ▶️ Ejecución

Para ejecutar el programa:

1. Asegúrate de tener Python 3 instalado
2. Ejecutá el archivo desde una terminal o entorno como VS Code:

```bash
python tp_integrador_poo.py
```

## 👨‍💻 Autor
- 🧑 Nombre: Benjamin Ezequiel Vasques Perrone
- 🏫 Escuela: Escuela Publica Bilingüe Digital Maatma Gandhi
- 📚 Curso: 6to año
- 📅 Año: 2025
