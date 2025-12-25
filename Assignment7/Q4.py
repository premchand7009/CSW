import random

def generate(n):
    d={i:0 for i in range(0,10)}
    for _ in range(n):
        num=random.randint(0,9)
        d[num]+=1
    print("Total Generations:", n)
    print("Digit\tFrequency\tRatio (Actual/Expected)")
    for num in range(10):
        count=d[num]
        expected=n/10
        ratio=count/expected if expected > 0 else 0
        print(f"{num}\t{count}\t\t{ratio:.2f}")

generate(10000)
