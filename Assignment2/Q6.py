def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def process_data(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, list):
            result[key] = sum(x for x in value if is_prime(x))
        elif isinstance(value, tuple):
            product = 1
            for x in value:
                if x % 2 == 1:
                    product *= x
            result[key] = product
    return result

data = {
    "A": [2, 3, 4, 5, 10],
    "B": (1, 2, 3, 4, 5),
    "C": [7, 8, 9],
    "D": (6, 7, 8)
}

print(process_data(data))
