from enum import Enum


class EvaluationName(Enum):
    APPROPRIATE = "appropriate"
    INAPPROPRIATE = "inappropriate"
    UNKNOWN = "unknown"
    STRONGER = "stronger"
    WEAKER = "weaker"
