import pytest

from fibonacci import *


@pytest.mark.parametrize(
        "n, expected_value",
        [
            (1, 0),
            (2, 1),
            (3, 1),
            (4, 2),
            (5, 3),
            (6, 5),
            (7, 8),
            (8, 13),
            (9, 21),
        ]
)
def test_fibo_ok(n: int, expected_value: int):
    actual_value = fibo(n)
    assert expected_value == actual_value

def test_fibo_default():
    assert 34 == fibo(10)

@pytest.mark.parametrize(
        "n",
        [ 0, -1 ,-2 ]
)
def test_fibo_ko(n: int):
    with pytest.raises(ValueError) as ex_info:
        _ = fibo(n)
    assert "argument must be strictly positive" == str(ex_info.value)


@pytest.mark.parametrize(
        ["n", "expected_value"],
        [
            (-1, []),
            (0, []),
            (1, [0]),
            (2, [0, 1]),
            (3, [0, 1, 1]),
            (4, [0, 1, 1, 2]),
            (5, [0, 1, 1, 2, 3]),
            (6, [0, 1, 1, 2, 3, 5]),
            (7, [0, 1, 1, 2, 3, 5, 8]),
            (8, [0, 1, 1, 2, 3, 5, 8, 13]),
            (9, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
        ]
)
def test_fibo_list_ok(n: int, expected_value: list[int]):
    actual_value = fibo_list(n)
    assert expected_value == actual_value

def test_fibo_list_default():
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 33, 55] == fibo_list()