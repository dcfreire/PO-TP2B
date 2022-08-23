import re
import numpy as np


def get_max_change(a, costs, x, idx):
    x_a = a[idx]
    aux = a.T.copy()
    x = np.delete(x, idx)
    aux = np.delete(aux, idx, axis=1)
    eq = (costs - (aux @ x)) / x_a
    eq[eq == -np.inf] = np.inf
    return (np.nanmin(eq), np.nanargmin(eq))


def is_covered(p, c):
    return p[c == 1].sum() > 0


def set_cover(a, costs):
    c = np.zeros((len(costs),))
    x = np.zeros((a.shape[0],))
    for i, p in enumerate(a):
        if not is_covered(p, c):
            change, idx = get_max_change(a, costs, x, i)
            c[idx] = 1
            x[i] = change
    return c, x


if __name__ == "__main__":
    np.seterr(divide='ignore', invalid='ignore')

    n_elem, n_sub = map(int, re.findall(r"\d+", input()))
    cost = np.array(re.findall(r"\d+,?\d*", input()), np.int64)
    m = np.zeros((n_elem, n_sub), np.int64)
    for i in range(n_elem):
        m[i] = np.array(re.findall(r"\d+,?\d*", input()), np.int64)

    selected_subsets, x = set_cover(m, cost)

    out = ""
    for i in selected_subsets:
        out += f"{int(i)} "
    print(out)
    out = ""

    for i in x:
        out += f"{int(i)} "
    print(out)
