class Transaccion:
    def __init__(self, id, valor_unitario, cantidad, factura_id):
        self.id = id
        self.valor_unitario = valor_unitario
        self.cantidad = cantidad
        self.factura_id = factura_id