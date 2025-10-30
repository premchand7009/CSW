def top_student(scores_dict):
    highest_avg = 0
    top_name = ""
    for name, scores in scores_dict.items():
        avg = sum(scores) / len(scores)
        if avg > highest_avg:
            highest_avg = avg
            top_name = name
    return top_name

students_scores = {
    "Ram": [85, 90, 92],
    "Laxman": [70, 80, 88],
    "Janaki": [95, 100, 90]
}
print("Top student:", top_student(students_scores))
