import math
from classes.World_map import WorldMap
from classes.Jumpmaster import JumpMaster
import numpy as np

def main():

    jm = JumpMaster()

    map_dimensions = (100, 200)
    wm = WorldMap(map_dimensions)

    diving = True
    while diving:
        progress = int()
        direction = float(input())

        jm.set_direction(direction)
        jm.set_speed()

        diving = False



    # print(round(np.rad2deg((1/math.sqrt(5))), 2))

    # angle_ratio = (1 / math.sqrt(5))
    # conversion_to_degrees = (180/math.pi)
    # print(round(angle_ratio * conversion_to_degrees, 2))


if __name__ == "__main__":
    main()
