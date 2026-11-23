# SPDX-FileCopyrightText: 2026-present Baptiste Prisset <baptiste.prisset@etudiant.univ-lr.fr>
#
# SPDX-License-Identifier: MIT

import pytest

from my_arithmetic_bprisset.pgcd import gcd, pgcd


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (48, 18, 6),
        (18, 48, 6),
        (60, 48, 12),
        (100, 10, 10),
        (54, 24, 6),
        (7, 7, 7),
        (1, 42, 1),
        (42, 1, 1),
        (13, 7, 1),
        (17, 19, 1),
    ],
)
def test_pgcd_standard_positive(a: int, b: int, expected: int):
    """Vérifie le calcul du PGCD pour des entiers strictement positifs."""
    assert pgcd(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (-48, 18, 6),
        (48, -18, 6),
        (-48, -18, 6),
        (-7, 7, 7),
        (-13, -7, 1),
    ],
)
def test_pgcd_negative_numbers(a: int, b: int, expected: int):
    """Vérifie que le PGCD est toujours positif, même avec des entiers négatifs."""
    assert pgcd(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (0, 5, 5),
        (5, 0, 5),
        (0, -5, 5),
        (-5, 0, 5),
        (0, 0, 0),
    ],
)
def test_pgcd_with_zeros(a: int, b: int, expected: int):
    """Vérifie le calcul du PGCD lorsque l'un ou les deux termes valent zéro."""
    assert pgcd(a, b) == expected


def test_pgcd_large_numbers():
    """Vérifie le calcul avec de très grands entiers."""
    assert pgcd(1234567890, 9876543210) == 90


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (4.5, 2),
        (2, 4.5),
        ("12", 4),
        (12, "4"),
        (None, 4),
        (4, None),
        (True, 4),
        (4, False),
        ([1, 2], 3),
        (10, {1: 2}),
    ],
)
def test_pgcd_invalid_types_raise_typeerror(a, b):
    """Vérifie que des types non entiers lèvent une exception TypeError."""
    with pytest.raises(TypeError):
        pgcd(a, b)


def test_gcd_alias():
    """Vérifie que l'alias anglais gcd pointe bien sur pgcd."""
    assert gcd is pgcd
    assert gcd(48, 18) == 6
