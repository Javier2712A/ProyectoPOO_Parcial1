# ProyectoPOO_Parcial1
# Sistema de Gestión de Servicios de Cine y Eventos

## Descripción

Sistema orientado a objetos para la gestión de servicios de cine y eventos especiales. Implementa conceptos fundamentales de POO como **encapsulamiento**, **herencia** y **polimorfismo** en Python.

---

## Autores

- Agusto Gómez Javier Rodolfo
- Castillo Sánchez Marco Elías
- Santamaría Cevallos Viviana Sofía
- Luis Miguel Soriano Arias

**Fecha:** 7/12/2025

---

## Arquitectura del Sistema

### Diagrama de Clases

```
Cliente                    Servicio (Clase Base)
   |                            |
   |                    +-------+-------+
   |                    |               |
   |            ProyeccionCine    EventoEspecial
   |
   +----> GestorServicios
```

---

## Estructura del Proyecto

```
proyecto/
│
├── Cliente.py              # Clase Cliente con encapsulamiento
├── Servicio.py            # Clase base para servicios
├── ProyeccionCine.py      # Servicio de proyección de películas
├── EventoEspecial.py      # Servicio de eventos especiales
├── GestorServicios.py     # Gestor polimórfico de servicios
└── Main.py                # Archivo principal de pruebas
```

---

## Componentes del Sistema

### 1. **Cliente** (`Cliente.py`)
Representa un cliente de la organización.

**Atributos:**
- `id_cliente`: Identificador único del cliente
- `nombre_completo`: Nombre completo del cliente (mínimo 3 caracteres)

**Características:**
- Encapsulamiento con properties
- Validaciones de datos
- Getters y setters

### 2. **Servicio** (`Servicio.py`)
Clase base abstracta para todos los servicios.

**Atributos:**
- `id_servicio`: Identificador del servicio
- `precio_base`: Precio base del servicio (≥ $1.00)

**Métodos principales:**
- `calcular_costo_final()`: Método polimórfico para calcular el costo
- `mostrar_info()`: Información básica del servicio

**Constantes:**
- `VALOR_MINIMO_PRECIO = 1.0`

### 3. **ProyeccionCine** (`ProyeccionCine.py`)
Hereda de `Servicio`. Representa proyecciones de películas.

**Atributos adicionales:**
- `descuento_aplicable`: Porcentaje de descuento (0.0 - 1.0)
- `nombre_pelicula`: Nombre de la película

**Cálculo de costo:**
```python
costo_final = precio_base × (1 - descuento_aplicable)
```

### 4. **EventoEspecial** (`EventoEspecial.py`)
Hereda de `Servicio`. Representa eventos especiales (conciertos, torneos, etc.).

**Atributos adicionales:**
- `cargo_logistica`: Cargo adicional por logística (≥ $5.00)
- `nombre_evento`: Nombre del evento

**Cálculo de costo:**
```python
costo_final = precio_base + cargo_logistica
```

**Constantes:**
- `CARGO_MINIMO_LOGISTICA = 5.0`

### 5. **GestorServicios** (`GestorServicios.py`)
Gestiona colecciones de servicios de forma polimórfica.

**Métodos principales:**
- `agregar_servicio()`: Agrega un servicio a la lista
- `sumar_costos_totales()`: Suma polimórfica de costos
- `generar_reporte_detallado()`: Genera reporte usando `__str__` de cada servicio

---

## Uso del Sistema

### Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd proyecto

# No requiere instalación de dependencias (Python estándar)
```

### Ejecución

```bash
# Ejecutar todas las pruebas
python Main.py

# Ejecutar módulos individuales
python Cliente.py
python Servicio.py
python ProyeccionCine.py
python EventoEspecial.py
python GestorServicios.py
```

### Ejemplo de Uso

```python
from Cliente import Cliente
from ProyeccionCine import ProyeccionCine
from EventoEspecial import EventoEspecial
from GestorServicios import GestorServicios

# Crear cliente
cliente = Cliente("C001", "Juan Pérez")

# Crear servicios
cine = ProyeccionCine("S101", 15.00, 0.10, "Avatar 2")
evento = EventoEspecial("S205", 50.00, 7.50, "Concierto Rock")

# Gestionar servicios
gestor = GestorServicios()
gestor.agregar_servicio(cine)
gestor.agregar_servicio(evento)

# Calcular total
total = gestor.sumar_costos_totales()
print(f"Total: ${total:.2f}")

# Generar reporte
print(gestor.generar_reporte_detallado())
```

---

## Características Principales

### Encapsulamiento
- Atributos privados con prefijo `_`
- Propiedades (`@property`) para acceso controlado
- Setters con validaciones robustas

### Herencia
- Clase base `Servicio` con lógica común
- Clases derivadas especializadas
- Reutilización de código mediante `super()`

### Polimorfismo
- Método `calcular_costo_final()` sobrescrito en cada clase
- `GestorServicios` opera sin conocer tipos específicos
- Método `__str__()` personalizado por clase

---

## Tests Incluidos

El archivo `Main.py` ejecuta 4 baterías de pruebas:

1. **Test Cliente**: Validaciones de encapsulamiento
2. **Test Servicio Base**: Validaciones de precio mínimo
3. **Test Clases Hijas**: Lógica de cálculo de costos
4. **Test Gestor**: Polimorfismo en acción

**Salida esperada:**
```
Suma Total: $81.00
Validaciones exitosas
Polimorfismo demostrado
```

---

## Ejemplos de Cálculo

### ProyeccionCine
```
Precio Base: $20.00
Descuento: 15%
Costo Final: $20.00 × (1 - 0.15) = $17.00
```

### EventoEspecial
```
Precio Base: $75.00
Cargo Logística: $10.00
Costo Final: $75.00 + $10.00 = $85.00
```

---

## Validaciones Implementadas

| Clase | Atributo | Validación |
|-------|----------|------------|
| Cliente | `nombre_completo` | ≥ 3 caracteres, no vacío |
| Cliente | `id_cliente` | No vacío |
| Servicio | `precio_base` | ≥ $1.00 |
| ProyeccionCine | `descuento_aplicable` | 0.0 ≤ x ≤ 1.0 |
| EventoEspecial | `cargo_logistica` | ≥ $5.00 |

---

## Requisitos

- **Python:** 3.7+
- **Sistema Operativo:** Windows, Linux, macOS
- **Dependencias:** Ninguna (usa biblioteca estándar)

---

## Licencia

Este proyecto es de uso académico y educativo.

---

## Contribuciones

Este es un proyecto académico. Para sugerencias o mejoras, contactar a los autores.

---

## Contacto

Para consultas sobre el proyecto, contactar a través del repositorio de GitHub.

---

**Desarrollado como parte del curso de Programación Orientada a Objetos**
