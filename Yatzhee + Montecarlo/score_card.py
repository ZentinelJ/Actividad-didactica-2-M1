from rules import rules

class score_card:
    def __init__(self):
        # Listas [puntaje_j1, puntaje_j2]
        # None indica que la casilla está libre, 0 es que se marcó un 0.
        self.card = {
            "Unos": [None, None],
            "Dos": [None, None],
            "Tres": [None, None],
            "Cuatros": [None, None],
            "Cincos": [None, None],
            "Seises": [None, None],
            "Suma": [0, 0],
            "Bono": [0, 0],
            "Tercia": [None, None],
            "Poker": [None, None],
            "Full": [None, None],
            "Escalera corta": [None, None],
            "Escalera larga": [None, None],
            "Yahtzee": [None, None],
            "Azar": [None, None],
            "Puntaje total": [0, 0]
        }
        self.categorias_juego = [k for k in self.card.keys() if k not in ("Suma", "Bono", "Puntaje total")]

    def actualizar_sumas(self):
        """Recalcula las sumas, bonos y totales para ambos jugadores."""
        for j in (0, 1):
            # Suma de parte superior
            suma_sup = sum(self.card[cat][j] or 0 for cat in ["Unos", "Dos", "Tres", "Cuatros", "Cincos", "Seises"])
            self.card["Suma"][j] = suma_sup
            
            # Bono
            if suma_sup >= 63:
                self.card["Bono"][j] = 35
            else:
                self.card["Bono"][j] = 0
                
            # Puntaje Total
            total = suma_sup + self.card["Bono"][j] + sum(
                self.card[cat][j] or 0 for cat in ["Tercia", "Poker", "Full", "Escalera corta", "Escalera larga", "Yahtzee", "Azar"]
            )
            self.card["Puntaje total"][j] = total

    def obtener_puntuaciones_posibles(self, dados, jugador):
        """Retorna {categoria: puntaje} solo para las que el jugador tiene en None."""
        valores = [d.valor for d in dados]
        posibles = rules.evaluar_todo(valores)
        
        opciones_disponibles = {}
        for cat in self.categorias_juego:
            if self.card[cat][jugador] is None:
                opciones_disponibles[cat] = posibles[cat]
                
        return opciones_disponibles

    def registrar_puntos(self, jugador, categoria, puntos):
        """Anota los puntos de un jugador en la categoría, y actualiza sumas."""
        if self.card[categoria][jugador] is None:
            self.card[categoria][jugador] = puntos
            self.actualizar_sumas()

    def obtener_total(self, jugador):
        return self.card["Puntaje total"][jugador]

    def pintar_tablero(self, mostrar_ceros=False):
        def blancos(val):
            if val is None:
                return " "
            if val == 0 and not mostrar_ceros:
                return "0" 
            return str(val)

        ancho_cat = 18
        ancho_col = 11

        borde_top    = f"╔{'═'*ancho_cat}╦{'═'*ancho_col}╦{'═'*ancho_col}╗"
        borde_header = f"╠{'═'*ancho_cat}╬{'═'*ancho_col}╬{'═'*ancho_col}╣"
        borde_mid    = f"╠{'═'*ancho_cat}╬{'═'*ancho_col}╬{'═'*ancho_col}╣"
        borde_bot    = f"╚{'═'*ancho_cat}╩{'═'*ancho_col}╩{'═'*ancho_col}╝"

        print(borde_top)
        print(f"║{'Categoría':<{ancho_cat}}║{'Jugador 1':^{ancho_col}}║{'Jugador 2':^{ancho_col}}║")
        print(borde_header)

        separador_en = {"Bono", "Puntaje total"}

        for categoria, (j1, j2) in self.card.items():
            print(f"║{categoria:<{ancho_cat}}║{blancos(j1):^{ancho_col}}║{blancos(j2):^{ancho_col}}║")
            if categoria in separador_en and categoria != "Puntaje total":
                print(borde_mid)

        print(borde_bot)