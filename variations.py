n = 30
k = 4
pow = 0

def variations(n = n, k = k):
    results = []

    for_Newton = [n, k, n-k]

    for rep in range(1, len(for_Newton) + 1):
        start_pos = rep
        start_value = 1

        for element in range(1, for_Newton[start_pos-1]+1):
            n_element = start_value * element
            start_value = n_element

        results.append(n_element)
        print(results)

    n_value = results[0]
    n_k_diff = results[2]

    if pow == 0:
        result = n_value / n_k_diff
    else:
        result = n ** k
    return result


print(variations())