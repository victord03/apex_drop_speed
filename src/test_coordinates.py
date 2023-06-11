# Design by testing

# Think about WHAT to do, not how !

import pytest
from datetime import datetime as dt

import coordinates as cd

dimensions = ((-50, 50), (-50, 50))
new_coordinates = (1, 2)

out_of_bound_x_coordinate_min = (dimensions[0][0] - 10, 5)
out_of_bound_x_coordinate_max = (dimensions[0][1] + 10, 5)

out_of_bound_y_coordinate_min = (5, dimensions[1][0] - 10)
out_of_bound_y_coordinate_max = (5, dimensions[1][1] + 10)

grid_instance = cd.Grid(dimensions)
point_instance = cd.Point(grid_instance)


def test_create_grid():
    """I represent an empty 2-axis (x, y) grid."""
    assert isinstance(grid_instance, cd.Grid)
    assert grid_instance.min_x == dimensions[0][0]
    assert grid_instance.max_x == dimensions[0][1]
    assert grid_instance.min_y == dimensions[1][0]
    assert grid_instance.max_y == dimensions[1][1]


def test_create_point():
    """I represent a point at a (x=0, y=0) default position"""
    assert isinstance(point_instance, cd.Point)
    assert point_instance.current_coordinates == (0, 0)


def test_set_new_coordinates():
    """New coordinates can be passed and set to the Point object"""
    point_instance.set_new_coordinates(new_coordinates)

    assert point_instance.current_coordinates == new_coordinates

    with pytest.raises(ValueError):
        assert point_instance.set_new_coordinates(out_of_bound_x_coordinate_min)
        assert point_instance.set_new_coordinates(out_of_bound_x_coordinate_max)
        assert point_instance.set_new_coordinates(out_of_bound_y_coordinate_min)
        assert point_instance.set_new_coordinates(out_of_bound_y_coordinate_max)


def test_store_current_coordinates():
    """I can store current coordinates in a dictionary using the milliseconds of the current time
    using datetime.datetime.now()."""
    point_instance.set_new_coordinates(new_coordinates)
    now_dt = dt.now()
    now_str = now_dt.strftime("%f")
    point_instance.store_current_coordinates()
    assert point_instance.coordinates_history[now_str] == new_coordinates
