from fastapi import APIRouter, HTTPException
from app.models.transaccion import Transaccion
from app.schemas import TransaccionSchema

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)

transacciones = []


@router.get("/")
def obtener_transacciones():
    return transacciones


@router.post("/")
def crear_transaccion(datos: TransaccionSchema):
    transaccion = Transaccion(
        datos.id,
        datos.valor_unitario,
        datos.cantidad,
        datos.factura_id
    )

    transacciones.append(transaccion.__dict__)

    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion.__dict__
    }


@router.put("/{id}")
def actualizar_transaccion(id: int, datos: TransaccionSchema):
    for transaccion in transacciones:
        if transaccion["id"] == id:
            transaccion["valor_unitario"] = datos.valor_unitario
            transaccion["cantidad"] = datos.cantidad
            transaccion["factura_id"] = datos.factura_id

            return {
                "mensaje": "Transacción actualizada",
                "transaccion": transaccion
            }

    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.delete("/{id}")
def eliminar_transaccion(id: int):
    for transaccion in transacciones:
        if transaccion["id"] == id:
            transacciones.remove(transaccion)
            return {"mensaje": "Transacción eliminada"}

    raise HTTPException(status_code=404, detail="Transacción no encontrada")