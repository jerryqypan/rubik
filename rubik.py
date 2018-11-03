import numpy as np


class Cube:
    def __init__(self):
        edges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        corners = [0, 1, 2, 3, 4, 5, 6, 7]

    def twist(self, move):
        if move == "U":
            ...

corners = {
    "UFR": 0,
    "URB": 1,
    "UBL": 2,
    "ULF": 3,
    "DRF": 4,
    "DFL": 5,
    "DLB": 6,
    "DBR": 7,
    "FRU": 8,
    "RBU": 9,
    "BLU": 10,
    "LFU": 11,
    "RFD": 12,
    "FLD": 13,
    "LBD": 14,
    "BRD": 15,
    "RUF": 16,
    "BUR": 17,
    "LUB": 18,
    "FUL": 19,
    "FDR": 20,
    "LDF": 21,
    "BDL": 22,
    "RDB": 23
}

moves = {
    "U": [0,1,2,3],
    "F": [0,3,4,7],
    "R": [0,1,4,5],
    "D": [4,5,6,7],
    "B": [1,2,5,6],
    "L": [2,3,6,7]
}

moves_orientation = {
    "U": [0,0,0,0],
    "F": [1,2,1,2],
    "F'": [2,1,2,1],
    "R": [1,2,]

}

edges = {
    "UF": 0,
    "UR": 1,
    "UB": 2,
    "UL": 3,
    "DF": 4,
    "DR": 5,
    "DB": 6,
    "DL": 7,
    "FR": 8,
    "FL": 9,
    "BR": 10,
    "BL": 11,
    "FU": 12,
    "RU": 13,
    "BU": 14,
    "LU": 15,
    "FD": 16,
    "RD": 17,
    "BD": 18,
    "LD": 19,
    "RF": 20,
    "LF": 21,
    "RB": 22,
    "LB": 23
}
