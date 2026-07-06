from fastapi import APIRouter, HTTPException
from app.models.factura import Factura
from app.schemas import FacturaSchema

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)

facturas = []


@router.get("/")
def obtener_facturas():
    return facturas


@router.post("/")
def crear_factura(datos: FacturaSchema):
    factura = Factura(
        datos.id,
        datos.fecha,
        datos.cliente
    )

    facturas.append(factura.__dict__)

    return {
        "mensaje": "Factura creada",
        "factura": factura.__dict__
    }


@router.put("/{id}")
def actualizar_factura(id: int, datos: FacturaSchema):
    for factura in facturas:
        if factura["id"] == id:
            factura["fecha"] = datos.fecha
            factura["cliente"] = datos.cliente

            return {
                "mensaje": "Factura actualizada",
                "factura": factura
            }

    raise HTTPException(status_code=404, detail="Factura no encontrada")


@router.delete("/{id}")
def eliminar_factura(id: int):
    for factura in facturas:
        if factura["id"] == id:
            facturas.remove(factura)
            return {"mensaje": "Factura eliminada"}

    raise HTTPException(status_code=404, detail="Factura no encontrada")

@router.get("/{id}/total")
def obtener_total_factura(id: int):
    for factura in facturas:
        if factura["id"] == id:
            total = 0

            from app.routers.transaccion import transacciones

            for transaccion in transacciones:
                if transaccion["factura_id"] == id:
                    total += (
                        transaccion["valor_unitario"]
                        * transaccion["cantidad"]
                    )

            return {
                "factura": id,
                "total": total
            }

    raise HTTPException(status_code=404, detail="Factura no encontrada")