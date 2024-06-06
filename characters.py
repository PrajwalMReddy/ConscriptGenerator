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
    "r": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (0, 0, 0, unit2),  # Left Vertical
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "l": {
        "lines": [
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (0, 0, 0, unit2),  # Left Vertical
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "j": {
        "lines": [
            (unit, 0, unit, unit2),  # Right Vertical
            (unit0_5, 0, unit, unit),  # Top South
            (unit0_5, unit2, unit, unit),  # Bottom North
        ],
        "size": unit,
    },
    "w": {
        "lines": [
            (0, 0, 0, unit2),  # Left Vertical
            (0, unit, unit0_5, 0),  # Top North
            (0, unit, unit0_5, unit2),  # Bottom South
        ],
        "size": unit,
    },
    "m": {
        "lines": [
            (unit0_5, 0, unit0_5, unit2),  # Vertical
            (unit0_5, unit, unit, 0),  # Top North
            (0, 0, unit0_5, unit),  # Top South
            (unit0_5, unit, unit, unit2),  # Bottom South
            (0, unit2, unit0_5, unit),  # Bottom North
        ],
        "size": unit,
    },
    "n": {
        "lines": [
            (unit0_5, 0, unit0_5, unit2),  # Vertical
            (unit0_5, unit, unit, 0),  # Top North
            (0, 0, unit0_5, unit),  # Top South
        ],
        "size": unit,
    },
    "ṅ": {
        "lines": [
            (unit0_5, 0, unit0_5, unit2),  # Vertical
            (unit0_5, unit, unit, unit2),  # Bottom South
            (0, unit2, unit0_5, unit),  # Bottom North
        ],
        "size": unit,
    },
    "h": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (0, 0, unit, unit2),  # Diagonal Right
            (unit, 0, 0, unit2),  # Diagonal Left
        ],
        "size": unit,
    },
    "c": {
        "lines": [
            (0, 0, 0, unit2),  # Left Vertical
            (unit, 0, unit, unit2),  # Right Vertical
            (0, 0, unit, unit2),  # Diagonal South
            (0, unit2, unit, 0),  # Diagonal North
        ],
        "size": unit,
    },
}

conjunct_consonants = {
    "r": {
        "lines": [
            (0, 0, unit, 0),  # Top Horizontal
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "l": {
        "lines": [
            (0, unit2, unit, unit2),  # Bottom Horizontal
            (unit, 0, unit, unit2)  # Right Vertical
        ],
        "size": unit,
    },
    "j": {
        "lines": [
            (-unit0_5, unit3 - unit0_5, unit0_5, unit3 - unit0_5),  # Horizontal
            (unit0_5, unit3 - unit0_5, unit0_5, unit2 - unit0_5),  # Vertical
        ],
        "size": unit0_5,
    },
    "w": {
        "lines": [
            (-unit0_5, -unit0_5, unit0_5, -unit0_5),  # Horizontal
            (unit0_5, -unit0_5, unit0_5, unit0_5),  # Vertical
        ],
        "size": unit,
    },
}

individual_vowels = {
    "a": {
        "lines": [
            (0, unit0_5, 0, unit0_5 + unit)  # Vertical Line
        ],
        "size": line_width,
    },
    "i": {
        "lines": [
            (0, unit0_5, unit, unit0_5),  # Horizontal Line
            (unit0_5, unit0_5, unit0_5, unit0_5 + unit)  # Vertical Line
        ],
        "size": unit,
    },
    "e": {
        "lines": [
            (0, unit0_5 + unit, unit, unit0_5 + unit),  # Horizontal Line
            (unit0_5, unit0_5, unit0_5, unit0_5 + unit)  # Vertical Line
        ],
        "size": unit,
    },
    "o": {
        "lines": [
            (0, 0, unit0_5, unit0_5),  # Left Diagonal
            (unit0_5, unit0_5, unit, 0),  # Right Diagonal
            (unit0_5, unit0_5, unit0_5, unit0_5 + unit)  # Vertical Line
        ],
        "size": unit,
    },
    "u": {
        "lines": [
            (0, unit2, unit0_5, unit0_5 + unit),  # Left Diagonal
            (unit0_5, unit0_5 + unit, unit, unit2),  # Right Diagonal
            (unit0_5, unit0_5, unit0_5, unit0_5 + unit)  # Vertical Line
        ],
        "size": unit,
    }
}

diacritic_vowels = {
    "a": {
        "lines": [
        ],
        "size": line_width,
    },
    "i": {
        "lines": [
            (0, -unit0_5, unit, -unit0_5),  # Horizontal Line
        ],
        "size": unit,
    },
    "e": {
        "lines": [
            (0, unit3 - unit0_5, unit, unit3 - unit0_5),  # Horizontal Line
        ],
        "size": unit,
    },
    "o": {
        "lines": [
            (0, -unit0_5, unit0_5, 0),  # Left Diagonal
            (unit0_5, 0, unit, -unit0_5),  # Right Diagonal
        ],
        "size": unit,
    },
    "u": {
        "lines": [
            (0, unit2 + unit0_5, unit0_5, unit2),  # Left Diagonal
            (unit0_5, unit2, unit, unit2 + unit0_5),  # Right Diagonal
        ],
        "size": unit,
    }
}

markings = {
    "long": {
        "lines": [
            (unit0_5 / 2, unit0_5, unit0_5 / 2, unit0_5 * 3 / 2),  # Top
            (unit0_5 / 2, unit2 - unit0_5, unit0_5 / 2, unit2 - unit0_5 * 3 / 2),  # Bottom
        ],
        "size": line_width,
    },
    "dead": {
        "lines": [
            (unit0_5 / 2, unit + unit0_5 / 2, unit - unit0_5 / 2, unit2 - unit0_5 / 2),  # South
            (unit0_5 / 2, unit2 - unit0_5 / 2, unit - unit0_5 / 2, unit + unit0_5 / 2),  # North
        ],
        "size": unit0_5 / 2,
    },
    "foreign": {
        "lines": [
            (unit0_5 / 2, unit0_5 / 2, unit - unit0_5 / 2, unit - unit0_5 / 2),  # South
            (unit0_5 / 2, unit - unit0_5 / 2, unit - unit0_5 / 2, unit0_5 / 2),  # North
        ],
        "size": unit0_5 / 2,
    }
}
