class PilaApoyos:
    def __init__(self):
        self.items = []

    def empilar(self, item):
        self.items.append(item)

    def desempilar(self):
        if not self.esta_vacia():
            return f"Quitado: {self.items.pop()}"
        return "La pila está vacía."

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.items
