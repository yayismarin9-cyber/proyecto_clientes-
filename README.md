# 📌 API de Facturación con FastAPI

## 📖 Descripción

Este proyecto consiste en el desarrollo de una API REST para la gestión de clientes, facturas y transacciones utilizando FastAPI.

La aplicación permite realizar operaciones CRUD sobre las entidades principales y almacena la información en una base de datos SQLite utilizando SQLAlchemy como ORM.

---

## 🚀 Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Git
- GitHub

---

## 📁 Estructura del proyecto

```
Proyecto clientes
│
├── app
│   ├── database
│   │   ├── database.py
│   │   └── __init__.py
│   │
│   ├── models
│   │   ├── cliente.py
│   │   ├── factura.py
│   │   └── transaccion.py
│   │
│   ├── routers
│   │   ├── clientes.py
│   │   ├── factura.py
│   │   └── transaccion.py
│   │
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
│
├── facturacion.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/yayismarin9-cyber/proyecto_clientes-.git
```

Ingresar a la carpeta del proyecto:

```bash
cd proyecto_clientes-
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar la aplicación

```bash
python -m uvicorn app.main:app --reload
```

---

## 📚 Documentación de la API

Una vez iniciada la aplicación ingresar a:

```
http://127.0.0.1:8000/docs
```

Allí se encuentra disponible la documentación automática generada por Swagger UI.

---

# Funcionalidades

## Clientes

- Crear cliente
- Consultar clientes
- Actualizar cliente
- Eliminar cliente

## Facturas

- Crear factura
- Consultar facturas
- Actualizar factura
- Eliminar factura
- Calcular total de una factura

## Transacciones

- Crear transacción
- Consultar transacciones
- Actualizar transacción
- Eliminar transacción

---

# Relación de la Base de Datos

```
Cliente
   │
   └──────────< Factura
                    │
                    └──────────< Transacción
```

- Un cliente puede tener muchas facturas.
- Una factura pertenece a un cliente.
- Una factura puede tener muchas transacciones.
- Una transacción pertenece a una factura.

---

# Métodos HTTP utilizados

| Método | Descripción |
|---------|-------------|
| GET | Consultar información |
| POST | Crear registros |
| PUT | Actualizar registros |
| DELETE | Eliminar registros |

---

# Autora

**Cielo Dayanna S.M**

Proyecto desarrollado utilizando FastAPI, SQLAlchemy y SQLite.