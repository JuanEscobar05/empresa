# 🏢 Sistema de Gestión Empresarial

## 📌 Descripción General

El proyecto **Empresa** es una aplicación de consola desarrollada en **Python**, orientada a la gestión básica de una empresa. El sistema permite administrar **usuarios, vendedores, productos, tiendas y ventas**, aplicando una **estructura tipo MVC (Modelo – Vista – Controlador)** y conexión a base de datos.

Este proyecto demuestra el uso de **programación modular**, separación de responsabilidades y conexión a base de datos, siendo ideal para **presentación académica o entrevista técnica**.

---

## 🎯 Objetivos del Proyecto

* Gestionar usuarios del sistema.
* Administrar vendedores.
* Registrar y visualizar productos.
* Gestionar tiendas.
* Registrar ventas.
* Aplicar el patrón MVC.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Base de datos:** MySQL (mediante conexión)
* **Paradigma:** Programación estructurada / modular
* **Arquitectura:** MVC (Modelo – Vista – Controlador)
* **Entorno:** Consola

---

## 📁 Estructura del Proyecto

```
empresa/
│
├── main.py
│
├── Connection/
│   └── conexion.py
│
├── controllers/
│   ├── controladorProducto.py
│   ├── controladorTienda.py
│   ├── controladorUsuarios.py
│   ├── controladorVendedor.py
│   └── controladorVenta.py
│
├── models/
│   ├── producto.py
│   ├── tienda.py
│   ├── usuario.py
│   ├── vendedor.py
│   └── venta.py
│
├── views/
│   ├── vistaProducto.py
│   ├── vistaTienda.py
│   ├── vistaUsuarios.py
│   ├── vistaVendedor.py
│   └── vistaVenta.py
│
└── modules/
    └── venv/ (entorno virtual)
```

> ⚠️ Nota: La carpeta `modules/` contiene el entorno virtual y no hace parte de la lógica del sistema.

---

## 🧠 Arquitectura MVC

### 📦 Modelo (`models`)

Contiene las clases que representan las entidades del sistema:

* Usuario
* Vendedor
* Producto
* Tienda
* Venta

Cada modelo define los atributos y estructura de los datos.

---

### 🎮 Controlador (`controllers`)

Gestiona la lógica del negocio y conecta el modelo con la vista:

* Crear registros
* Consultar información
* Actualizar datos
* Eliminar registros

Ejemplo:

* `controladorProducto.py` gestiona la lógica relacionada con productos.

---

### 🖥️ Vista (`views`)

Encargada de la interacción con el usuario por consola:

* Mostrar menús
* Solicitar datos
* Mostrar resultados

Ejemplo:

* `vistaProducto.py` muestra las opciones para gestionar productos.

---

### 🔌 Conexión (`Connection`)

**Archivo:** `conexion.py`

* Establece la conexión con la base de datos MySQL.
* Centraliza la configuración de acceso.

---

## ▶️ Ejecución del Sistema

Desde la carpeta raíz:

```bash
python main.py
```

Esto inicia el menú principal del sistema.

---

## 🧭 Flujo del Sistema

1. Inicio del sistema
2. Menú principal
3. Selección del módulo a gestionar:

   * Usuarios
   * Vendedores
   * Productos
   * Tiendas
   * Ventas
4. Ejecución de operaciones CRUD
5. Retorno al menú

---

## 📌 Funcionalidades Principales

### 👤 Gestión de Usuarios

* Registrar usuarios
* Listar usuarios
* Actualizar información
* Eliminar usuarios

### 🧑‍💼 Gestión de Vendedores

* Registrar vendedores
* Consultar vendedores
* Actualizar datos

### 📦 Gestión de Productos

* Registrar productos
* Listar productos
* Actualizar información
* Eliminar productos

### 🏬 Gestión de Tiendas

* Registrar tiendas
* Visualizar tiendas

### 🧾 Gestión de Ventas

* Registrar ventas
* Asociar productos y vendedores
* Consultar ventas

---

## 📈 Ejemplo de Uso

```
===== MENÚ PRINCIPAL =====
1. Usuarios
2. Vendedores
3. Productos
4. Tiendas
5. Ventas
6. Salir
```

---

## 🚀 Mejoras Futuras

* Autenticación y roles (Admin / Vendedor)
* Validaciones de entrada
* Reportes de ventas
* Persistencia optimizada
* Interfaz gráfica o versión web

---

## 👨‍💻 Autor

**Juan Escobar**
Estudiante de Desarrollo de Software

---

## 📄 Licencia

Proyecto de uso académico y educativo.
