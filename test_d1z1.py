from d1 import znajdz_pare_o_sumie

import pytest
import random


@pytest.mark.parametrize(
    "cel,liczby,rozwiazania,kroki",
    # fmt: off
    [
        pytest.param(14, [],
            [], 0, id="pusta lista"),

        pytest.param(14, [13],
            [], 0, id="jedna licza za mała"),
        pytest.param(14, [14],
            [], 0, id="jedna licza równa celowi"),
        pytest.param(14, [15],
            [], 0, id="jedna licza za duża"),

        pytest.param(14, [1, 12],
            [], 1, id="dwie liczby za małe"),
        pytest.param(14, [1, 13],
            [(1, 13)], 1, id="dwie liczby w sam raz"),
        pytest.param(14, [1, 14],
            [], 1, id="dwie liczby razem za duże"),
        pytest.param(14, [15, 16],
            [], 1, id="dwie liczby obie za duże"),

        pytest.param(14, [3, 5, 7],
            [], 2, id="3 liczby wszystkie za małe"),
        pytest.param(14, [6, 8, 9],
            [(6, 8)], 2, id="3 liczby para po lewej"),
        pytest.param(14, [6, 7, 8],
            [(6, 8)], 1, id="3 liczby para na skraju"),
        pytest.param(14, [4, 6, 8],
            [(6, 8)], 2, id="3 liczby para po prawej"),

        pytest.param(7, [3, 4, 5, 6, 7, 8, 9, 10],
            [(3, 4)], 7, id="8 liczb para po lewej"),
        pytest.param(14, [1, 3, 5, 6, 8, 10, 12, 14],
            [(6, 8)], 7, id="8 liczb para po środku"),
        pytest.param(19, [3, 4, 5, 6, 7, 8, 9, 10],
            [(9, 10)], 7, id="8 liczb para po prawej"),

        pytest.param(140, [8, 9, 68, 72, 77, 80, 107, 111, 120, 121],
            [(68, 72)], 9, id="10 liczb lewy skacze i dubel"),

        pytest.param(14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            [(1, 13), (2, 12), (3, 11), (4, 10), (5, 9), (6, 8)], 6, id="ciąg arytmetyczny"),
        pytest.param(28, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
            [(2, 26), (4, 24), (6, 22), (8, 20), (10, 18), (12, 16)], 6, id="ciąg arytmetyczny parzyste"),
        pytest.param(28, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25],
            [(3, 25), (5, 23), (7, 21), (9, 19), (11, 17), (13, 15)], 7, id="ciąg arytmetyczny niparzyste"),

        pytest.param(140, [9, 10, 11, 15, 16, 19, 21, 23, 26, 30, 33, 39, 42, 45, 61, 63, 69, 71, 82, 86, 103, 115, 133, 135, 136, 139, 140],
            [(69, 71)], 26, id="dlugie - blisko"),
        pytest.param(140, [13, 14, 36, 43, 44, 52, 61, 66, 73, 74, 76, 77, 80, 81, 82, 85, 93, 98, 114, 118, 120, 135, 138, 139],
            [(66, 74)], 22, id="dlugie - dubel blisko"),
        pytest.param(140, [15, 18, 19, 21, 31, 38, 42, 59, 61, 66, 68, 69, 71, 72, 74, 76, 78, 82, 86, 87, 96, 97, 110, 120, 133],
            [(66, 74), (68, 72), (69, 71)], 22, id="dlugie - trzy blisko i dubel"),
        pytest.param(140, [11, 17, 28, 31, 33, 38, 42, 47, 50, 51, 53, 54, 55, 61, 65, 66, 69, 69, 74, 84, 91, 92, 95, 98, 111, 124, 134, 142],
            [(42, 98), (66, 74)], 25, id="dlugie - blisko i daleko"),
        pytest.param(140, [8, 9, 10, 15, 26, 48, 53, 57, 63, 66, 67, 73, 74, 92, 96, 101, 102, 112, 118, 119, 120, 129, 133],
            [(48, 92), (66, 74), (67, 73)], 20, id="dlugie - blisko, lewy duzo skacze i dubel"),
        pytest.param(140, [9, 10, 23, 28, 32, 57, 62, 63, 64, 65, 67, 72, 77, 85, 87, 89, 90, 95, 96, 110, 111, 119, 125, 128, 130],
            [(10, 130), (63, 77)], 22, id="dlugie - blisko i daleko, lewy duzo skacze"),
        pytest.param(140, [9, 13, 27, 31, 33, 34, 42, 46, 50, 56, 66, 70, 72, 75, 76, 78, 80, 85, 86, 87, 90, 95, 101, 103, 109, 111, 113, 116, 120, 131],
            [(9, 131), (27, 113), (31, 109), (50, 90)], 25, id="dlugie - daleko kilka i dubel"),

        pytest.param(140, sorted(random.sample(range(8, 142), 30)), [], -1, marks=pytest.mark.xfail, id="nowy losowy"),
    ],
    # fmt: on
)
def test_znajdz_pare_o_sumie(cel, liczby, rozwiazania, kroki):
    if kroki == -1:
        print(f"\ncel, liczby = {cel}, [{', '.join(str(s) for s in liczby)}]\n")
    assert znajdz_pare_o_sumie(cel, liczby) == (rozwiazania, kroki)
