
from prueba1 import mayor


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, 1, 0),
    (0, 0, 0),
    (100, -100, 100),
    (-15, -1, -1),
    (-3, 8, 8),
    (9, (-1, -2), 9)
    ]
)
def test_mayor_params(input_n1, input_n2, expected):
    assert mayor(input_n1, input_n2) == expected