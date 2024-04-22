import numpy as np

class Rubik_cube():
    def __init__(self):
        self.sides = np.empty((6, 3, 3), dtype=str)

    def load_configuration_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = (line.strip().split(",") for line in file.readlines())
                if len(lines) != 6:
                    raise ValueError("El archivo debe contener 6 líneas.")

                for i, colors in enumerate(lines):
                    if len(colors) != 9:
                        raise ValueError(f"Cada línea debe contener 9 colores/ Error en la línea {i+1}.")

                    invalid_colors = set(colors) - {"W", "O", "G", "R", "B", "Y"}
                    if invalid_colors:
                        raise ValueError(f"Color(es) inválido(s) en la línea {i+1}: {', '.join(invalid_colors)}")

                    self.sides[i] = np.array([colors[j:j+3] for j in range(0, len(colors), 3)])

        except FileNotFoundError:
            print("El archivo no existe")
        except ValueError as ve:
            print("Error al cargar la configuración: ", ve)

    def bfs_solve(self):
        queue = deque([(self, [])])
        while queue:
            current_cube, moves = queue.popleft()

            if current_cube.is_goal_state():
                return moves

            for move in current_cube.valid_moves():
                new_cube = copy.deepcopy(current_cube)
                new_cube.action(move)
                queue.append((new_cube, moves + [move]))

        return None
def print_solution(self, solution):
    decode_step = {
        "U": "Arriba derecha (U)",
        "U'": "Arriba izquierda (U')",
        "D": "Abajo derecha (D)",
        "D'": "Abajo izquierda (D')",
        "F": "Frente derecha (F)",
        "F'": "Frente izquierda (F')",
        "B": "Atrás derecha (B)",
        "B'": "Atrás izquierda (B')",
        "R": "Derecha arriba (R)",
        "R'": "Derecha abajo (R')",
        "L": "Izquierda arriba (L)",
        "L'": "Izquierda abajo (L')",
        "E": "Medio horizontal (E)",
        "E'": "Medio horizontal invertido (E')",
        "S": "Medio vertical (S)",
        "S'": "Medio vertical invertido (S')",
        "M": "Medio central (M)",
        "M'": "Medio central invertido (M')"
    }

    if solution:
        print("Secuencia de pasos necesarios para resolver el cubo:")
        for i, step in enumerate(solution, start=1):
            print(f"Paso {i}: {decode_step.get(step, 'Movimiento desconocido')}")
        print(f"Cantidad de pasos requeridos para la resolución: {len(solution)}")
    else:
        print("No se encontró solución.")
