# Sistema de Gestión Empresarial en Python

Este proyecto es un **Sistema de Gestión Empresarial** desarrollado en **Python**, diseñado para administrar información de **clientes, productos, vendedores y ventas** mediante operaciones **CRUD** y conexión a una base de datos.

El sistema está estructurado de forma modular, facilitando el mantenimiento, la escalabilidad y la comprensión del código.

---

## Características Principales

- Conexión centralizada a base de datos
- Operaciones CRUD completas
- Separación clara de responsabilidades
- Arquitectura modular
- Fácil extensión a nuevas entidades
- Orientado a proyectos académicos y administrativos

---

## Estructura del Proyecto

```text
empresa-main/
├── 📁 Connection/
│   ├── 📁 __pycache__/
│   └── 📄 db.py
│
├── 📁 Crd/
│   ├── 📁 __pycache__/
│   ├── 📄 crudCliente.py
│   ├── 📄 crudProducto.py
│   ├── 📄 crudVendedor.py
│   └── 📄 crudVenta.py
│
├── 📁 modules/
│   ├── 📁 Lib/
│   └── ⚙️ pyvenv.cfg
│
├── 📁 Table/
│   ├── 📁 __pycache__/
│   ├── 📄 TablaCliente.py
│   ├── 📄 TablaProducto.py
│   ├── 📄 TablaVendedor.py
│   ├── 📄 TablaVenta.py
│   └── 📄 main.py
````

---

##  Descripción de Carpetas y Archivos

### Connection

Contiene la lógica relacionada con la conexión a la base de datos.

* **db.py**
  Archivo encargado de establecer y administrar la conexión a la base de datos, reutilizable por los demás módulos del sistema.

---

### Crd (CRUD)

Incluye los módulos que implementan las operaciones **Crear, Leer, Actualizar y Eliminar** para cada entidad.

* **crudCliente.py** → Gestión de clientes
* **crudProducto.py** → Gestión de productos
* **crudVendedor.py** → Gestión de vendedores
* **crudVenta.py** → Gestión de ventas

Cada archivo encapsula la lógica de negocio específica de su entidad.

---

### modules

Carpeta correspondiente al **entorno virtual de Python**.

* **Lib/** → Librerías instaladas
* **pyvenv.cfg** → Configuración del entorno virtual

> ⚠️ No se recomienda modificar esta carpeta manualmente.

---

### Table

Define las estructuras de las tablas y coordina la ejecución del sistema.

* **TablaCliente.py** → Definición de la tabla clientes
* **TablaProducto.py** → Definición de la tabla productos
* **TablaVendedor.py** → Definición de la tabla vendedores
* **TablaVenta.py** → Definición de la tabla ventas
* **main.py** → Archivo principal desde donde se ejecuta la aplicación

---

## Ejecución del Proyecto

1. Asegúrese de tener **Python 3** instalado.
2. Active el entorno virtual (si aplica).
3. Desde la raíz del proyecto ejecute:

```bash
python Table/main.py
```

---

## Tecnologías Utilizadas

* Python 3
* Base de datos relacional
* Programación modular
* Arquitectura CRUD

---

## Posibles Mejoras

* Implementar interfaz gráfica o web
* Agregar validaciones de datos
* Manejo de excepciones avanzado
* Implementar patrón MVC
* Integración con frameworks como Flask o Django

---

## Licencia

Este proyecto es de uso **académico y educativo**.

---

## Autor

Desarrollado por **Juan**


