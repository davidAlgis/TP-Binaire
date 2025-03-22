import random
import time


def is_power_of_two_naive(n: int) -> bool:
    """
    Vérifie si n est une puissance de 2 en utilisant des division.
    Méthode naïve.
    """
    # A faire
    return True


def is_power_of_two_bit(n: int) -> bool:
    """
    Vérifie si n est une puissance de 2 en utilisant l'opération binaire &.
    On pourrait par exemple comparer n et un autre nombre bien choisi avec &
    """
    # A faire
    return True


if __name__ == "__main__":
    # Test sur des valeurs spécifiques pour vérifier que les deux fonctions
    # donnent le même résultat
    print("Lancement des tests pour s'assurer que les fonctions sont OK...")
    test_values = [
        0,
        1,
        2,
        3,
        4,
        5,
        8,
        16,
        31,
        32,
        33,
        64,
        100,
        128,
        256,
        1023,
        1024,
        1025,
    ]
    # Valeurs attendues correspondantes
    expected_values = [
        False,  # 0 n'est pas une puissance de 2
        True,  # 1 = 2^0
        True,  # 2 = 2^1
        False,  # 3 n'est pas une puissance de 2
        True,  # 4 = 2^2
        False,  # 5 n'est pas une puissance de 2
        True,  # 8 = 2^3
        True,  # 16 = 2^4
        False,  # 31 n'est pas une puissance de 2
        True,  # 32 = 2^5
        False,  # 33 n'est pas une puissance de 2
        True,  # 64 = 2^6
        False,  # 100 n'est pas une puissance de 2
        True,  # 128 = 2^7
        True,  # 256 = 2^8
        False,  # 1023 n'est pas une puissance de 2
        True,  # 1024 = 2^10
        False,  # 1025 n'est pas une puissance de 2
    ]

    for n, expected in zip(test_values, expected_values):
        result_naive = is_power_of_two_naive(n)
        result_bit = is_power_of_two_bit(n)
        # Vérifie que les deux méthodes donnent le même résultat
        assert (
            result_naive == result_bit
        ), f"Erreur pour n = {n} : {result_naive} != {result_bit}"
        # Vérifie que le résultat est celui attendu
        assert (
            result_naive == expected
        ), f"Pour n = {n}, attendu {expected} mais obtenu {result_naive}"
    print("Tous les tests sont validés.")

    print("Lancement des tests de performances...")
    # Warm-up : exécuter un certain nombre d'itérations pour "chauffer" le CPU
    warmup_iterations = 100000
    for _ in range(warmup_iterations):
        _ = is_power_of_two_naive(random.randint(1, 10**6))
        _ = is_power_of_two_bit(random.randint(1, 10**6))

    # Nombre d'essais pour la comparaison de performance
    N = 5 * 10**6
    # Générer N entiers aléatoires dans une plage donnée
    numbers = [random.randint(1, 10**9) for _ in range(N)]

    # Mesurer le temps d'exécution de la méthode naïve
    start_naive = time.perf_counter()
    for n in numbers:
        is_power_of_two_naive(n)
    end_naive = time.perf_counter()
    time_naive = end_naive - start_naive

    # Mesurer le temps d'exécution de la méthode par bits
    start_bit = time.perf_counter()
    for n in numbers:
        is_power_of_two_bit(n)
    end_bit = time.perf_counter()
    time_bit = end_bit - start_bit

    print(f"Temps de la méthode naïve : {time_naive:.6f} secondes")
    print(f"Temps de la méthode par bits : {time_bit:.6f} secondes")