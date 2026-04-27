import numpy as np

class rules:
    @staticmethod
    def numeros(operador_tablero, valor_num):
        return int(np.sum(operador_tablero[operador_tablero == valor_num]))

    @staticmethod
    def tercia(operador_tablero):
        valores, conteos = np.unique(operador_tablero, return_counts=True)
        if np.any(conteos >= 3):
            return int(np.sum(operador_tablero))
        return 0

    @staticmethod
    def poker(operador_tablero):
        valores, conteos = np.unique(operador_tablero, return_counts=True)
        if np.any(conteos >= 4):
            return int(np.sum(operador_tablero))
        return 0
        
    @staticmethod
    def full(operador_tablero):
        valores, conteos = np.unique(operador_tablero, return_counts=True)
        if (np.any(conteos == 3) and np.any(conteos == 2)) or np.any(conteos == 5):
            return 25
        return 0
        
    @staticmethod
    def escalera_corta(operador_tablero):
        vals = np.unique(operador_tablero)
        diffs = np.diff(vals)
        if len(diffs) >= 3 and np.any(np.convolve((diffs == 1).astype(int), [1, 1, 1], mode='valid') == 3):
            return 30
        return 0

    @staticmethod
    def escalera_larga(operador_tablero):
        vals = np.unique(operador_tablero)
        diffs = np.diff(vals)
        if len(diffs) >= 4 and np.any(np.convolve((diffs == 1).astype(int), [1, 1, 1, 1], mode='valid') == 4):
            return 40
        return 0

    @staticmethod
    def yahtzee(operador_tablero):
        valores, conteos = np.unique(operador_tablero, return_counts=True)
        if np.any(conteos == 5):
            return 50
        return 0

    @staticmethod
    def azar(operador_tablero):
        return int(np.sum(operador_tablero))

    @classmethod
    def evaluar_todo(cls, tablero_valores):
        op = np.array(tablero_valores)
        return {
            "Unos": cls.numeros(op, 1),
            "Dos": cls.numeros(op, 2),
            "Tres": cls.numeros(op, 3),
            "Cuatros": cls.numeros(op, 4),
            "Cincos": cls.numeros(op, 5),
            "Seises": cls.numeros(op, 6),
            "Tercia": cls.tercia(op),
            "Poker": cls.poker(op),
            "Full": cls.full(op),
            "Escalera corta": cls.escalera_corta(op),
            "Escalera larga": cls.escalera_larga(op),
            "Yahtzee": cls.yahtzee(op),
            "Azar": cls.azar(op)
        }