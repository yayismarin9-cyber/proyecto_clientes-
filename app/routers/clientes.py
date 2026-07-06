from fastapi import APIRouter, HTTPException
from app.models.cliente import Cliente
from app.schemas import ClienteSchema

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

clientes = []


@router.get("/")
def obtener_clientes():
    return clientes


@router.post("/")
def crear_cliente(datos: ClienteSchema):
    cliente = Cliente(
        datos.id,
        datos.nombre,
        datos.correo
    )

    clientes.append(cliente.__dict__)

    return {
        "mensaje": "Cliente creado",
        "cliente": cliente.__dict__
    }


@router.put("/{id}")
def actualizar_cliente(id: int, datos: ClienteSchema):
    for cliente in clientes:
        if cliente["id"] == id:
            cliente["nombre"] = datos.nombre
            cliente["correo"] = datos.correo

            return {
                "mensaje": "Cliente actualizado",
                "cliente": cliente
            }

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@router.delete("/{id}")
def eliminar_cliente(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")