n = 10
p = 2


def permutations(n = n, p = p ):

    if p == 0:
        n_value = 1
        for element in range(1, n+1):
            n_element = n_value * element
            n_value = n_element
            permutacja = n_value
        print(f"Liczba permutacji dla zbioru liczacego {n} elementów bez powtórzeń jest równa: {permutacja} ")

    else:
        n_value = 1
        for element in range(1, n+1):

            n_element = n_value * element
            n_value = n_element

            if element == n:
                p_value = 1
                for element in range(1, p+1):
                    p_element = p_value * element
                    p_value = p_element
                permutacja_zp = n_value/p_value
                print(f"Liczba permutacji dla zbioru liczacego {n} elementów z {p} powtórzeniami jest równa: {permutacja_zp} ")

            else:
                pass




permutations()