def group_sum(list, n):
    res = []

    for i in range(len(list)):
        list_excluding = [list[j] for j in range(len(list)) if j != i]

        res.append(group_sum(list_excluding, n - list[i]))

    return any(res)