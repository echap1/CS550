from typing import List


class StringTable:
    table: List[List[str]]

    def __init__(self, w, h):
        self.table = [[""] * h] * w