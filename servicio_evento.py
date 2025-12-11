# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]

"""
Módulo que define la clase ServicioEvento que hereda de Servicio.
Representa eventos especiales como conciertos, obras de teatro, etc.
"""

from datetime import datetime
from servicio import Servicio


class ServicioEvento(Servicio):
    """
    Clase que representa un servicio de evento especial.
    Hereda de Servicio e implementa sus métodos abstractos.
    """

    # Constantes de la clase
    TIPOS_EVENTO = ["Concierto", "Obra de Teatro", "Stand-up Comedy", "Opera", "Ballet"]
    RECARGO_ZONA_VIP = 25.00
    RECARGO_ZONA_PREFERENCIAL = 15.00

    def __init__(self, codigo: str, nombre: str, fecha: datetime, precio_base: float,
                 artista: str, tipo_evento: str, duracion_horas: float, zona: str = "General"):
        """
        Constructor de ServicioEvento.

        Args:
            codigo: Código único del servicio
            nombre: Nombre del evento
            fecha: Fecha y hora del evento
            precio_base: Precio base de la entrada
            artista: Nombre del artista o grupo
            tipo_evento: Tipo de evento (Concierto, Teatro, etc.)
            duracion_horas: Duración estimada en horas
            zona: Zona del evento (General, Preferencial, VIP)
        """
        super().__init__(codigo, nombre, fecha, precio_base)
        self._artista = artista
        self._tipo_evento = tipo_evento
        self._duracion_horas = duracion_horas
        self._zona = zona
        self._entradas_vendidas = 0
        self._capacidad_total = 500
        self._incluye_meet_and_greet = False

    # Property para artista
    @property
    def artista(self) -> str:
        """Obtiene el nombre del artista."""
        return self._artista

    @artista.setter
    def artista(self, valor: str):
        """Establece el nombre del artista con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del artista debe ser una cadena no vacía")
        self._artista = valor

    # Property para tipo_evento
    @property
    def tipo_evento(self) -> str:
        """Obtiene el tipo de evento."""
        return self._tipo_evento

    @tipo_evento.setter
    def tipo_evento(self, valor: str):
        """Establece el tipo de evento con validación."""
        if valor not in self.TIPOS_EVENTO:
            raise ValueError(f"Tipo de evento debe ser uno de: {self.TIPOS_EVENTO}")
        self._tipo_evento = valor

    # Property para duracion_horas
    @property
    def duracion_horas(self) -> float:
        """Obtiene la duración del evento en horas."""
        return self._duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor: float):
        """Establece la duración con validación."""
        if valor <= 0:
            raise ValueError("La duración debe ser positiva")
        self._duracion_horas = valor

    # Property para zona
    @property
    def zona(self) -> str:
        """Obtiene la zona del evento."""
        return self._zona

    @zona.setter
    def zona(self, valor: str):
        """Establece la zona con validación."""
        zonas_validas = ["General", "Preferencial", "VIP"]
        if valor not in zonas_validas:
            raise ValueError(f"La zona debe ser una de: {zonas_validas}")
        self._zona = valor

    # Property para entradas_vendidas
    @property
    def entradas_vendidas(self) -> int:
        """Obtiene el número de entradas vendidas."""
        return self._entradas_vendidas

    @entradas_vendidas.setter
    def entradas_vendidas(self, valor: int):
        """Establece entradas vendidas con validación."""
        if valor < 0 or valor > self._capacidad_total:
            raise ValueError(f"Entradas vendidas debe estar entre 0 y {self._capacidad_total}")
        self._entradas_vendidas = valor

    # Property para incluye_meet_and_greet
    @property
    def incluye_meet_and_greet(self) -> bool:
        """Indica si incluye meet and greet."""
        return self._incluye_meet_and_greet

    @incluye_meet_and_greet.setter
    def incluye_meet_and_greet(self, valor: bool):
        """Establece si incluye meet and greet."""
        self._incluye_meet_and_greet = valor

    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total de la entrada considerando zona y extras.

        Returns:
            Precio total calculado
        """
        precio = self._precio_base

        # Agregar recargo por zona
        if self._zona == "VIP":
            precio += self.RECARGO_ZONA_VIP
        elif self._zona == "Preferencial":
            precio += self.RECARGO_ZONA_PREFERENCIAL

        # Recargo adicional por meet and greet
        if self._incluye_meet_and_greet:
            precio += 50.00

        # Descuento por evento de larga duración (más de 3 horas)
        if self._duracion_horas > 3:
            precio *= 1.10  # 10% de recargo por evento largo

        return round(precio, 2)

    def mostrar_info(self) -> str:
        """
        Muestra información detallada del evento.

        Returns:
            String con la información formateada
        """
        info = f"\n{'=' * 50}\n"
        info += f"EVENTO ESPECIAL\n"
        info += f"{'=' * 50}\n"
        info += f"Nombre: {self._nombre}\n"
        info += f"Código: {self._codigo}\n"
        info += f"Tipo: {self._tipo_evento}\n"
        info += f"Artista/Grupo: {self._artista}\n"
        info += f"Fecha: {self._fecha.strftime('%d/%m/%Y')}\n"
        info += f"Hora: {self._fecha.strftime('%H:%M')}\n"
        info += f"Duración: {self._duracion_horas} horas\n"
        info += f"Zona: {self._zona}\n"
        info += f"Precio base: ${self._precio_base:.2f}\n"
        info += f"Precio total: ${self.calcular_precio_total():.2f}\n"
        info += f"Meet & Greet: {'Sí' if self._incluye_meet_and_greet else 'No'}\n"
        info += f"Entradas vendidas: {self._entradas_vendidas}/{self._capacidad_total}\n"
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

        if self._entradas_vendidas + cantidad <= self._capacidad_total:
            self._entradas_vendidas += cantidad
            if self._entradas_vendidas == self._capacidad_total:
                self._estado = "Agotado"
            return True
        return False

    def calcular_ocupacion_porcentaje(self) -> float:
        """
        Calcula el porcentaje de ocupación del evento.

        Returns:
            Porcentaje de ocupación
        """
        return round((self._entradas_vendidas / self._capacidad_total) * 100, 2)


# ============= MAIN DE PRUEBA =============
if __name__ == "__main__":
    print("PRUEBA DE LA CLASE SERVICIO EVENTO")

    # Crear eventos
    print("\n1. Creando eventos especiales...")
    evento1 = ServicioEvento(
        codigo="E001",
        nombre="Rock en Concierto",
        fecha=datetime(2024, 12, 20, 20, 0),
        precio_base=45.00,
        artista="Los Rockeros",
        tipo_evento="Concierto",
        duracion_horas=2.5,
        zona="General"
    )

    evento2 = ServicioEvento(
        codigo="E002",
        nombre="Noche de Opera",
        fecha=datetime(2024, 12, 22, 19, 30),
        precio_base=65.00,
        artista="Compañía Nacional de Opera",
        tipo_evento="Opera",
        duracion_horas=3.5,
        zona="VIP"
    )
    evento2.incluye_meet_and_greet = True

    evento3 = ServicioEvento(
        codigo="E003",
        nombre="Stand-up Night",
        fecha=datetime(2024, 12, 25, 21, 0),
        precio_base=30.00,
        artista="Comediantes Unidos",
        tipo_evento="Stand-up Comedy",
        duracion_horas=2.0,
        zona="Preferencial"
    )

    print("   Eventos creados exitosamente")

    # Mostrar información
    print("\n2. Información de los eventos:")
    print(evento1.mostrar_info())
    print(evento2.mostrar_info())
    print(evento3.mostrar_info())

    # Probar venta de entradas
    print("\n3. Probando venta de entradas...")
    print(f"   Vendiendo 250 entradas para {evento1.nombre}...")
    if evento1.vender_entradas(250):
        print(f"   Venta exitosa. Ocupación: {evento1.calcular_ocupacion_porcentaje()}%")

    print(f"\n   Vendiendo 300 entradas para {evento2.nombre}...")
    if evento2.vender_entradas(300):
        print(f"   Venta exitosa. Ocupación: {evento2.calcular_ocupacion_porcentaje()}%")

    # Probar polimorfismo
    print("\n4. Probando polimorfismo - calcular_precio_total():")
    eventos = [evento1, evento2, evento3]
    for evento in eventos:
        print(f"   {evento.nombre} ({evento.zona}): ${evento.calcular_precio_total():.2f}")

    # Probar properties
    print("\n5. Probando encapsulamiento con properties:")
    print(f"   Artista original: {evento1.artista}")
    evento1.artista = "Super Rockeros"
    print(f"   Artista modificado: {evento1.artista}")

    # Probar validaciones
    print("\n6. Probando validaciones:")
    try:
        evento1.tipo_evento = "Festival"  # Tipo no válido
    except ValueError as e:
        print(f"   Validación correcta: {e}")

    try:
        evento1.duracion_horas = -2  # Duración negativa
    except ValueError as e:
        print(f"   Validación correcta: {e}")