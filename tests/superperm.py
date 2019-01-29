import itertools


def diff(a, b):
    return [i for i in a if not i in set(b)]


def gen_covered(n):
    covered_list = [[i] for i in list(range(n))]
    c_n = 1

    while c_n < n:
        c_n += 1
        new_covered_list = []

        for i in covered_list:
            for j in diff(range(n), i):
                new_covered_list += [i + [j]]

        covered_list = new_covered_list

    return {tuple(i): False for i in covered_list}


def vals_starting_with(x: tuple, covered: dict):
    return dict(i for i in covered.items() if i[0][:len(x)] == x)


def num_false_starting_with(x: tuple, covered: dict):
    return len([i[0] for i in vals_starting_with(x, covered).items() if not i[1]])


def get_index(n, next_val, covered):
    if len(next_val) == n - 1:
        first_check = diff(range(n), next_val)

        if len(first_check) == 1 and not covered[tuple(next_val + first_check)]:
            return [first_check[0]]

        return get_index(n, next_val[1:], covered)

    possible_indexes = diff(range(n), next_val)

    c_max = 0
    c_index = []

    for i in range(len(possible_indexes)):
        m = num_false_starting_with(tuple(next_val + [possible_indexes[i]]), covered)

        if m > c_max:
            c_max = m
            c_index = [i]

        elif m == c_max:
            c_index += [i]

    if c_max == 0 and len(next_val) > 1:
        return get_index(n, next_val[1:], covered)

    return [possible_indexes[i] for i in c_index]

def super_perm(n, result=None, covered=None, level=0):
    options = [str(i + 1) for i in range(n)]

    if result is None or covered is None:
        result = list(range(n))
        covered = gen_covered(n)

        covered[tuple(range(n))] = True  # (0, 1, 2, ..., n) is covered

    while not all(covered.values()):
        next_val = result[1 - n:]

        index = get_index(n, next_val, covered)

        if len(index) > 1:
            returns = []

            for i in index:
                c_res = result.copy() + [i]
                c_covered = covered.copy()
                c_covered[tuple(next_val + [i])] = True

                returns += [super_perm(n, c_res, c_covered, level + 1)]

            a_r = ["", -1]

            for r in returns:
                if r[1] < a_r[1] or a_r[1] == -1:
                    a_r = r

            print(level)
            return a_r

        result += index
        covered[tuple(next_val + index)] = True
        continue

        # TODO Everything lol

    return ("".join([options[i] for i in result]), len(result))

print(super_perm(6))