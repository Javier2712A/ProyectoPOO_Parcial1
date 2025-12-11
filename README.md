#  Sistema de Gestión de Servicios de Cine/Eventos

##  Información del Proyecto

**Asignatura:** Programación Orientada a Objetos  
**Proyecto:** Primer Parcial  
**Grupo:** 9 - Gestión de Servicios de Cine/Eventos  

###  Integrantes
 - [Agusto Gómez Javier Rodolfo]
 - [Castillo Sánchez Marco Elías]
 - [Santamaría Cevallos Viviana Sofía]
 - [Luis Miguel Soriano Arias]


---

##  Descripción del Proyecto

Sistema completo de gestión para servicios de cine y eventos especiales que implementa los conceptos fundamentales de Programación Orientada a Objetos:

- **Herencia:** Estructura jerárquica con una superclase `Servicio` y dos subclases `ServicioCine` y `ServicioEvento`
- **Encapsulamiento:** Todos los atributos son privados con acceso controlado mediante `@property` y validaciones
- **Polimorfismo:** Métodos que operan sobre listas de objetos de la superclase sin verificar tipos específicos

---

##  Estructura del Proyecto

```
ProyectoPOO_Parcial1/
│
├── servicio.py              # Clase base abstracta Servicio
├── servicio_cine.py         # Clase hija ServicioCine
├── servicio_evento.py       # Clase hija ServicioEvento
├── cliente.py               # Clase adicional Cliente
├── gestor_servicios.py      # Clase adicional GestorServicios
├── main.py                  # Programa principal integrador
└── README.md                # Este archivo
```

---

##  Conceptos POO Implementados

###  Herencia

**Diagrama de Clases:**

```
              Servicio (ABC)
                   |
        ┌──────────┴──────────┐
        |                     |
  ServicioCine        ServicioEvento
```

- **Servicio (Superclase):** Clase abstracta base que define atributos y métodos comunes
  - Atributos: `codigo`, `nombre`, `fecha`, `precio_base`, `estado`
  - Métodos abstractos: `calcular_precio_total()`, `mostrar_info()`

- **ServicioCine (Subclase):** Hereda de Servicio y agrega:
  - Atributos: `pelicula`, `sala`, `es_3d`, `es_vip`, `asientos_vendidos`
  - Implementa cálculo de precio con recargos por 3D/VIP y descuentos matine

- **ServicioEvento (Subclase):** Hereda de Servicio y agrega:
  - Atributos: `artista`, `tipo_evento`, `duracion_horas`, `zona`, `entradas_vendidas`
  - Implementa cálculo de precio con recargos por zona y meet & greet

###  Encapsulamiento

 **Todos los atributos son privados** (prefijo `_`)  
 **Acceso controlado mediante `@property`**  
 **Modificación mediante `@setter` con validaciones**

**Ejemplo:**
```python
@property
def precio_base(self) -> float:
    return self._precio_base

@precio_base.setter
def precio_base(self, valor: float):
    if valor < 0:
        raise ValueError("El precio no puede ser negativo")
    self._precio_base = valor
```

###  Polimorfismo

El sistema implementa **2 métodos polimórficos obligatorios** en `GestorServicios`:

#### Método 1: `calcular_ingresos_totales(servicios: List[Servicio])`
Calcula ingresos totales de una lista de servicios sin importar si son de cine o eventos.

```python
def calcular_ingresos_totales(self, servicios: List[Servicio]) -> float:
    total = 0.0
    for servicio in servicios:
        # Polimorfismo: funciona con ServicioCine y ServicioEvento
        precio = servicio.calcular_precio_total()
        # ... resto del cálculo
    return total
```

#### Método 2: `generar_reporte_servicios(servicios: List[Servicio])`
Genera reportes detallados llamando a `mostrar_info()` de cada servicio.

```python
def generar_reporte_servicios(self, servicios: List[Servicio]) -> str:
    for servicio in servicios:
        # Polimorfismo: cada clase implementa su propia versión
        reporte += servicio.mostrar_info()
    return reporte
```

---

##  Instrucciones de Ejecución

### Requisitos Previos
- Python 3.8 o superior
- Ninguna librería externa requerida (solo librerías estándar)

### Ejecutar el Programa Principal

```bash
python main.py
```

### Ejecutar Pruebas Individuales de Cada Módulo

```bash
# Probar clase Servicio
python servicio.py

# Probar ServicioCine
python servicio_cine.py

# Probar ServicioEvento
python servicio_evento.py

# Probar Cliente
python cliente.py

# Probar GestorServicios
python gestor_servicios.py
```

---

##  Funcionalidades del Sistema

### Menú Principal

1. **Ver todos los servicios** - Lista completa de funciones de cine y eventos
2. **Ver servicios disponibles** - Solo servicios con estado "Disponible"
3. **Realizar venta** - Proceso de venta de entradas a clientes
4. **Ver clientes** - Información de clientes registrados
5. **Generar reporte completo** - Usa método polimórfico para reportes
6. **Calcular ingresos totales** - Usa método polimórfico para cálculos
7. **Ver estadísticas** - Resumen general del sistema
8. **Salir** - Terminar el programa

### Características Destacadas

 **Gestión de Cine:**
- Funciones regulares, 3D y VIP
- Descuentos automáticos para funciones matine
- Control de ocupación de salas

 **Gestión de Eventos:**
- Conciertos, obras de teatro, stand-up comedy, ópera, ballet
- Zonas: General, Preferencial, VIP
- Opción de meet & greet con artistas

 **Sistema de Clientes:**
- Registro completo de datos
- Programa de fidelidad (clientes premium)
- Descuentos especiales (15% para premium)
- Acumulación de puntos

 **Gestión Centralizada:**
- Control total de servicios y clientes
- Reportes automáticos
- Estadísticas en tiempo real
- Sistema de ventas integrado

---

##  Ejemplos de Uso

### Crear un Servicio de Cine

```python
cine = ServicioCine(
    codigo="C001",
    nombre="Estreno de la Semana",
    fecha=datetime(2024, 12, 15, 20, 30),
    precio_base=8.50,
    pelicula="Dune: Part Two",
    sala=1,
    es_3d=True,
    es_vip=False
)
```

### Crear un Evento

```python
evento = ServicioEvento(
    codigo="E001",
    nombre="Rock en Vivo",
    fecha=datetime(2024, 12, 20, 20, 0),
    precio_base=45.00,
    artista="Los Rockeros",
    tipo_evento="Concierto",
    duracion_horas=2.5,
    zona="VIP"
)
```

### Demostrar Polimorfismo

```python
servicios = [cine1, cine2, evento1, evento2]  # Lista mixta

# Método polimórfico 1
ingresos = gestor.calcular_ingresos_totales(servicios)

# Método polimórfico 2
reporte = gestor.generar_reporte_servicios(servicios)
```

---

##  Evidencias

### Capturas de Pantalla

![Ejecución del programa mostrando fecha y hora del sistema]
<img width="1600" height="900" alt="Captura de pantalla 2025-12-10 223535" src="https://github.com/user-attachments/assets/ebfa3a55-96d5-4d16-94b8-1f077eccecf1" />
<img width="1594" height="356" alt="Captura de pantalla 2025-12-10 223850" src="https://github.com/user-attachments/assets/59b336d8-61f6-4f4b-85bc-890c5fd9a81d" />


### Video Explicativo

 **Link al video:** [URL del video en Google Drive/YouTube]

**Duración:** ≤ 2 minutos

**Contenido del video:**
1. Explicación de las 5 clases creadas
2. Demostración de herencia
3. Demostración de encapsulamiento (properties)
4. Demostración de polimorfismo (2 métodos)
5. Ejecución final del programa

---

##  Checklist de Requisitos Cumplidos

-  Mínimo 5 clases implementadas
-  1 superclase (Servicio)
-  2 subclases que heredan (ServicioCine, ServicioEvento)
-  2 clases adicionales (Cliente, GestorServicios)
-  Todos los atributos privados con `_`
-  `@property` y `@setter` en todas las clases
-  Validaciones en todos los setters
-  2 métodos polimórficos obligatorios
-  Nombres en snake_case (archivos y variables)
-  Clases en PascalCase
-  Código con PEP8
-  Comentarios claros y docstrings
-  Programa main.py funcional
-  Main de prueba en cada módulo
-  README completo
-  Capturas de pantalla con fecha/hora
-  Video explicativo

---

##  Conceptos Clave Demostrados

### Herencia
- Reutilización de código
- Jerarquía de clases
- Métodos abstractos
- Super() para llamar al constructor padre

### Encapsulamiento
- Atributos privados
- Getters y setters
- Validación de datos
- Protección de la integridad de datos

### Polimorfismo
- Métodos que trabajan con la superclase
- Comportamiento específico en cada subclase
- Duck typing de Python
- Listas heterogéneas de objetos

---

##  Notas Adicionales

- El código sigue las convenciones PEP8
- Cada archivo tiene su propio main de prueba
- El sistema es completamente funcional e interactivo
- Se incluyen validaciones robustas en todas las clases
- Los comentarios explican la lógica de negocio

---

**Fecha de entrega:** 10 / 12 / 2025 
**Institución:** Universidad estatal de Guayaquil 
**Docente:** Guillermo Valarezo Guzmán
