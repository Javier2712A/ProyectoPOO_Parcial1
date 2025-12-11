# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]

"""
Módulo que define la clase GestorServicios para el sistema de cine/eventos.
Gestiona servicios y clientes, implementa métodos polimórficos.
"""

from datetime import datetime
from typing import List
from servicio import Servicio
from cliente import Cliente


class GestorServicios:
    """
    Clase que gestiona servicios y clientes del sistema.
    Implementa métodos polimórficos para operaciones sobre listas de servicios.
    """

    def __init__(self, nombre_empresa: str):
        """
        Constructor del GestorServicios.

        Args:
            nombre_empresa: Nombre de la empresa de cine/eventos
        """
        self._nombre_empresa = nombre_empresa
        self._servicios = []
        self._clientes = []
        self._ventas_totales = 0.0
        self._fecha_creacion = datetime.now()

    # Property para nombre_empresa
    @property
    def nombre_empresa(self) -> str:
        """Obtiene el nombre de la empresa."""
        return self._nombre_empresa

    @nombre_empresa.setter
    def nombre_empresa(self, valor: str):
        """Establece el nombre de la empresa con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre de la empresa debe ser una cadena no vacía")
        self._nombre_empresa = valor

    # Property para ventas_totales
    @property
    def ventas_totales(self) -> float:
        """Obtiene el total de ventas."""
        return self._ventas_totales

    def agregar_servicio(self, servicio: Servicio):
        """
        Agrega un servicio a la lista de servicios.

        Args:
            servicio: Objeto de tipo Servicio (o subclases)
        """
        if not isinstance(servicio, Servicio):
            raise ValueError("Debe ser una instancia de Servicio")
        self._servicios.append(servicio)
        print(f"   Servicio '{servicio.nombre}' agregado exitosamente")

    def agregar_cliente(self, cliente: Cliente):
        """
        Agrega un cliente a la lista de clientes.

        Args:
            cliente: Objeto de tipo Cliente
        """
        if not isinstance(cliente, Cliente):
            raise ValueError("Debe ser una instancia de Cliente")
        self._clientes.append(cliente)
        print(f"   Cliente '{cliente.nombre_completo()}' registrado exitosamente")

    def buscar_servicio(self, codigo: str) -> Servicio:
        """
        Busca un servicio por su código.

        Args:
            codigo: Código del servicio a buscar

        Returns:
            Servicio encontrado o None
        """
        for servicio in self._servicios:
            if servicio.codigo == codigo:
                return servicio
        return None

    def buscar_cliente(self, cedula: str) -> Cliente:
        """
        Busca un cliente por su cédula.

        Args:
            cedula: Cédula del cliente a buscar

        Returns:
            Cliente encontrado o None
        """
        for cliente in self._clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    # ========== MÉTODOS POLIMÓRFICOS (OBLIGATORIOS) ==========

    def calcular_ingresos_totales(self, servicios: List[Servicio]) -> float:
        """
        MÉTODO POLIMÓRFICO 1: Calcula los ingresos totales de una lista de servicios.
        Funciona con cualquier tipo de servicio (Cine o Evento) sin verificar tipo.

        Args:
            servicios: Lista de objetos Servicio

        Returns:
            Total de ingresos calculados
        """
        total = 0.0
        for servicio in servicios:
            # Polimorfismo: llama al método calcular_precio_total()
            # sin importar si es ServicioCine o ServicioEvento
            precio = servicio.calcular_precio_total()

            # Obtener entradas vendidas (asumiendo que tienen este atributo)
            if hasattr(servicio, '_asientos_vendidos'):
                entradas = servicio._asientos_vendidos
            elif hasattr(servicio, '_entradas_vendidas'):
                entradas = servicio._entradas_vendidas
            else:
                entradas = 0

            total += precio * entradas

        return round(total, 2)

    def generar_reporte_servicios(self, servicios: List[Servicio]) -> str:
        """
        MÉTODO POLIMÓRFICO 2: Genera un reporte detallado de una lista de servicios.
        Funciona con cualquier tipo de servicio sin verificar tipo.

        Args:
            servicios: Lista de objetos Servicio

        Returns:
            String con el reporte formateado
        """
        reporte = f"\n{'=' * 70}\n"
        reporte += f"REPORTE DE SERVICIOS - {self._nombre_empresa}\n"
        reporte += f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n"
        reporte += f"{'=' * 70}\n\n"

        if not servicios:
            reporte += "No hay servicios registrados.\n"
            return reporte

        total_ingresos = 0.0

        for i, servicio in enumerate(servicios, 1):
            # Polimorfismo: llama a mostrar_info() sin importar el tipo
            reporte += f"{i}. {servicio.mostrar_info()}\n"

            # Calcular ingresos de este servicio
            precio = servicio.calcular_precio_total()
            if hasattr(servicio, '_asientos_vendidos'):
                entradas = servicio._asientos_vendidos
            elif hasattr(servicio, '_entradas_vendidas'):
                entradas = servicio._entradas_vendidas
            else:
                entradas = 0

            ingresos_servicio = precio * entradas
            total_ingresos += ingresos_servicio
            reporte += f"   Ingresos generados: ${ingresos_servicio:.2f}\n"
            reporte += f"   {'-' * 50}\n"

        reporte += f"\n{'=' * 70}\n"
        reporte += f"TOTAL DE SERVICIOS: {len(servicios)}\n"
        reporte += f"INGRESOS TOTALES: ${total_ingresos:.2f}\n"
        reporte += f"{'=' * 70}\n"

        return reporte

    # ========== MÉTODOS ADICIONALES ==========

    def realizar_venta(self, codigo_servicio: str, cedula_cliente: str, cantidad: int) -> bool:
        """
        Realiza una venta de entradas.

        Args:
            codigo_servicio: Código del servicio
            cedula_cliente: Cédula del cliente
            cantidad: Cantidad de entradas a vender

        Returns:
            True si la venta fue exitosa, False en caso contrario
        """
        servicio = self.buscar_servicio(codigo_servicio)
        cliente = self.buscar_cliente(cedula_cliente)

        if not servicio:
            print(f"   Servicio '{codigo_servicio}' no encontrado")
            return False

        if not cliente:
            print(f"   Cliente con cédula '{cedula_cliente}' no encontrado")
            return False

        # Intentar vender entradas
        if hasattr(servicio, 'vender_entradas'):
            if servicio.vender_entradas(cantidad):
                precio_total = servicio.calcular_precio_total() * cantidad
                precio_final = cliente.calcular_descuento(precio_total)

                cliente.registrar_compra(servicio, cantidad, precio_final)
                self._ventas_totales += precio_final

                print(f"   Venta exitosa!")
                print(f"   Cliente: {cliente.nombre_completo()}")
                print(f"   Servicio: {servicio.nombre}")
                print(f"   Cantidad: {cantidad} entrada(s)")
                print(f"   Total: ${precio_final:.2f}")
                return True
            else:
                print(f"   No hay suficientes entradas disponibles")
                return False
        else:
            print(f"   El servicio no permite venta de entradas")
            return False

    def listar_servicios_disponibles(self) -> List[Servicio]:
        """
        Retorna una lista de servicios disponibles.

        Returns:
            Lista de servicios con estado 'Disponible'
        """
        return [s for s in self._servicios if s.estado == "Disponible"]

    def obtener_estadisticas(self) -> str:
        """
        Genera estadísticas generales del sistema.

        Returns:
            String con las estadísticas
        """
        stats = f"\n{'=' * 60}\n"
        stats += f"ESTADÍSTICAS - {self._nombre_empresa}\n"
        stats += f"{'=' * 60}\n"
        stats += f"Total de servicios: {len(self._servicios)}\n"
        stats += f"Servicios disponibles: {len(self.listar_servicios_disponibles())}\n"
        stats += f"Total de clientes: {len(self._clientes)}\n"

        clientes_premium = sum(1 for c in self._clientes if c.es_premium)
        stats += f"Clientes premium: {clientes_premium}\n"
        stats += f"Ventas totales: ${self._ventas_totales:.2f}\n"

        return stats

    def __str__(self) -> str:
        """Representación en string del gestor."""
        return (f"GestorServicios: {self._nombre_empresa} | "
                f"Servicios: {len(self._servicios)} | "
                f"Clientes: {len(self._clientes)}")


# ============= MAIN DE PRUEBA =============
if __name__ == "__main__":
    from servicio_cine import ServicioCine
    from servicio_evento import ServicioEvento

    print("PRUEBA DE LA CLASE GESTOR SERVICIOS")

    # Crear gestor
    print("\n1. Creando gestor de servicios...")
    gestor = GestorServicios("CineMax Entertainment")
    print(f"   Gestor creado: {gestor}")

    # Crear y agregar servicios
    print("\n2. Agregando servicios...")

    cine1 = ServicioCine("C001", "Estreno", datetime(2024, 12, 15, 20, 0),
                         8.50, "Dune: Part Two", 1, False, False)
    cine1.vender_entradas(50)

    cine2 = ServicioCine("C002", "Función VIP", datetime(2024, 12, 16, 21, 0),
                         8.50, "Avatar 3", 5, True, True)
    cine2.vender_entradas(75)

    evento1 = ServicioEvento("E001", "Rock Concert", datetime(2024, 12, 20, 20, 0),
                             45.00, "Los Rockeros", "Concierto", 2.5, "VIP")
    evento1.vender_entradas(200)

    gestor.agregar_servicio(cine1)
    gestor.agregar_servicio(cine2)
    gestor.agregar_servicio(evento1)

    # Crear y agregar clientes
    print("\n3. Registrando clientes...")

    cliente1 = Cliente("0912345678", "Juan", "Pérez", "juan@email.com", "0987654321")
    cliente2 = Cliente("0923456789", "María", "González", "maria@email.com", "0976543210")

    gestor.agregar_cliente(cliente1)
    gestor.agregar_cliente(cliente2)

    # Probar MÉTODO POLIMÓRFICO 1: calcular_ingresos_totales
    print("\n4. PROBANDO POLIMORFISMO 1 - Calcular ingresos totales:")
    print("   (Funciona con lista mixta de ServicioCine y ServicioEvento)")

    todos_servicios = [cine1, cine2, evento1]
    ingresos = gestor.calcular_ingresos_totales(todos_servicios)
    print(f"\n  Ingresos totales calculados: ${ingresos:.2f}")

    # Probar MÉTODO POLIMÓRFICO 2: generar_reporte_servicios
    print("\n5. PROBANDO POLIMORFISMO 2 - Generar reporte:")
    print(" (Genera reporte de cualquier tipo de servicio)")

    reporte = gestor.generar_reporte_servicios(todos_servicios)
    print(reporte)

    # Realizar ventas
    print("\n6. Realizando ventas...")
    gestor.realizar_venta("C001", "0912345678", 2)
    print()
    gestor.realizar_venta("E001", "0923456789", 3)

    # Obtener estadísticas
    print("\n7. Estadísticas del sistema:")
    print(gestor.obtener_estadisticas())

    # Probar búsqueda
    print("\n8. Probando búsqueda de servicios...")
    servicio_encontrado = gestor.buscar_servicio("C001")
    if servicio_encontrado:
        print(f"   Servicio encontrado: {servicio_encontrado}")
