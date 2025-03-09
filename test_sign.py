import struct
import random
import time


def get_nth_bit(x: float, n: int) -> int:
    """
    Récupère le n-ième bit de la représentation binaire d'un float en double précision (64 bits, IEEE 754).

    On considère que le bit d'indice 0 est le bit le plus significatif (bit de signe)
    et que le bit d'indice 63 est le moins significatif.

    :param x: Nombre flottant à convertir.
    :param n: Indice du bit à récupérer (0 <= n < 64).
    :return: Le bit à l'indice n (0 ou 1).
    """
    # Convertir le float en 8 octets, puis en entier non signé (64 bits)
    bits = struct.unpack('!Q', struct.pack('!d', x))[0]
    # Décaler de (63 - n) bits à droite pour placer le n-ième bit en position 0, puis effectuer un masque pour l'extraire
    return (bits >> (63 - n)) & 1


def is_positive_bit(x: float) -> bool:
    """
    En utilisant la représentation binaire du nombre x.
    Si le nombre x est positif ça doit retourner True, sinon False
    """
    # A Faire
    # Vous pouvez utiliser la fonction get_nth_bit
    return True


def is_positive_naive(x: float) -> bool:
    """
    En utilisant uniquement des comparaisons <, <=, >, ou >= déterminé si x est positif.
    Si le nombre x est positif ça doit retourner True, sinon False
    """
    # A Faire
    return True


if __name__ == '__main__':
    # Test sur des valeurs spécifiques pour vérifier que les deux fonctions donnent le même résultat
    print("Lancement des tests spécifiques pour vérifier les fonctions...")
    test_values = [-100.0, -1.0, 0.0, 0.0, 0.1, 1.0, 3.14, 100.0, -0.0001]
    # Valeurs attendues (considérant 0.0 et -0.0 comme positifs)
    expected_values = [
        False,  # -100.0 est négatif
        False,  # -1.0 est négatif
        True,  # 0.0 est positif
        True,  # 0.0 est positif
        True,  # 0.1 est positif
        True,  # 1.0 est positif
        True,  # 3.14 est positif
        True,  # 100.0 est positif
        False  # -0.0001 est négatif
    ]

    for x, expected in zip(test_values, expected_values):
        result_bit = is_positive_bit(x)
        result_naive = is_positive_naive(x)
        assert result_bit == result_naive, f"Erreur pour x = {x} : {result_bit} != {result_naive}"
        assert result_bit == expected, f"Pour x = {x}, attendu {expected} mais obtenu {result_bit}"

    print("Tous les tests spécifiques sont validés.\n")

    print("Lancement des tests de performances...")
    # Warm-up : exécuter un certain nombre d'itérations pour "chauffer" le CPU
    warmup_iterations = 100000
    for _ in range(warmup_iterations):
        _ = is_positive_bit(random.uniform(-100, 100))
        _ = is_positive_naive(random.uniform(-100, 100))

    # Nombre d'essais pour la comparaison de performance
    N = 10**6
    # Générer N nombres flottants aléatoires entre -100 et 100
    valeurs = [random.uniform(-100, 100) for _ in range(N)]

    # Mesurer le temps d'exécution de la méthode par extraction du bit de signe
    debut = time.perf_counter()
    _ = [is_positive_bit(v) for v in valeurs]
    fin = time.perf_counter()
    temps_bits = fin - debut

    # Mesurer le temps d'exécution de la méthode naïve (comparaison directe)
    debut = time.perf_counter()
    _ = [is_positive_naive(v) for v in valeurs]
    fin = time.perf_counter()
    temps_naif = fin - debut

    print(f"Temps de la méthode par bits : {temps_bits:.6f} secondes")
    print(f"Temps de la méthode naïve    : {temps_naif:.6f} secondes")
    print(
        "Les deux méthodes donnent des résultats identiques pour tous les tests."
    )
