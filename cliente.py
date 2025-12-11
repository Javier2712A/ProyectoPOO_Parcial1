# Integrantes:
# - [Agusto Gómez Javier Rodolfo]
# - [Castillo Sánchez Marco Elías]
# - [Santamaría Cevallos Viviana Sofía]
# - [Luis Miguel Soriano Arias]


"""
Módulo que define la clase Cliente para el sistema de gestión de cine/eventos.
Representa a los clientes que compran servicios.
"""


class Cliente:
    """
    Clase que representa a un cliente del sistema de cine/eventos.
    Implementa encapsulamiento y manejo de compras.
    """

    # Constantes de la clase
    DESCUENTO_PREMIUM = 0.15  # 15% de descuento
    COMPRAS_PARA_PREMIUM = 5

    def __init__(self, cedula: str, nombre: str, apellido: str, email: str, telefono: str):
        """
        Constructor de la clase Cliente.

        Args:
            cedula: Número de cédula del cliente
            nombre: Nombre del cliente
            apellido: Apellido del cliente
            email: Correo electrónico
            telefono: Número de teléfono
        """
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._es_premium = False
        self._historial_compras = []
        self._puntos_acumulados = 0

    # Property para cedula
    @property
    def cedula(self) -> str:
        """Obtiene la cédula del cliente."""
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str):
        """Establece la cédula con validación."""
        if not valor or len(valor) < 10:
            raise ValueError("La cédula debe tener al menos 10 caracteres")
        self._cedula = valor

    # Property para nombre
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = valor

    # Property para apellido
    @property
    def apellido(self) -> str:
        """Obtiene el apellido del cliente."""
        return self._apellido

    @apellido.setter
    def apellido(self, valor: str):
        """Establece el apellido con validación."""
        if not valor or not isinstance(valor, str):
            raise ValueError("El apellido debe ser una cadena no vacía")
        self._apellido = valor

    # Property para email
    @property
    def email(self) -> str:
        """Obtiene el email del cliente."""
        return self._email

    @email.setter
    def email(self, valor: str):
        """Establece el email con validación."""
        if not valor or "@" not in valor:
            raise ValueError("El email debe ser válido y contener @")
        self._email = valor

    # Property para telefono
    @property
    def telefono(self) -> str:
        """Obtiene el teléfono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        """Establece el teléfono con validación."""
        if not valor or len(valor) < 10:
            raise ValueError("El teléfono debe tener al menos 10 dígitos")
        self._telefono = valor

    # Property para es_premium
    @property
    def es_premium(self) -> bool:
        """Indica si el cliente es premium."""
        return self._es_premium

    @es_premium.setter
    def es_premium(self, valor: bool):
        """Establece el estado premium del cliente."""
        self._es_premium = valor

    # Property para puntos_acumulados
    @property
    def puntos_acumulados(self) -> int:
        """Obtiene los puntos acumulados del cliente."""
        return self._puntos_acumulados

    @puntos_acumulados.setter
    def puntos_acumulados(self, valor: int):
        """Establece los puntos acumulados con validación."""
        if valor < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_acumulados = valor

    def registrar_compra(self, servicio, cantidad_entradas: int, precio_total: float):
        """
        Registra una compra en el historial del cliente.

        Args:
            servicio: Objeto del servicio comprado
            cantidad_entradas: Número de entradas compradas
            precio_total: Monto total pagado
        """
        compra = {
            "servicio": servicio.nombre,
            "codigo": servicio.codigo,
            "cantidad": cantidad_entradas,
            "total": precio_total,
            "fecha": servicio.fecha
        }
        self._historial_compras.append(compra)

        # Acumular puntos (1 punto por cada dólar gastado)
        self._puntos_acumulados += int(precio_total)

        # Verificar si califica para premium
        if len(self._historial_compras) >= self.COMPRAS_PARA_PREMIUM and not self._es_premium:
            self._es_premium = True
            print(f"   ¡Felicitaciones! {self.nombre_completo()} ahora es cliente PREMIUM")

    def nombre_completo(self) -> str:
        """
        Obtiene el nombre completo del cliente.

        Returns:
            Nombre y apellido concatenados
        """
        return f"{self._nombre} {self._apellido}"

    def obtener_historial(self) -> list:
        """
        Obtiene el historial de compras del cliente.

        Returns:
            Lista de compras realizadas
        """
        return self._historial_compras.copy()

    def calcular_descuento(self, precio: float) -> float:
        """
        Calcula el descuento aplicable al precio según el tipo de cliente.

        Args:
            precio: Precio original

        Returns:
            Precio con descuento aplicado
        """
        if self._es_premium:
            return precio * (1 - self.DESCUENTO_PREMIUM)
        return precio

    def mostrar_info(self) -> str:
        """
        Muestra la información del cliente.

        Returns:
            String con la información formateada
        """
        info = f"\n{'=' * 50}\n"
        info += f"INFORMACIÓN DEL CLIENTE\n"
        info += f"{'=' * 50}\n"
        info += f"Cédula: {self._cedula}\n"
        info += f"Nombre: {self.nombre_completo()}\n"
        info += f"Email: {self._email}\n"
        info += f"Teléfono: {self._telefono}\n"
        info += f"Tipo: {'PREMIUM' if self._es_premium else 'Regular'}\n"
        info += f"Puntos acumulados: {self._puntos_acumulados}\n"
        info += f"Compras realizadas: {len(self._historial_compras)}\n"
        info += f"{'=' * 50}\n"
        return info

    def __str__(self) -> str:
        """Representación en string del cliente."""
        tipo = "PREMIUM" if self._es_premium else "Regular"
        return f"Cliente: {self.nombre_completo()} | Cédula: {self._cedula} | Tipo: {tipo}"


# ============= MAIN DE PRUEBA =============
if __name__ == "__main__":
    print("PRUEBA DE LA CLASE CLIENTE")

    # Crear clientes
    print("\n1. Creando clientes...")
    cliente1 = Cliente(
        cedula="0912345678",
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@email.com",
        telefono="0987654321"
    )

    cliente2 = Cliente(
        cedula="0923456789",
        nombre="María",
        apellido="González",
        email="maria.gonzalez@email.com",
        telefono="0976543210"
    )

    print("   Clientes creados exitosamente")

    # Mostrar información
    print("\n2. Información de los clientes:")
    print(cliente1.mostrar_info())
    print(cliente2.mostrar_info())

    # Simular compras
    print("\n3. Simulando compras...")


    # Crear un servicio simulado para las compras
    class ServicioSimulado:
        def __init__(self, nombre, codigo, fecha):
            self.nombre = nombre
            self.codigo = codigo
            self.fecha = fecha


    from datetime import datetime

    servicio_sim = ServicioSimulado("Película Test", "C001", datetime.now())

    # Registrar múltiples compras para cliente1
    for i in range(6):
        cliente1.registrar_compra(servicio_sim, 2, 25.50)
        print(f"   Compra {i + 1} registrada para {cliente1.nombre}")

    # Una compra para cliente2
    cliente2.registrar_compra(servicio_sim, 1, 15.00)

    print("\n4. Estado actualizado de los clientes:")
    print(cliente1)
    print(cliente2)

    # Probar cálculo de descuento
    print("\n5. Probando cálculo de descuentos:")
    precio_original = 100.00
    print(f"   Precio original: ${precio_original:.2f}")
    print(f"   Precio para {cliente1.nombre} (Premium): ${cliente1.calcular_descuento(precio_original):.2f}")
    print(f"   Precio para {cliente2.nombre} (Regular): ${cliente2.calcular_descuento(precio_original):.2f}")

    # Probar properties
    print("\n6. Probando encapsulamiento con properties:")
    print(f"   Email original: {cliente1.email}")
    cliente1.email = "nuevo.email@email.com"
    print(f"   Email modificado: {cliente1.email}")

    # Probar validaciones
    print("\n7. Probando validaciones:")
    try:
        cliente1.email = "email_invalido"
    except ValueError as e:
        print(f"   Validación correcta: {e}")

    try:
        cliente1.puntos_acumulados = -100
    except ValueError as e:
        print(f"   Validación correcta: {e}")

    # Mostrar historial
    print("\n8. Historial de compras de cliente1:")
    historial = cliente1.obtener_historial()
    print(f"   Total de compras: {len(historial)}")
