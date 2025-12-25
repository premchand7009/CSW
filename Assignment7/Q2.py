import random
l=[]
for i in range (10):
    str=""
    for j in range (8):
        n=random.randint(97,122)
        str+=chr(n)
    l.append(str)
for i in l:
    print(i)
