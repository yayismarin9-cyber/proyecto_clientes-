from pydantic import BaseModel
from typing import Optional, List


# ==========================
# CLIENTES
# ==========================

class ClienteSchema(BaseModel):
    nombre: str
    correo: str


class ClienteResponse(ClienteSchema):
    id: int

    class Config:
        from_attributes = True


# ==========================
# FACTURAS
# ==========================

class FacturaSchema(BaseModel):
    fecha: str
    cliente_id: Optional[int] = None


class FacturaResponse(FacturaSchema):
    id: int
    cliente: Optional[ClienteResponse] = None
    transacciones: List["TransaccionResponse"] = []

    class Config:
        from_attributes = True


# ==========================
# TRANSACCIONES
# ==========================

class TransaccionSchema(BaseModel):
    valor_unitario: float
    cantidad: int
    factura_id: int


class TransaccionResponse(TransaccionSchema):
    id: int

    class Config:
        from_attributes = True