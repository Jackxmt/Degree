from math import floor, ceil


# __all__ = ["degree"]


class Degree:

    def __init__(self, md: float, degree: object = 0) -> None:
        self.md = md
        self.degree: str = str(md) + "˚"

    def __str__(self):
        return self.degree

    def __repr__(self):
        return self.degree

    def __eq__(self, other: object) -> bool:
        return type(other) == type(self) and other.degree == self.degree

    def __hash__(self) -> int:
        return hash(self.md)

    def __ge__(self, other: object) -> bool:
        return self.md >= other.md

    def __gt__(self, other: object) -> bool:
        return self.md > other.md

    def __le__(self, other: object) -> bool:
        return self.md <= other.md

    def __lt__(self, other: object) -> bool:
        return self.md < other.md

    def __add__(self, other: object):
        return Degree(self.md + other.md)

    def __mul__(self, other: object):
        return Degree(self.md * other.md)

    def __ne__(self, other: object) -> bool:
        return self.md == other.md

    def __sub__(self, other: object):
        return Degree(self.md + other.md)

    def __truediv__(self, other: object):
        return Degree(self.md / other.md)

    def __floordiv__(self, other: object):
        return Degree(self.md // other.md)

    def __floor__(self):
        return Degree(floor(self.md))

    def __ceil__(self):
        return Degree(ceil(self.md))
