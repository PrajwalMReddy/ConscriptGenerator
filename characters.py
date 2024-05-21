from config import *

consonants = {
    "p": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (0, 0, 0, unit2),  # Left Vertical
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "t": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (0, 0, 0, unit2),  # Left Vertical
        ],
        "size": unit,
    },
    "k": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "f": {
        "lines": [
            (0, unit, unit0_5, 0),  # Top North
            (unit0_5, 0, unit, unit),  # Top South
            (0, unit, unit0_5, unit2),  # Bottom South
            (unit0_5, unit2, unit, unit),  # Bottom North
        ],
        "size": unit,
    },
    "s": {
        "lines": [
            (0, unit, unit0_5, 0),  # Top North
            (0, unit, unit0_5, unit2),  # Bottom South
        ],
        "size": unit0_5,
    },
    "x": {
        "lines": [
            (unit0_5, 0, unit, unit),  # Top South
            (unit0_5, unit2, unit, unit),  # Bottom North
        ],
        "size": unit0_5,
    },
    "v": {
        "lines": [
            # Top
            (0, unit / 2, unit0_5, 0),  # Top North
            (unit0_5, 0, unit, unit / 2),  # Top South
            (0, unit / 2, unit0_5, unit),  # Bottom South
            (unit0_5, unit, unit, unit / 2),  # Bottom North

            # Bottom
            (0, (unit / 2) + unit, unit0_5, unit),  # Top North
            (unit0_5, unit, unit, (unit / 2) + unit),  # Top South
            (0, (unit / 2) + unit, unit0_5, unit2),  # Bottom South
            (unit0_5, unit2, unit, (unit / 2) + unit),  # Bottom North
        ],
        "size": unit,
    },
    "z": {
        "lines": [
            # Top
            (0, unit / 2, unit0_5, 0),  # Top North
            (0, unit / 2, unit0_5, unit),  # Bottom South

            # Bottom
            (0, (unit / 2) + unit, unit0_5, unit),  # Top North
            (0, (unit / 2) + unit, unit0_5, unit2),  # Bottom South
        ],
        "size": unit0_5,
    },
    "g": {
        "lines": [
            # Top
            (unit0_5, 0, unit, unit / 2),  # Top South
            (unit0_5, unit, unit, unit / 2),  # Bottom North

            # Bottom
            (unit0_5, unit, unit, (unit / 2) + unit),  # Top South
            (unit0_5, unit2, unit, (unit / 2) + unit),  # Bottom North
        ],
        "size": unit0_5,
    },
}
