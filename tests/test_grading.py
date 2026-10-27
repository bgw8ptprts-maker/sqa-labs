
import pytest
from src.grading import grade



@pytest.mark.parametrize(
    "score, expected",
    [
        (-1, None),
        (0, 2),
        (1, 2),
        (53, 2),
        (54, 2),
        (55, 3),
        (56, 3),
        (68, 3),
        (69, 3),
        (70, 4),
        (71, 4),
        (83, 4),
        (84, 4),
        (85, 5),
        (86, 5),
        (99, 5),
        (100, 5),
        (101, None),
    ],
)
def test_grade_boundaries(score, expected):
    if expected is None:
        with pytest.raises(ValueError):
            grade(score)
    else:
        assert grade(score) == expected



@pytest.mark.parametrize("score", [-1, 101, 2.5, "abc", None, True])
def test_grade_invalid_scores(score):
    with pytest.raises(ValueError):
        grade(score)


