from fastapi import FastAPI
from app.routers import clientes, factura, transaccion

app = FastAPI(
    title="API Facturación",
    version="1.0"
)

app.include_router(clientes.router)
app.include_router(factura.router)
app.include_router(transaccion.router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a la API de Facturación"
    }