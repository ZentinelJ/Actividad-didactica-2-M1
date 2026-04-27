class player:
    def __init__(self, name, score_card_instance, player_value):
        self.name = name
        self.score_card = score_card_instance
        self.player_value = player_value

    def ver_estado_hoja(self):
        """Muestra qué categorías están llenas y cuáles no."""
        print(f"\n--- Hoja compartida ---")
        self.score_card.pintar_tablero()

    def elegir_y_marcar_categoria(self, dados):
        """
        Cumple con: 'Player elige qué casilla seleccionar'
        y 'Se anota... Si no hay resultado, se pone 0'.
        """
        opciones = self.score_card.obtener_puntuaciones_posibles(dados, self.player_value)

        print(f"\nOpciones disponibles para {self.name}:")
        categorias_disponibles = list(opciones.keys())

        if not categorias_disponibles:
            print("No quedan categorías disponibles.")
            return

        for i, cat in enumerate(categorias_disponibles):
            print(f"{i + 1}. {cat} ({opciones[cat]} pts)")

        while True:
            try:
                seleccion = int(input("\nSelecciona el número de la categoría: ")) - 1
                if 0 <= seleccion < len(categorias_disponibles):
                    cat_elegida = categorias_disponibles[seleccion]
                    puntos = opciones[cat_elegida]

                    self.score_card.registrar_puntos(self.player_value, cat_elegida, puntos)
                    break
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")