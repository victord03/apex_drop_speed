
class WorldMap:
    dimensions: tuple[int, int]
    grid: list

    def __init__(self, dimensions: tuple[int, int]):
        self.dimensions = dimensions

        number_of_rows = dimensions[0]
        number_of_columns = dimensions[1]

        self.grid = [1 for _ in range(0, number_of_rows)]

        # grid_copy = self.grid.copy()

        """for row in grid_copy:
            column = [1 for _ in range(0, number_of_columns)]
            self.grid[row] = column"""
