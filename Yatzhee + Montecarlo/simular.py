import matplotlib.pyplot as plt
from monte_carlo_engine import MonteCarloEngine

class simular:
    """Motor Monte Carlo para estimar probabilidades de patrones en Yahtzee.
    Consume a MonteCarloEngine."""

    def __init__(self, n: int = 100_000, seed: int = 42):
        self.n = n
        self.motor = MonteCarloEngine(n=n, seed=seed)
        self.conteos = {}

    def correr(self, dados_mantenidos=None) -> dict[str, int]:
        """Ejecuta la simulación usando el motor y acumula los conteos."""
        if dados_mantenidos is None:
            dados_mantenidos = []
        self.conteos = self.motor.correr(dados_mantenidos)
        return self.conteos

    def probabilidades(self) -> dict[str, float]:
        """Retorna la probabilidad (%) de cada patrón."""
        if not self.conteos:
            self.correr()
        return {p: round(c / self.n * 100, 4) for p, c in self.conteos.items()}

    def mostrar_probabilidades(self) -> None:
        """Imprime la tabla de probabilidades en consola."""
        probs = self.probabilidades()
        print(f"\n{'Patrón':<18} {'Conteo':>8} {'Probabilidad':>13}")
        print("-" * 42)
        for patron, prob in probs.items():
            print(f"{patron:<18} {self.conteos[patron]:>8} {prob:>12.4f}%")

    def graficar(self) -> None:
        """Muestra un gráfico de barras con la distribución de patrones."""
        probs = self.probabilidades()
        patrones = list(probs.keys())
        valores = list(probs.values())

        colores = ["#e63946", "#f4a261", "#2a9d8f", "#457b9d",
                   "#a8dadc", "#6a4c93", "#adb5bd"]

        plt.figure(figsize=(11, 5))
        barras = plt.bar(patrones, valores, color=colores, edgecolor="white", linewidth=0.8)

        for barra, val in zip(barras, valores):
            plt.text(barra.get_x() + barra.get_width() / 2,
                     barra.get_height() + 0.1,
                     f"{val:.2f}%", ha="center", va="bottom", fontsize=9)

        plt.title(f"Distribución de Patrones — {self.n:,} simulaciones", fontsize=13)
        plt.xlabel("Patrón")
        plt.ylabel("Probabilidad (%)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Test rápido de funcionamiento
    sim = simular(n=10000)
    sim.mostrar_probabilidades()