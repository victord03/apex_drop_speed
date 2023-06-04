

class JumpMaster:
    coordinates: tuple[int, int]

    def __init__(self):
        self.coordinates = (0, 0)

    def update_coordinates(self, new_coordinates: tuple[int, int]):
        self.coordinates = new_coordinates



class MapCoordinates:
    dimensions: tuple[int, int]

    def __init__(self, dimensions: tuple[int, int]):
        self.dimensions = dimensions




def main():

    initial_speed = 100

    horizontal_speed = 50
    vertical_speed = 75  # 30% increase from horizontal speed


if __name__ == '__main__':
    main()
