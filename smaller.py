def smaller(x, y):
    for x_c, y_c in zip(x, y):
        if x_c == y_c:
            continue

        if x_c < y_c:
            return x
        else
            return y
    return x

a = "dell"
b = "dmac"

print(smaller(b, a))