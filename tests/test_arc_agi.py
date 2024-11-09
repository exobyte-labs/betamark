from betamark import arc_agi


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

    result = arc_agi.run_eval(user_func=placeholder)
    assert result["acc"] == 0.0025
