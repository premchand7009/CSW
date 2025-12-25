import random

tosses = 1000
results = []

for _ in range(tosses):
    results.append(random.choice(["H", "T"]))

heads_count = results.count("H")
tails_count = results.count("T")

prob_heads = heads_count / tosses
prob_tails = tails_count / tosses

print("Total Tosses:", tosses)
print("Number of Heads:", heads_count)
print("Number of Tails:", tails_count)
print("Probability of Heads:", prob_heads)
print("Probability of Tails:", prob_tails)
