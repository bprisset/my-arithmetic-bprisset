# SPDX-FileCopyrightText: 2026-present Baptiste Prisset <baptiste.prisset@etudiant.univ-lr.fr>
#
# SPDX-License-Identifier: MIT

def pgcd(a: int, b: int) -> int:
    """Calcule le Plus Grand Commun Diviseur (PGCD) de deux entiers a et b.

    Utilise l'algorithme d'Euclide.
    Le résultat est toujours un entier positif ou nul (si a = b = 0).

    Args:
        a: Premier entier.
        b: Deuxième entier.

    Returns:
        int: Le plus grand commun diviseur de a et b.

    Raises:
        TypeError: Si a ou b n'est pas une instance d'entier (les booléens sont exclus).

    Examples:
        >>> pgcd(48, 18)
        6
        >>> pgcd(-48, 18)
        6
        >>> pgcd(13, 7)
        1
        >>> pgcd(0, 5)
        5
        >>> pgcd(0, 0)
        0
    """
    if type(a) is not int:
        raise TypeError(f"L'argument 'a' doit être un entier (int), reçu {type(a).__name__}.")
    if type(b) is not int:
        raise TypeError(f"L'argument 'b' doit être un entier (int), reçu {type(b).__name__}.")

    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


# Alias en anglais
gcd = pgcd

