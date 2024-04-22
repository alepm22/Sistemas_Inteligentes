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
