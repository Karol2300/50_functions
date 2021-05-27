n = 10
k = 2
pow = 1

def combinations(n = n, k = k):
    results = []

    if pow == 0:
        for_Newton = [n, k, n-k]

    else:
        for_Newton = [k + n - 1, k, n - 1]


    for rep in range(1, len(for_Newton) + 1):
        start_pos = rep
        start_value = 1

        for element in range(1, for_Newton[start_pos-1]+1):
            n_element = start_value * element
            start_value = n_element

        results.append(n_element)
        print(results)

    n_value = results[0]
    k_value = results[1]
    n_k_diff = results[2]
    k_n_1 = results[0]
    k = results[1]
    n_1 = results[2]

    if pow == 0:
        result = n_value / (n_k_diff * k_value)
    else:
        result = k_n_1/(k*n_1)
    return result


print(combinations())