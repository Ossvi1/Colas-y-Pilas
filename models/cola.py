class ColaTarjetas:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return f"Atendido: {self.items.pop(0)}"
        return "La cola está vacía."

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items
