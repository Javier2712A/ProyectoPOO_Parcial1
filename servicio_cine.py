# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]


"""
Módulo que define la clase ServicioCine que hereda de Servicio.
Representa funciones de cine con características específicas.
"""

from datetime import datetime
from servicio import Servicio


class ServicioCine(Servicio):
    """
    Clase que representa un servicio de función de cine.
    Hereda de Servicio e implementa sus métodos abstractos.
    """

    # Constantes de la clase
    RECARGO_3D = 3.50
    RECARGO_VIP = 5.00
    DESCUENTO_MATINE = 0.30  # 30% de descuento

    def __init__(self, codigo: str, nombre: str, fecha: datetime, precio_base: float,
                 pelicula: str, sala: int, es_3d: bool = False, es_vip: bool = False):
        """
        Constructor de ServicioCine.

        Args:
            codigo: Código único del servicio
            nombre: Nombre del servicio
            fecha: Fecha y hora de la función
            precio_base: Precio base de la entrada
            pelicula: Nombre de la película
            sala: Número de sala
            es_3d: Si la función es en 3D
            es_vip: Si es sala VIP
        """
        super().__init__(codigo, nombre, fecha, precio_base)
        self._pelicula = pelicula
        self._sala = sala
        self._es_3d = es_3d
        self._es_vip = es_vip
        self._asientos_vendidos = 0
        self._capacidad_total = 100

    # Property para pelicula
    @property
    def pelicula(self) -> str:
        """Obtiene el nombre de la película."""
        return self._pelicula

    @pelicula.setter
    def pelicula(self, valor: str):
        """Establece el nombre de la película con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre de la película debe ser una cadena no vacía")
        self._pelicula = valor

    # Property para sala
    @property
    def sala(self) -> int:
        """Obtiene el número de sala."""
        return self._sala

    @sala.setter
    def sala(self, valor: int):
        """Establece el número de sala con validación."""
        if valor < 1:
            raise ValueError("El número de sala debe ser positivo")
        self._sala = valor

    # Property para es_3d
    @property
    def es_3d(self) -> bool:
        """Indica si la función es en 3D."""
        return self._es_3d

    @es_3d.setter
    def es_3d(self, valor: bool):
        """Establece si la función es 3D."""
        self._es_3d = valor

    # Property para es_vip
    @property
    def es_vip(self) -> bool:
        """Indica si es sala VIP."""
        return self._es_vip

    @es_vip.setter
    def es_vip(self, valor: bool):
        """Establece si es sala VIP."""
        self._es_vip = valor

    # Property para asientos_vendidos
    @property
    def asientos_vendidos(self) -> int:
        """Obtiene la cantidad de asientos vendidos."""
        return self._asientos_vendidos

    @asientos_vendidos.setter
    def asientos_vendidos(self, valor: int):
        """Establece asientos vendidos con validación."""
        if valor < 0 or valor > self._capacidad_total:
            raise ValueError(f"Asientos vendidos debe estar entre 0 y {self._capacidad_total}")
        self._asientos_vendidos = valor

    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total de una entrada considerando recargos y descuentos.

        Returns:
            Precio total calculado
        """
        precio = self._precio_base

        # Agregar recargos
        if self._es_3d:
            precio += self.RECARGO_3D

        if self._es_vip:
            precio += self.RECARGO_VIP

        # Aplicar descuento si es función matine (antes de las 14:00)
        if self._fecha.hour < 14:
            precio *= (1 - self.DESCUENTO_MATINE)

        return round(precio, 2)

    def mostrar_info(self) -> str:
        """
        Muestra información detallada de la función de cine.

        Returns:
            String con la información formateada
        """
        info = f"\n{'=' * 50}\n"
        info += f"FUNCIÓN DE CINE\n"
        info += f"{'=' * 50}\n"
        info += f"Película: {self._pelicula}\n"
        info += f"Código: {self._codigo}\n"
        info += f"Sala: {self._sala}\n"
        info += f"Fecha: {self._fecha.strftime('%d/%m/%Y')}\n"
        info += f"Hora: {self._fecha.strftime('%H:%M')}\n"
        info += f"Formato: {'3D' if self._es_3d else '2D'}\n"
        info += f"Tipo: {'VIP' if self._es_vip else 'Regular'}\n"
        info += f"Precio base: ${self._precio_base:.2f}\n"
        info += f"Precio total: ${self.calcular_precio_total():.2f}\n"
        info += f"Ocupación: {self._asientos_vendidos}/{self._capacidad_total}\n"
        info += f"Estado: {self._estado}\n"
        info += f"{'=' * 50}\n"
        return info

    def vender_entradas(self, cantidad: int) -> bool:
        """
        Vende una cantidad de entradas si hay disponibilidad.

        Args:
            cantidad: Número de entradas a vender

        Returns:
            True si la venta fue exitosa, False en caso contrario
        """
        if cantidad < 1:
            return False

        if self._asientos_vendidos + cantidad <= self._capacidad_total:
            self._asientos_vendidos += cantidad
            if self._asientos_vendidos == self._capacidad_total:
                self._estado = "Agotado"
            return True
        return False


# ============= MAIN DE PRUEBA =============
if __name__ == "__main__":
    print("PRUEBA DE LA CLASE SERVICIO CINE")

    # Crear funciones de cine
    print("\n1. Creando funciones de cine...")
    funcion1 = ServicioCine(
        codigo="C001",
        nombre="Función Regular",
        fecha=datetime(2024, 12, 15, 20, 30),
        precio_base=8.50,
        pelicula="Dune: Part Two",
        sala=1,
        es_3d=False,
        es_vip=False
    )

    funcion2 = ServicioCine(
        codigo="C002",
        nombre="Función 3D VIP",
        fecha=datetime(2024, 12, 15, 21, 0),
        precio_base=8.50,
        pelicula="Avatar 3",
        sala=5,
        es_3d=True,
        es_vip=True
    )

    funcion3 = ServicioCine(
        codigo="C003",
        nombre="Matine Regular",
        fecha=datetime(2024, 12, 16, 11, 0),
        precio_base=8.50,
        pelicula="Oppenheimer",
        sala=3,
        es_3d=False,
        es_vip=False
    )

    print("   Funciones creadas exitosamente")

    # Mostrar información
    print("\n2. Información de las funciones:")
    print(funcion1.mostrar_info())
    print(funcion2.mostrar_info())
    print(funcion3.mostrar_info())

    # Probar venta de entradas
    print("\n3. Probando venta de entradas...")
    print(f"   Vendiendo 45 entradas para {funcion1.pelicula}...")
    if funcion1.vender_entradas(45):
        print(f"   Venta exitosa. Asientos vendidos: {funcion1.asientos_vendidos}")

    print(f"\n   Vendiendo 60 entradas más para {funcion1.pelicula}...")
    if funcion1.vender_entradas(60):
        print(f"   Venta exitosa. Estado: {funcion1.estado}")

    # Probar polimorfismo
    print("\n4. Probando polimorfismo - calcular_precio_total():")
    funciones = [funcion1, funcion2, funcion3]
    for funcion in funciones:
        print(f"   {funcion.pelicula}: ${funcion.calcular_precio_total():.2f}")

    # Probar properties
    print("\n5. Probando encapsulamiento con properties:")
    print(f"   Película original: {funcion1.pelicula}")
    funcion1.pelicula = "Dune: Part Three"
    print(f"   Película modificada: {funcion1.pelicula}")

    # Probar validaciones
    print("\n6. Probando validaciones:")
    try:
        funcion1.sala = -1
    except ValueError as e:
        print(f"   Validación correcta: {e}")