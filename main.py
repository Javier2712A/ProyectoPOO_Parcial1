# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]

"""
PROGRAMA PRINCIPAL - Sistema de Gestión de Servicios de Cine/Eventos
Este programa integra todas las clases y demuestra:
- Herencia (Servicio -> ServicioCine, ServicioEvento)
- Encapsulamiento (properties y setters en todas las clases)
- Polimorfismo (métodos que trabajan con listas de objetos de la superclase)
"""

from datetime import datetime
from servicio import Servicio
from servicio_cine import ServicioCine
from servicio_evento import ServicioEvento
from cliente import Cliente
from gestor_servicios import GestorServicios


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 70)
    print("SISTEMA DE GESTIÓN DE CINE/EVENTOS - CINEMAX ENTERTAINMENT")
    print("=" * 70)
    print("1. Ver todos los servicios")
    print("2. Ver servicios disponibles")
    print("3. Realizar venta")
    print("4. Ver clientes")
    print("5. Generar reporte completo (Polimorfismo)")
    print("6. Calcular ingresos totales (Polimorfismo)")
    print("7. Ver estadísticas")
    print("8. Salir")

def crear_datos_ejemplo(gestor: GestorServicios):
    """
    Crea datos de ejemplo para demostrar el sistema.

    Args:
        gestor: Instancia del GestorServicios
    """
    print("\n INICIALIZANDO SISTEMA CON DATOS DE EJEMPLO...")

    # ========== CREAR SERVICIOS DE CINE ==========
    print("\n  Creando servicios de CINE...")

    cine1 = ServicioCine(
        codigo="C001",
        nombre="Función Estreno",
        fecha=datetime(2024, 12, 15, 20, 30),
        precio_base=8.50,
        pelicula="Dune: Part Two",
        sala=1,
        es_3d=False,
        es_vip=False
    )
    cine1.vender_entradas(45)
    gestor.agregar_servicio(cine1)

    cine2 = ServicioCine(
        codigo="C002",
        nombre="Función 3D VIP",
        fecha=datetime(2024, 12, 15, 21, 0),
        precio_base=8.50,
        pelicula="Avatar 3",
        sala=5,
        es_3d=True,
        es_vip=True
    )
    cine2.vender_entradas(60)
    gestor.agregar_servicio(cine2)

    cine3 = ServicioCine(
        codigo="C003",
        nombre="Matine Infantil",
        fecha=datetime(2024, 12, 16, 11, 0),
        precio_base=8.50,
        pelicula="Moana 2",
        sala=3,
        es_3d=True,
        es_vip=False
    )
    cine3.vender_entradas(80)
    gestor.agregar_servicio(cine3)

    # ========== CREAR SERVICIOS DE EVENTOS ==========
    print("\n Creando servicios de EVENTOS...")

    evento1 = ServicioEvento(
        codigo="E001",
        nombre="Noche de Rock",
        fecha=datetime(2024, 12, 20, 20, 0),
        precio_base=45.00,
        artista="Los Rockeros",
        tipo_evento="Concierto",
        duracion_horas=2.5,
        zona="General"
    )
    evento1.vender_entradas(250)
    gestor.agregar_servicio(evento1)

    evento2 = ServicioEvento(
        codigo="E002",
        nombre="Opera Clásica",
        fecha=datetime(2024, 12, 22, 19, 30),
        precio_base=65.00,
        artista="Compañía Nacional de Opera",
        tipo_evento="Opera",
        duracion_horas=3.5,
        zona="VIP"
    )
    evento2.incluye_meet_and_greet = True
    evento2.vender_entradas(180)
    gestor.agregar_servicio(evento2)

    evento3 = ServicioEvento(
        codigo="E003",
        nombre="Comedia Stand-up",
        fecha=datetime(2024, 12, 25, 21, 0),
        precio_base=30.00,
        artista="Comediantes Unidos",
        tipo_evento="Stand-up Comedy",
        duracion_horas=2.0,
        zona="Preferencial"
    )
    evento3.vender_entradas(320)
    gestor.agregar_servicio(evento3)

    # ========== CREAR CLIENTES ==========
    print("\n Registrando clientes...")

    cliente1 = Cliente(
        cedula="0912345678",
        nombre="Juan Carlos",
        apellido="Pérez López",
        email="juan.perez@email.com",
        telefono="0987654321"
    )
    gestor.agregar_cliente(cliente1)

    cliente2 = Cliente(
        cedula="0923456789",
        nombre="María Fernanda",
        apellido="González Ruiz",
        email="maria.gonzalez@email.com",
        telefono="0976543210"
    )
    gestor.agregar_cliente(cliente2)

    cliente3 = Cliente(
        cedula="0934567890",
        nombre="Carlos Andrés",
        apellido="Martínez Silva",
        email="carlos.martinez@email.com",
        telefono="0965432109"
    )
    gestor.agregar_cliente(cliente3)

    cliente4 = Cliente(
        cedula="0945678901",
        nombre="Ana Lucía",
        apellido="Torres Vega",
        email="ana.torres@email.com",
        telefono="0954321098"
    )
    gestor.agregar_cliente(cliente4)

    print("\n Sistema inicializado correctamente")
    print(f"   • {len(gestor._servicios)} servicios creados")
    print(f"   • {len(gestor._clientes)} clientes registrados")


def demostrar_herencia():
    """Demuestra el concepto de herencia en el sistema."""
    print("DEMOSTRACIÓN DE HERENCIA")
    print("\n Estructura de Herencia:")
    print("   Servicio (Superclase abstracta)")
    print("      ─ ServicioCine (Subclase 1)")
    print("      ─ ServicioEvento (Subclase 2)")
    print("\n✓ ServicioCine hereda: codigo, nombre, fecha, precio_base, estado")
    print("  + Agrega: pelicula, sala, es_3d, es_vip, asientos_vendidos")
    print("\n✓ ServicioEvento hereda: codigo, nombre, fecha, precio_base, estado")
    print("  + Agrega: artista, tipo_evento, duracion_horas, zona, entradas_vendidas")


def demostrar_encapsulamiento(gestor: GestorServicios):
    """Demuestra el concepto de encapsulamiento en el sistema."""
    print("DEMOSTRACIÓN DE ENCAPSULAMIENTO")

    print("\n Todos los atributos son privados (con _ al inicio)")
    print("   Se acceden mediante @property y @setter con validaciones")

    # Obtener un servicio de ejemplo
    servicio = gestor._servicios[0] if gestor._servicios else None

    if servicio:
        print(f"\n Ejemplo con servicio '{servicio.nombre}':")
        print(f"   • Nombre actual: {servicio.nombre}")

        print("\n   Intentando cambiar nombre a valor vacío...")
        try:
            servicio.nombre = ""
        except ValueError as e:
            print(f"   Validación activada: {e}")

        print("\n   Intentando cambiar precio_base a valor negativo...")
        try:
            servicio.precio_base = -10
        except ValueError as e:
            print(f"   Validación activada: {e}")

        print("\n   Cambiando nombre a valor válido...")
        servicio.nombre = "Función Actualizada"
        print(f"   Nombre actualizado: {servicio.nombre}")


def demostrar_polimorfismo(gestor: GestorServicios):
    """Demuestra el concepto de polimorfismo con los métodos obligatorios."""
    print("DEMOSTRACIÓN DE POLIMORFISMO")

    print("\n Los métodos polimórficos trabajan con listas de tipo Servicio")
    print("   y funcionan con cualquier subclase (ServicioCine o ServicioEvento)")
    print("   sin necesidad de verificar el tipo específico.")

    # Crear lista mixta de servicios
    servicios_mixtos = gestor._servicios.copy()

    print(f"\n Lista de servicios ({len(servicios_mixtos)} elementos):")
    for i, serv in enumerate(servicios_mixtos, 1):
        tipo = "CINE" if isinstance(serv, ServicioCine) else "EVENTO"
        print(f"   {i}. [{tipo}] {serv.nombre}")

    # MÉTODO POLIMÓRFICO 1
    print(" MÉTODO POLIMÓRFICO 1: calcular_ingresos_totales()")
    print("   Este método recibe una lista de servicios y calcula los ingresos")
    print("   totales llamando a calcular_precio_total() de cada objeto,")
    print("   sin importar si es ServicioCine o ServicioEvento.")

    ingresos = gestor.calcular_ingresos_totales(servicios_mixtos)
    print(f"\n  INGRESOS TOTALES: ${ingresos:,.2f}")

    # MÉTODO POLIMÓRFICO 2
    print(" MÉTODO POLIMÓRFICO 2: generar_reporte_servicios()")
    print("   Este método recibe una lista de servicios y genera un reporte")
    print("   llamando a mostrar_info() de cada objeto, sin importar su tipo.")

    input("\n   Presiona ENTER para ver el reporte completo...")
    reporte = gestor.generar_reporte_servicios(servicios_mixtos)
    print(reporte)


def main():
    """Función principal que ejecuta el sistema completo."""

    # Banner inicial
    print("\n" + "=" * 70)
    print(" " * 15 + "SISTEMA DE GESTIÓN DE CINE/EVENTOS")
    print(" " * 20 + "Grupo 9 - Proyecto POO")
    print("=" * 70)

    # Crear instancia del gestor
    gestor = GestorServicios("CineMax Entertainment")

    # Cargar datos de ejemplo
    crear_datos_ejemplo(gestor)

    # Demostraciones de conceptos POO
    print("\n\n" + " DEMOSTRACIONES DE CONCEPTOS POO ".center(70, "="))

    demostrar_herencia()
    input("\nPresiona ENTER para continuar...")

    demostrar_encapsulamiento(gestor)
    input("\nPresiona ENTER para continuar...")

    demostrar_polimorfismo(gestor)
    input("\nPresiona ENTER para continuar al menú principal...")

    # Menú interactivo
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            # Ver todos los servicios
            print("TODOS LOS SERVICIOS")
            for servicio in gestor._servicios:
                print(servicio.mostrar_info())
            input("\nPresiona ENTER para continuar...")

        elif opcion == "2":
            # Ver servicios disponibles
            disponibles = gestor.listar_servicios_disponibles()
            print("SERVICIOS DISPONIBLES")
            if disponibles:
                for serv in disponibles:
                    print(f"\n{serv}")
            else:
                print("\nNo hay servicios disponibles en este momento.")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "3":
            # Realizar venta
            print("REALIZAR VENTA")
            print("\nServicios disponibles:")
            for i, serv in enumerate(gestor._servicios, 1):
                print(f"{i}. {serv.codigo} - {serv.nombre}")

            print("\nClientes registrados:")
            for i, cli in enumerate(gestor._clientes, 1):
                print(f"{i}. {cli.cedula} - {cli.nombre_completo()}")

            codigo = input("\nIngresa el código del servicio: ")
            cedula = input("Ingresa la cédula del cliente: ")
            try:
                cantidad = int(input("Ingresa la cantidad de entradas: "))
                gestor.realizar_venta(codigo, cedula, cantidad)
            except ValueError:
                print("   Cantidad inválida")

            input("\nPresiona ENTER para continuar...")

        elif opcion == "4":
            # Ver clientes
            print("CLIENTES REGISTRADOS")
            for cliente in gestor._clientes:
                print(cliente.mostrar_info())
            input("\nPresiona ENTER para continuar...")

        elif opcion == "5":
            # Generar reporte (Polimorfismo)
            print("\n Usando método polimórfico generar_reporte_servicios()...")
            reporte = gestor.generar_reporte_servicios(gestor._servicios)
            print(reporte)
            input("\nPresiona ENTER para continuar...")

        elif opcion == "6":
            # Calcular ingresos (Polimorfismo)
            print("\n Usando método polimórfico calcular_ingresos_totales()...")
            ingresos = gestor.calcular_ingresos_totales(gestor._servicios)
            print(f"\n INGRESOS TOTALES CALCULADOS: ${ingresos:,.2f}")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "7":
            # Ver estadísticas
            print(gestor.obtener_estadisticas())
            input("\nPresiona ENTER para continuar...")

        elif opcion == "8":
            # Salir
            print("\n" + "=" * 70)
            print("¡Gracias por usar el Sistema de Gestión de Cine/Eventos!")
            print("=" * 70)
            break

        else:
            print("\n Opción no válida. Intenta de nuevo.")
            input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    main()