import random
import struct
import time


def get_nth_bit(x: float, n: int) -> int:
    """
    Recupere le n-ieme bit de la representation binaire d'un float en
    double precision (64 bits, IEEE 754).
    On considere que le bit d'indice 0 est le bit le plus significatif (bit
    de signe) et que le bit d'indice 63 est le moins significatif.

    :param x: Nombre flottant à convertir.
    :param n: Indice du bit à recuperer (0 <= n < 64).
    :return: Le bit à l'indice n (0 ou 1).


    """
    # Convertir le float en 8 octets, puis en entier non signe (64 bits)
    bits = struct.unpack("!Q", struct.pack("!d", x))[0]
    # Decaler de (63 - n) bits à droite pour placer le n-ieme bit en position
    # 0, puis effectuer un masque pour l'extraire
    return (bits >> (63 - n)) & 1


def is_positive_bit(x: float) -> bool:
    """
    En utilisant la representation binaire du nombre x.
    Si le nombre x est positif ça doit retourner True, sinon False
    """
    # A Faire
    # Vous pouvez utiliser la fonction get_nth_bit
    return True


def is_positive_naive(x: float) -> bool:
    """
    En utilisant uniquement des comparaisons <, <=, >, ou >= determine si x est positif.
    Si le nombre x est positif ça doit retourner True, sinon False
    """
    # A Faire
    return True


if __name__ == "__main__":
    # Test sur des valeurs specifiques pour verifier que les deux fonctions
    # donnent le même resultat
    print("Lancement des tests specifiques pour verifier les fonctions...")
    test_values = [-100.0, -1.0, 0.0, 0.0, 0.1, 1.0, 3.14, 100.0, -0.0001]
    # Valeurs attendues (considerant 0.0 et -0.0 comme positifs)
    expected_values = [
        False,  # -100.0 est negatif
        False,  # -1.0 est negatif
        True,  # 0.0 est positif
        True,  # 0.0 est positif
        True,  # 0.1 est positif
        True,  # 1.0 est positif
        True,  # 3.14 est positif
        True,  # 100.0 est positif
        False,  # -0.0001 est negatif
    ]

    for x, expected in zip(test_values, expected_values):
        result_bit = is_positive_bit(x)
        result_naive = is_positive_naive(x)
        assert (
            result_bit == result_naive
        ), f"Erreur pour x = {x} : {result_bit} != {result_naive}"
        assert (
            result_bit == expected
        ), f"Pour x = {x}, attendu {expected} mais obtenu {result_bit}"

    print("Tous les tests specifiques sont valides.\n")

    print("Lancement des tests de performances...")
    # Warm-up : executer un certain nombre d'iterations pour "chauffer" le CPU
    warmup_iterations = 100000
    for _ in range(warmup_iterations):
        _ = is_positive_bit(random.uniform(-100, 100))
        _ = is_positive_naive(random.uniform(-100, 100))

    # Nombre d'essais pour la comparaison de performance
    N = 10**6
    # Generer N nombres flottants aleatoires entre -100 et 100
    valeurs = [random.uniform(-100, 100) for _ in range(N)]

    # Mesurer le temps d'execution de la methode par extraction du bit de signe
    debut = time.perf_counter()
    for v in valeurs:
        is_positive_bit(v)
    fin = time.perf_counter()
    temps_bits = fin - debut

    # Mesurer le temps d'execution de la methode naïve (comparaison directe)
    debut = time.perf_counter()
    for v in valeurs:
        is_positive_naive(v)
    fin = time.perf_counter()
    temps_naif = fin - debut

    print(f"Temps de la methode par bits : {temps_bits:.6f} secondes")
    print(f"Temps de la methode naïve    : {temps_naif:.6f} secondes")