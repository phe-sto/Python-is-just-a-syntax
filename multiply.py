from dis import dis


def add5(n):
    s = 0
    for _ in range(n):
        s += 5
    return s


add5(120000000)
dis(add5)
