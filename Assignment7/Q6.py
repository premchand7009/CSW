import random
def spin(n):
    d={i:0 for i in range(1,7)}
    for i in range(n):
        a=random.randint(1,6)
        d[a]+=1
    for i in range(1,7):
        print(f"Probability of {i}",d[i]/n)
    print("The segment with the highest appearance:",max(d,key=d.get))
spin(2000)