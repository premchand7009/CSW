import random

rolls=10000
sum_counts={i:0 for i in range(2,13)}
for _ in range(rolls):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
    sum_counts[total]+=1
print("Total Rolls:", rolls)
for sum_value in range(2,13):
    count=sum_counts[sum_value]
    probability=count/rolls
    print(f"Sum: {sum_value}, Count: {count}, Probability: {probability}")
