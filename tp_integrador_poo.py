# REPSUESTA DEL TRABAJO

class Excursion:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_detalle(self):
        print(f"-- Excursión: {self.nombre} - Precio: ${self.precio}")


class Pasajero:
    def __init__(self, nombre, dni, saldo_inicial):
        self.nombre = nombre
        self.dni = dni
        self.__saldo = saldo_inicial  # Encapsulamiento
        self.excursiones = []  # Lista de objetos Excursion

    def ver_saldo(self):
        return self.__saldo

    def pagar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        else:
            return False

    def agregar_excursion(self, excursion):
        self.excursiones.append(excursion)

    def mostrar_info(self):
        print(f"\n---  Pasajero: {self.nombre} - DNI: {self.dni}")
        print(f"---  Saldo disponible: ${self.__saldo}")
        if self.excursiones:
            print("---  Excursiones compradas:")
            for e in self.excursiones:
                print(f"   ---  {e.nombre}")
        else:
            print("---  No ha comprado excursiones aún.")


class Viaje:
    def __init__(self, destino):
        self.destino = destino
        self.pasajeros = []
        self.excursiones_disponibles = []

    def agregar_pasajero(self):
        nombre = input(">> Nombre del pasajero: ").strip()
        dni = input(">> DNI del pasajero: ").strip()

        if nombre == "" or dni == "":
            print("⚠ No puedes dejar datos vacíos.")
            return

        try:
            saldo = float(input(">> Saldo inicial del pasajero: $"))
            if saldo < 0:
                print("⚠ El saldo no puede ser negativo.")
                return
        except:
            print("⚠ Debes ingresar un número válido.")
            return

        self.pasajeros.append(Pasajero(nombre, dni, saldo))
        print("\n✅ Pasajero agregado exitosamente.")

    def listar_pasajeros(self):
        if not self.pasajeros:
            print("⚠ No hay pasajeros cargados.")
            return
        for p in self.pasajeros:
            p.mostrar_info()

    def listar_excursiones(self):
        if not self.excursiones_disponibles:
            print("⚠ No hay excursiones disponibles.")
        else:
            print("\n--- Excursiones disponibles:")
            for i, e in enumerate(self.excursiones_disponibles):
                print(f"{i+1}. {e.nombre} - ${e.precio}")

    def vender_excursion(self):
        if not self.pasajeros:
            print("⚠ Primero debes cargar pasajeros.")
            return
        if not self.excursiones_disponibles:
            print("⚠ No hay excursiones cargadas.")
            return

        dni = input(">>  Ingrese DNI del pasajero: ")
        pasajero = next((p for p in self.pasajeros if p.dni == dni), None)

        if not pasajero:
            print("\n❌ Pasajero no encontrado.")
            return

        self.listar_excursiones()
        try:
            opcion = int(input(">>  Elija el número de excursión: "))
            if opcion < 1 or opcion > len(self.excursiones_disponibles):
                print("\n❌ Opción inválida.")
                return
        except:
            print("\n❌ Debe ingresar un número válido.")
            return

        excursion = self.excursiones_disponibles[opcion - 1]

        if pasajero.pagar(excursion.precio):
            pasajero.agregar_excursion(excursion)
            print(f"\n✅ {pasajero.nombre} compró '{excursion.nombre}' correctamente.")
        else:
            print("\n❌ Saldo insuficiente.")

    def agregar_excursion_nueva(self):
        nombre = input("---  Nombre de la excursión: ").strip()
        if nombre == "":
            print("⚠ Nombre inválido.")
            return
        try:
            precio = float(input("Precio: $"))
            if precio <= 0:
                print("⚠ Precio inválido.")
                return
        except:
            print("⚠ Debe ingresar un número válido.")
            return

        self.excursiones_disponibles.append(Excursion(nombre, precio))
        print("\n✅ Excursión agregada al sistema.")


# ----------------- PROGRAMA PRINCIPAL ----------------- #

viaje = Viaje("Balneario Camboriú")

# Excursiones iniciales
viaje.excursiones_disponibles.extend([
    Excursion("Beto Carrero World", 50000),
    Excursion("Playa Brava", 15000),
    Excursion("Itapema", 20000),
    Excursion("City Tour", 12000),
])

while True:
    print(f"\n\n📍 VIAJE A {viaje.destino}\n")
    print("    > 1. Cargar pasajero")
    print("    > 2. Ver pasajeros")
    print("    > 3. Ver excursiones disponibles")
    print("    > 4. Comprar excursión")
    print("    > 5. Agregar excursión nueva")
    print("    > 6. Salir")

    opcion = input("\n -- Seleccione una opción:  \n>>> ")

    if opcion == "1":
        viaje.agregar_pasajero()
    elif opcion == "2":
        viaje.listar_pasajeros()
    elif opcion == "3":
        viaje.listar_excursiones()
    elif opcion == "4":
        viaje.vender_excursion()
    elif opcion == "5":
        viaje.agregar_excursion_nueva()
    elif opcion == "6":
        print("\n👋 Gracias por usar el sistema.")
        break
    else:
        print("\n❌ Opción inválida, intentá nuevamente.\n")