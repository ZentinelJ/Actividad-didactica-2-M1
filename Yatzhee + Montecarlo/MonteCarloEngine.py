import numpy as np
from rules import rules

class MonteCarloEngine:
    def __init__(self, n: int = 100_000, seed: int = 42):
        self.n = n
        np.random.seed(seed)

    def correr(self, dados_mantenidos=None) -> dict:
        """Simula N lanzamientos y retorna frecuencia de patrones.
        Se puede pasar una lista de valores de dados que se mantienen."""
        if dados_mantenidos is None:
            dados_mantenidos = []
            
        n_mantenidos = len(dados_mantenidos)
        n_a_tirar = 5 - n_mantenidos
        
        # Generamos tiros nuevos
        if n_a_tirar > 0:
            tiros_nuevos = np.random.randint(1, 7, size=(self.n, n_a_tirar))
            # Combinar con los dados que ya tenemos mantenidos
            if n_mantenidos > 0:
                mantenidos_array = np.tile(dados_mantenidos, (self.n, 1))
                tiros = np.hstack((mantenidos_array, tiros_nuevos))
            else:
                tiros = tiros_nuevos
        else:
            tiros = np.tile(dados_mantenidos, (self.n, 1))
        
        PATRONES = ["Yahtzee", "Poker", "Full", "Escalera larga",
                    "Escalera corta", "Tercia", "Azar"]
        conteos = {p: 0 for p in PATRONES}

        for tiro in tiros:
            if rules.yahtzee(tiro) > 0:
                conteos["Yahtzee"] += 1
            elif rules.poker(tiro) > 0:
                conteos["Poker"] += 1
            elif rules.full(tiro) > 0:
                conteos["Full"] += 1
            elif rules.escalera_larga(tiro) > 0:
                conteos["Escalera larga"] += 1
            elif rules.escalera_corta(tiro) > 0:
                conteos["Escalera corta"] += 1
            elif rules.tercia(tiro) > 0:
                conteos["Tercia"] += 1
            else:
                conteos["Azar"] += 1

        return conteos
