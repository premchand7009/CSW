scores = list(map(int, input("Enter the scores of students separated by spaces: ").split()))
average = sum(scores) / len(scores)
print(f"\nAverage Score: {average:.2f}")
print(f"Minimum Score: {min(scores)}")
print(f"Maximum Score: {max(scores)}")
above_avg = [score for score in scores if score > average]
print(f"Scores above average: {above_avg}")
scores.sort(reverse=True)
print(f"Scores in descending order: {scores}")
if len(scores) >= 3:
    scores[-3:] = [0, 0, 0]
else:
    scores = [0 for i in scores]
print(f"After replacing three lowest scores with 0: {scores}")
