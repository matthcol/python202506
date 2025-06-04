from euclide import pgcd
import pytest

def test_pgcd_1_1():
    assert 1 == pgcd(1, 1)


def test_pgcd_1_other():
    assert 1 == pgcd(1, 3)

@pytest.mark.timeout(2)
@pytest.mark.parametrize(
        "a, b, expected_gcd", # paramètres attendus
        [
            (1, 1, 1), # 1er cas
            (1, 12, 1),
            (12, 1, 1),
            (15, 21, 3), 
            (21, 15, 3),
            (832040, 1346269, 1), # ration nombre d'or
        ]
)
def test_pgcd_ok(a, b, expected_gcd):
    actual_gcd = pgcd(a, b)
    assert expected_gcd == actual_gcd

@pytest.mark.timeout(2)
@pytest.mark.parametrize(
      "a, b",
      [
          (0, 5),
          (5, 0),
          (0, 0),
          (-1, 5),
          (5, -1),
          (-1, -1),
      ]
)
def test_pgcd_ko(a, b):
    with pytest.raises(ValueError):
        _ = pgcd(a, b)
    # auto: pytest check expected exception happened
    # 3 scenarii:
    # - no exception is raised: test is failed
    # - exception ValueError is raised: test is OK
    # - another exception is raised: test is failed