import math

l = [2, 3, 5, 6, 4, 27]
d = {"Prime": [], "Composite": [], "Perfect Square": [], "Perfect Cubes": []}

def check(l, d):
    for n in l:
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            d["Prime"].append(n)
        else:
            d["Composite"].append(n)
        if int(math.sqrt(n)) ** 2 == n:
            d["Perfect Square"].append(n)
        if round(n ** (1/3)) ** 3 == n:
            d["Perfect Cubes"].append(n)

check(l, d)
print(d)
