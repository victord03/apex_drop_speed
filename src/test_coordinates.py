# Design by testing

# Think about WHAT to do, not how !

import coordinates

def test_create_grid():
    assert isinstance(coordinates.Grid(), coordinates.Grid)

def test_create_point():
    """I represent a point at a (x=0, y=0) default position"""
    assert coordinates.Point().coordinates == (0, 0)



