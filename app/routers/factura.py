from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.factura import Factura
from app.models.cliente import Cliente
from app.schemas import FacturaSchema, FacturaResponse

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)


@router.get("/", response_model=list[FacturaResponse])
def obtener_facturas(db: Session = Depends(get_db)):
    return db.query(Factura).all()


@router.post("/", response_model=FacturaResponse)
def crear_factura(datos: FacturaSchema, db: Session = Depends(get_db)):

    cliente = db.query(Cliente).filter(Cliente.id == datos.cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    nueva_factura = Factura(
        fecha=datos.fecha,
        cliente_id=datos.cliente_id
    )

    db.add(nueva_factura)
    db.commit()
    db.refresh(nueva_factura)

    return nueva_factura


@router.put("/{id}", response_model=FacturaResponse)
def actualizar_factura(id: int, datos: FacturaSchema, db: Session = Depends(get_db)):

    factura = db.query(Factura).filter(Factura.id == id).first()

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    factura.fecha = datos.fecha
    factura.cliente_id = datos.cliente_id

    db.commit()
    db.refresh(factura)

    return factura


@router.delete("/{id}")
def eliminar_factura(id: int, db: Session = Depends(get_db)):

    factura = db.query(Factura).filter(Factura.id == id).first()

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    db.delete(factura)
    db.commit()

    return {"mensaje": "Factura eliminada correctamente"}