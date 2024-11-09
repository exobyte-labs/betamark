from betamark import arc


def test_eval():
    def placeholder(x):
        return [
            [3, 2, 3, 2, 3, 2],
            [7, 8, 7, 8, 7, 8],
            [2, 3, 2, 3, 2, 3],
            [8, 7, 8, 7, 8, 7],
            [3, 2, 3, 2, 3, 2],
            [7, 8, 7, 8, 7, 8],
        ]

    result = arc.run_eval(user_func=placeholder)
    assert result["acc"] == 0.0025
