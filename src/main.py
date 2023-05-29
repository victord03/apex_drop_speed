import math
from classes.World_map import WorldMap
import numpy as np

def main():

    map_dimensions = (100, 200)
    wm = WorldMap(map_dimensions)

    print(round(np.rad2deg((1/math.sqrt(5))), 2))

    angle_ratio = (1 / math.sqrt(5))
    conversion_to_degrees = (180/math.pi)
    print(round(angle_ratio * conversion_to_degrees, 2))


if __name__ == "__main__":
    main()
