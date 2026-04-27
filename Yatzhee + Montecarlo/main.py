import random
import sys
from player import player
from score_card import score_card
from dice import dice
from lanzar import lanzar
from simular import simular

class YahtzeeGame:
    def __init__(self, player1_name, player2_name):
        random.seed()
        compartido = score_card()
        self.p1 = player(player1_name, compartido, 0)
        self.p2 = player(player2_name, compartido, 1)
        self.rondas_totales = 13
        self.tablero = [dice() for _ in range(5)]
        self.hoja_puntajes = compartido

    def turno_jugador(self, jugador):
        print(f"\n==============================")
        print(f"TURNO DE: {jugador.name}")
        print(f"==============================")
        
        jugador.ver_estado_hoja()

        tiros_realizados = 0
        
        # El primer lanzamiento de la ronda lanza todos los dados (o no, si lo decide?
        # En Yahtzee normalmente tiras antes de decidir, pero si decide Simular antes de tirar,
        # la lista 'dados_mantenidos' estará vacía. Haremos un tiro forzado al empezar.
        lanzar(self.tablero, [])
        tiros_realizados += 1
        print(f"\n[Primer lanzamiento automático]: {self.tablero}")

        while tiros_realizados <= 3:
            if tiros_realizados == 3:
                print(f"\nHas alcanzado el límite de 3 tiros. Debes elegir categoría.")
                break

            print("\n*** SUBMENÚ DE TURNO ***")
            print("1. Rendirse (Terminar el juego por completo)")
            print("2. Simulación (Pronosticar probabilidades manteniendo algunos dados)")
            print("3. Lanzar (Volver a tirar los dados seleccionando cuáles mantener)")
            print("4. Plantarse (No tirar más y usar estos dados para puntuar)")
            
            op = input("Elige una opción (1-4)> ")
            
            if op == "1":
                print(f"\n{jugador.name} se ha rendido. ¡Juego terminado!")
                sys.exit(0)
            elif op == "2":
                print("\nIndica los índices de los dados a MANTENER en la simulación (0 a 4, separados por espacio): ")
                print("Si no pones ninguno, se simulará asumiendo que tiras todos.")
                entrada = input("Índices a mantener> ")
                mantener = [int(i) for i in entrada.split() if i.isdigit() and int(i) < 5]
                dados_mantenidos = [self.tablero[i].valor for i in mantener]
                
                print("\nCalculando simulación de 10,000 escenarios...")
                sim = simular(n=10000, seed=random.randint(1, 100000))
                sim.correr(dados_mantenidos)
                sim.mostrar_probabilidades()
                sim.graficar()
                # No incrementa tiros_realizados, vuelve al menú
                
            elif op == "3":
                print("\nIndica los índices de los dados a MANTENER (ej: 0 1 4) o nada para relanzar todos:")
                entrada = input("Mantener> ")
                mantener_indices = [int(i) for i in entrada.split() if i.isdigit() and int(i) < 5]
                lanzar(self.tablero, mantener_indices)
                tiros_realizados += 1
                print(f"Lanzamiento {tiros_realizados}/3: {self.tablero}")
                
            elif op == "4":
                print(f"\nTe has plantado con: {self.tablero}")
                break
            else:
                print("Opción inválida.")

        # Al finalizar los tiros (o rendirse/plantarse), el jugador elige categoría
        jugador.elegir_y_marcar_categoria(self.tablero)

    def mainloop(self):
        """Ciclo principal del juego."""
        for ronda in range(1, self.rondas_totales + 1):
            print(f"\n\n*** INICIANDO RONDA {ronda}/{self.rondas_totales} ***")
            self.turno_jugador(self.p1)
            self.turno_jugador(self.p2)

        print("\n--- JUEGO TERMINADO ---")
        self.hoja_puntajes.pintar_tablero()
        
        p1_score = self.hoja_puntajes.obtener_total(0)
        p2_score = self.hoja_puntajes.obtener_total(1)

        if p1_score > p2_score:
            print(f"¡GANADOR: {self.p1.name} con {p1_score} puntos!")
        elif p2_score > p1_score:
            print(f"¡GANADOR: {self.p2.name} con {p2_score} puntos!")
        else:
            print(f"¡EMPATE a {p1_score} puntos!")

def menu_inicio():
    while True:
        print("\n=== B I E N V E N I D O   A   Y A H T Z E E ===")
        print("1. Nuevo Juego")
        print("2. Salir")
        op = input("Opción> ")
        if op == "2":
            print("¡Hasta pronto!")
            sys.exit(0)
        elif op == "1":
            print("\nIniciando nuevo juego...")
            game = YahtzeeGame("Jugador 1", "Jugador 2")
            game.mainloop()
        else:
            print("Por favor elige 1 o 2.")

if __name__ == "__main__":
    menu_inicio()