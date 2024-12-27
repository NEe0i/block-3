num = [(True, True), (True, False), (False, True), (False, False)]


def compute_expressions(X, Y):
    a = not (not X or Y) or not X
    b = not (not X and not Y) and X
    c = not (X or not Y) or not Y
    return a, b, c


for X, Y in num:
    a, b, c = compute_expressions(X, Y)
    print(f"X={X}, Y={Y}:")
    print(f"a) не (не X или Y) или не X = {a}")
    print(f"b) не (не X и не Y) и X = {b}")
    print(f"c) не (X или не Y) или не Y = {c}")
