class Factura:
    def __init__(self, id, fecha, cliente):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self.lista_transacciones = []

    def valor_total(self):
        total = 0
        for transaccion in self.lista_transacciones:
            total += transaccion.valor_unitario * transaccion.cantidad
        return total