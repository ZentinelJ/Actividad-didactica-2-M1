## 1. Introducción
Este proyecto implementa el clásico juego de mesa **Yahtzee** para dos jugadores en la consola de Python, incorporando una característica analítica avanzada: un **Motor de Simulación de Monte Carlo**. Este motor permite a los jugadores predecir estadísticamente la probabilidad de obtener ciertos patrones (como un Full House o un Yahtzee) basándose en los dados que deciden mantener en cada turno.

## 2. Arquitectura y Estructura del Código
La solución está modularizada siguiendo principios de programación orientada a objetos (POO), distribuyendo la lógica en diferentes archivos:

*   **`main.py`**: Orquesta el flujo principal del juego. Contiene la clase `YahtzeeGame` que gestiona las 13 rondas, turnos de los jugadores y el submenú de acciones (Lanzar, Plantarse, Simular, Rendirse).
*   **`monte_carlo_engine.py`**: Contiene la clase `MonteCarloEngine`, el núcleo analítico. Utiliza la biblioteca `numpy` para generar $N$ lanzamientos aleatorios de manera eficiente y evaluar qué patrones se forman.
*   **`simular.py`**: Envuelve al motor de Monte Carlo. Se encarga de traducir los resultados crudos en probabilidades porcentuales y utiliza `matplotlib` para renderizar un gráfico de barras mostrando la distribución probabilística.
*   **`rules.py`**: Implementa la lógica de puntuación. Mediante operaciones vectorizadas con `numpy`, detecta patrones complejos en los 5 dados como: *Escalera Larga*, *Escalera Corta*, *Full*, *Poker*, *Tercia*, etc.
*   **`score_card.py`**: Mantiene el estado de la hoja de puntuaciones para ambos jugadores, calcula sumas parciales, determina si aplica el bono (suma >= 63) y calcula el puntaje total. También se encarga de renderizar la tabla en consola.
*   **`player.py`**: Representa a un jugador. Maneja la interacción para elegir qué categoría marcar al final de un turno validando solo categorías libres.
*   **`dice.py`** y **`lanzar.py`**: Manejan la entidad básica del dado (con su respectivo valor de 1 a 6) y la lógica de generar los nuevos valores aleatorios en cada lanzamiento.

## 3. Lógica del Juego
El flujo de juego respeta las reglas tradicionales de Yahtzee:
1.  **Rondas**: Existen 13 rondas, en las cuales cada jugador tiene su turno.
2.  **Lanzamientos**: Un jugador puede lanzar los dados hasta 3 veces por turno. En el primer lanzamiento se tiran todos los dados automáticamente.
3.  **Decisiones**: Antes del segundo y tercer lanzamiento, el jugador debe decidir qué dados mantener (indicándolos por sus índices 0-4).
4.  **Puntuación**: Al finalizar los lanzamientos (o plantarse), se evalúan las combinaciones posibles en las categorías disponibles y el jugador elige dónde anotar. Si no cumple el patrón en la categoría elegida, se anotará un 0.

## 4. El Motor de Monte Carlo (Simulación Predictiva)
La innovación principal de esta solución es la integración de cálculos de probabilidad en tiempo real, ayudando al jugador en la toma de decisiones.

*   **¿Cómo se activa?**: Durante su turno (antes de alcanzar el límite de 3 tiros), el jugador puede elegir la opción de **Simulación**.
*   **¿Cómo funciona?**:
    1.  El jugador indica qué dados desea "mantener" en la simulación.
    2.  El motor `MonteCarloEngine` toma esos dados fijos y utiliza `numpy` para generar aleatoriamente los valores de los dados restantes miles de veces (por defecto 10,000 iteraciones).
    3.  Para cada uno de los escenarios generados, se aplican las reglas (`rules.py`) y se cuenta qué patrón (Tercia, Poker, Yahtzee, etc.) se logró formar.
    4.  Los resultados se tabulan y se calcula la probabilidad relativa de cada patrón.
*   **Visualización**: El módulo `simular.py` muestra en la consola una tabla detallada con conteos y probabilidades, y finalmente despliega una ventana gráfica interactiva con `matplotlib` usando un diagrama de barras de fácil lectura.

## 5. Algoritmos Destacados
*   **Detección de Escaleras (`rules.py`)**: En lugar de evaluar condiciones booleanas complejas y anidadas, se usa la diferencia de valores adyacentes de los arreglos únicos (`np.diff(vals)`) combinada con una convolución (`np.convolve`) para encontrar rápidamente secuencias matemáticas de 3 o 4 incrementos consecutivos.
*   **Evaluación Vectorizada**: Para evitar cuellos de botella por bucles iterativos lentos durante la simulación de miles de tiradas, el motor genera una matriz completa de $N$ dimensiones y delega la comprobación a las eficientes funciones vectorizadas de `numpy`.

## 6. Requisitos de Ejecución
Para ejecutar esta solución correctamente, es necesario tener instaladas las siguientes dependencias del ecosistema de ciencia de datos:
*   `numpy`: Usado intensamente para matemáticas vectoriales y generación de números aleatorios en lotes.
*   `matplotlib`: Necesario para dibujar y mostrar los gráficos de probabilidad al solicitar una simulación.
