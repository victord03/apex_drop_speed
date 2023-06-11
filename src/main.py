import math


def main():
    free_fall_speed = 40
    dropship_movement_speed = 52
    vertical_height = 570

    distance_to_desired_drop_point_on_the_ground = 700

    def solve_fall_time(distance: int, fall_speed: int) -> float:
        return round(distance / fall_speed, 1)

    def solve_horizontal_distance_parallel_to_the_ground(
        drop_height: int, distance: int
    ) -> float:
        return round(math.sqrt(distance**2 - drop_height**2), 1)

    def solve_time_to_travel_the_horizontal_distance(
        horizontal_distance: float, dropship_speed: int
    ) -> float:
        return round(horizontal_distance / dropship_speed, 1)

    def solve_problem(
        *,
        fall_speed: int,
        drop_ship_speed: int,
        vertical_drop_height: int,
        distance: int,
    ) -> tuple[float, float]:

        time_to_reach_destination_on_the_ground = solve_fall_time(distance, fall_speed)
        horizontal_distance = solve_horizontal_distance_parallel_to_the_ground(
            vertical_height, distance
        )
        time_to_travel_horizontal_distance = (
            solve_time_to_travel_the_horizontal_distance(
                horizontal_distance, drop_ship_speed
            )
        )

        return time_to_reach_destination_on_the_ground, round(
            time_to_travel_horizontal_distance
            + solve_fall_time(vertical_drop_height, fall_speed),
            1,
        )

    long_fall_time, vertical_fall_time = solve_problem(
        fall_speed=free_fall_speed,
        drop_ship_speed=dropship_movement_speed,
        vertical_drop_height=vertical_height,
        distance=distance_to_desired_drop_point_on_the_ground,
    )

    print(
        f"\nCurved fall time: {long_fall_time} seconds."
        + f"\nVertical fall time (+ dropship): {vertical_fall_time} seconds."
    )


if __name__ == "__main__":
    main()
