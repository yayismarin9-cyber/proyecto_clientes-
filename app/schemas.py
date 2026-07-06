from pydantic import BaseModel


class ClienteSchema(BaseModel):
    id: int
    nombre: str
    correo: str


class FacturaSchema(BaseModel):
    id: int
    fecha: str
    cliente: str


class TransaccionSchema(BaseModel):
    id: int
    valor_unitario: float
    cantidad: int
    factura_id: int