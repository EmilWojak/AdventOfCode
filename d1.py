from functools import reduce
from operator import mul
from typing import List, Tuple


def wypisz(krok, cel, suma, lista, lewy, prawy):
    suma_l, suma_p = (
        ("==", "==") if suma == cel else ((" <", "  "), ("  ", "> "))[suma > cel]
    )
    print(
        f"{krok:3}: {suma_l}{suma:03}{suma_p} "
        + " ".join(
            f"[{l}]" if i in (lewy, prawy) else f" {l} " for i, l in enumerate(lista)
        )
    )


def znajdz_pare_o_sumie(
    cel: int, liczby: List[int]
) -> Tuple[List[Tuple[int, int]], int]:
    liczby = sorted(liczby)
    lewy, prawy, krok = 0, len(liczby) - 1, 0
    rozwiazania: List[Tuple[int, int]] = []
    # print("krok, suma, liczby")

    while lewy < prawy:
        krok += 1
        suma = liczby[lewy] + liczby[prawy]
        # wypisz(krok, cel, suma, liczby, lewy, prawy)
        if suma == cel:
            rozwiazania.append((liczby[lewy], liczby[prawy]))
            prawy -= 1
        if suma <= cel:
            lewy += 1
        else:
            prawy -= 1
    return rozwiazania, krok


def czesc_1(liczby: List[int]):
    (rozwiazanie,) = znajdz_pare_o_sumie(2020, liczby)[0]
    wynik = [*rozwiazanie, reduce(mul, rozwiazanie)]
    print("{} * {} = {}".format(*wynik))


def czesc_2(liczby: List[int]):
    for n, liczba in enumerate(liczby):
        rest = liczby[0:n] + liczby[(n + 1) :]
        rozwiazania = znajdz_pare_o_sumie(2020 - liczba, rest)[0]
        if rozwiazania:
            (rozwiazanie,) = rozwiazania
            wynik = [liczba, *rozwiazanie]
            wynik = [*wynik, reduce(mul, wynik)]
            print("{} * {} * {} = {}".format(*wynik))


if __name__ == "__main__":
    with open("d1.txt") as f:
        liczby = [int(line) for line in f]
    czesc_1(liczby)
    czesc_2(liczby)
