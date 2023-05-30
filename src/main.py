from classes.Jumpmaster import JumpMaster

def main():

    # jm = JumpMaster()

    position = {"x": 0, "y": 10}
    speed = 2
    coefficient = 0.8

    positions_log = list()
    positions_log.append(tuple(position.values()))

    while True:

        position["x"] += 1
        position["y"] -= round(speed * coefficient, 1)

        positions_log.append(tuple(position.values()))

        ground_touched = position["y"] <= 0
        negative_y_next_iteration = position["y"] - round(speed * coefficient, 1) < 0
        if ground_touched or negative_y_next_iteration:
            break

    print(positions_log)

"""diving = True
    while diving:

        progress = int()

        direction = float(input())
        jm.set_direction(direction)

        jm.set_speed()

        diving = False"""


    # print(round(np.rad2deg((1/math.sqrt(5))), 2))

    # angle_ratio = (1 / math.sqrt(5))
    # conversion_to_degrees = (180/math.pi)
    # print(round(angle_ratio * conversion_to_degrees, 2))


if __name__ == "__main__":
    main()
