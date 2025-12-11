# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]


"""
Módulo que define la clase base Servicio para el sistema de gestión de cine/eventos.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Servicio(ABC):
    """
    Clase abstracta base que representa un servicio genérico de cine/eventos.
    Implementa encapsulamiento y define métodos polimórficos.
    """

    def __init__(self, codigo: str, nombre: str, fecha: datetime, precio_base: float):
        """
        Constructor de la clase Servicio.

        Args:
            codigo: Código único del servicio
            nombre: Nombre del servicio
            fecha: Fecha y hora del servicio
            precio_base: Precio base del servicio
        """
        self._codigo = codigo
        self._nombre = nombre
        self._fecha = fecha
        self._precio_base = precio_base
        self._estado = "Disponible"

    # Property para codigo
    @property
    def codigo(self) -> str:
        """Obtiene el código del servicio."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str):
        """Establece el código del servicio con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El código debe ser una cadena no vacía")
        self._codigo = valor

    # Property para nombre
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del servicio."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre del servicio con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = valor

    # Property para fecha
    @property
    def fecha(self) -> datetime:
        """Obtiene la fecha del servicio."""
        return self._fecha

    @fecha.setter
    def fecha(self, valor: datetime):
        """Establece la fecha del servicio con validación."""
        if not isinstance(valor, datetime):
            raise ValueError("La fecha debe ser un objeto datetime")
        self._fecha = valor

    # Property para precio_base
    @property
    def precio_base(self) -> float:
        """Obtiene el precio base del servicio."""
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float):
        """Establece el precio base con validación."""
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo")
        self._precio_base = valor

    # Property para estado
    @property
    def estado(self) -> str:
        """Obtiene el estado del servicio."""
        return self._estado

    @estado.setter
    def estado(self, valor: str):
        """Establece el estado del servicio con validación."""
        estados_validos = ["Disponible", "Agotado", "Cancelado", "En proceso"]
        if valor not in estados_validos:
            raise ValueError(f"Estado debe ser uno de: {estados_validos}")
        self._estado = valor

    @abstractmethod
    def calcular_precio_total(self) -> float:
        """
        Método abstracto para calcular el precio total del servicio.
        Debe ser implementado por las clases hijas.
        """
        pass

    @abstractmethod
    def mostrar_info(self) -> str:
        """
        Método abstracto para mostrar información del servicio.
        Debe ser implementado por las clases hijas.
        """
        pass

    def __str__(self) -> str:
        """Representación en string del servicio."""
        return (f"Servicio: {self._nombre} | Código: {self._codigo} | "
                f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M')} | "
                f"Estado: {self._estado}")


# ============= MAIN DE PRUEBA =============
if __name__ == "__main__":
    print("PRUEBA DE LA CLASE SERVICIO (BASE)")

    # No se puede instanciar directamente una clase abstracta
    print("\n1. Intentando crear instancia de clase abstracta...")
    try:
        servicio = Servicio("S001", "Servicio Test", datetime.now(), 10.0)
        print("   ERROR: No debería permitir instanciar")
    except TypeError as e:
        print(f"   Correcto: {e}")

    print("\n2. La clase Servicio es abstracta y define:")
    print("   - Atributos encapsulados: _codigo, _nombre, _fecha, _precio_base, _estado")
    print("   - Properties con validaciones")
    print("   - Métodos abstractos: calcular_precio_total(), mostrar_info()")

    print("\n3. Las clases hijas deberán implementar los métodos abstractos")
