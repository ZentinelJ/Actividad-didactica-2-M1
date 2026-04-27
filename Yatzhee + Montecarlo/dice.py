import random

class dice:
    """Representa un dado del juego Yahtzee."""

    def __init__(self):
        self.valor: int = 1

    def lanzar(self) -> int:
        """Lanza el dado y devuelve el nuevo valor."""
        self.valor = random.randint(1, 6)
        return self.valor

    def __repr__(self) -> str:
        return f"[{self.valor}]"