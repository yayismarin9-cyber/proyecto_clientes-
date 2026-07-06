from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.transaccion import Transaccion
from app.models.factura import Factura
from app.schemas import TransaccionSchema, TransaccionResponse

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


@router.get("/", response_model=list[TransaccionResponse])
def obtener_transacciones(db: Session = Depends(get_db)):
    return db.query(Transaccion).all()


@router.post("/", response_model=TransaccionResponse)
def crear_transaccion(datos: TransaccionSchema, db: Session = Depends(get_db)):

    factura = db.query(Factura).filter(Factura.id == datos.factura_id).first()

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    nueva_transaccion = Transaccion(
        valor_unitario=datos.valor_unitario,
        cantidad=datos.cantidad,
        factura_id=datos.factura_id
    )

    db.add(nueva_transaccion)
    db.commit()
    db.refresh(nueva_transaccion)

    return nueva_transaccion


@router.put("/{id}", response_model=TransaccionResponse)
def actualizar_transaccion(id: int, datos: TransaccionSchema, db: Session = Depends(get_db)):

    transaccion = db.query(Transaccion).filter(Transaccion.id == id).first()

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    transaccion.valor_unitario = datos.valor_unitario
    transaccion.cantidad = datos.cantidad
    transaccion.factura_id = datos.factura_id

    db.commit()
    db.refresh(transaccion)

    return transaccion


@router.delete("/{id}")
def eliminar_transaccion(id: int, db: Session = Depends(get_db)):

    transaccion = db.query(Transaccion).filter(Transaccion.id == id).first()

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    db.delete(transaccion)
    db.commit()

    return {"mensaje": "Transacción eliminada correctamente"}