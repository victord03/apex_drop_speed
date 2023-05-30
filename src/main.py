
def calculate_speed(angle, minimum_speed, maximum_speed):
    min_speed = minimum_speed
    max_speed = maximum_speed

    # Calculate the speed based on the angle. Max speed is achieved at 90 degrees, min at 0.
    speed = min_speed + (max_speed - min_speed) * (90 - angle) / 90
    return speed


def main():

    position = {'x': 0, 'y': 10}
    speed = 2
    coefficient = 0.5

    positions_log = list()
    positions_log.append(tuple(position.values()))

    while True:

        position['x'] += 1
        position['y'] -= round(speed * coefficient, 1)

        if position['y'] <= 0:
            position['y'] = 0

        # I want this to be checked before recording coordinates as if we have landed, we no longer track the free fall
        ground_touched = position['y'] == 0
        if ground_touched:
            break

        positions_log.append(tuple(position.values()))


    print(positions_log)




if __name__ == '__main__':
    main()
