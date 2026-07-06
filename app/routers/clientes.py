from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.cliente import Cliente
from app.schemas import ClienteSchema, ClienteResponse

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.get("/", response_model=list[ClienteResponse])
def obtener_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()


@router.post("/", response_model=ClienteResponse)
def crear_cliente(datos: ClienteSchema, db: Session = Depends(get_db)):
    nuevo_cliente = Cliente(
        nombre=datos.nombre,
        correo=datos.correo
    )

    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)

    return nuevo_cliente


@router.put("/{id}", response_model=ClienteResponse)
def actualizar_cliente(id: int, datos: ClienteSchema, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    cliente.nombre = datos.nombre
    cliente.correo = datos.correo

    db.commit()
    db.refresh(cliente)

    return cliente


@router.delete("/{id}")
def eliminar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    db.delete(cliente)
    db.commit()

    return {"mensaje": "Cliente eliminado correctamente"}