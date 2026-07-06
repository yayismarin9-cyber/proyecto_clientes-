from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    valor_unitario = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)

    factura_id = Column(Integer, ForeignKey("facturas.id"))

    factura = relationship("Factura", back_populates="transacciones")