from datetime import datetime as dt


class Grid:
    min_x: int
    max_x: int

    min_y: int
    max_y: int

    def __init__(self, dimensions=((-100, 100), (-100, 100))):
        self.min_x, self.max_x = dimensions[0]
        self.min_y, self.max_y = dimensions[1]


class Point:
    current_coordinates: tuple
    coordinates_history: dict

    plane: Grid

    def __init__(self, plane: Grid, coordinates=(0, 0)):
        self.current_coordinates = coordinates
        self.coordinates_history = dict()
        self.plane = plane

    def set_new_coordinates(self, new_coordinates: tuple):
        x_coord = new_coordinates[0]
        y_coord = new_coordinates[1]

        grid_min_x_val = self.plane.min_x
        grid_max_x_val = self.plane.max_x

        grid_min_y_val = self.plane.min_y
        grid_max_y_val = self.plane.max_y

        if (
            grid_min_x_val <= x_coord <= grid_max_x_val
            and grid_min_y_val <= y_coord <= grid_max_y_val
        ):
            self.current_coordinates = new_coordinates
        else:
            raise ValueError('Coordinates out of bounds')

    def store_current_coordinates(self):
        now_dt = dt.now()
        now_str = now_dt.strftime('%f')
        self.coordinates_history[now_str] = self.current_coordinates
