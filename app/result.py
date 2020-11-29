from typing import NamedTuple


class Result(NamedTuple):
    score: float
    text: str
    pred: int
