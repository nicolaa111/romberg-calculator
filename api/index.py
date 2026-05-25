import math

def f(x):
    return math.sin(x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        total += f(a + i * h)

    return h * total


def romberg(a, b, level):
    R = [[0 for _ in range(level + 1)] for _ in range(level + 1)]

    for i in range(level + 1):
        n = 2 ** i
        R[i][0] = trapezoidal(a, b, n)

        for j in range(1, i + 1):
            R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)

    return R[level][level], R


def handler(request):
    body = request.json()

    a = float(body["a"])
    b = float(body["b"])
    level = int(body["level"])

    result, table = romberg(a, b, level)

    return {
        "result": result,
        "table": table
    }
