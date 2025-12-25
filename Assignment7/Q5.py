import random

students = ["John", "Riya", "Meera", "Amit", "Rahul", "Zara", "Sneha", "Kunal"]

random.shuffle(students)

teams = {
    "Team A": students[0:2],
    "Team B": students[2:4],
    "Team C": students[4:6],
    "Team D": students[6:8]
}

for team, members in teams.items():
    print(f"{team}: {members[0]}, {members[1]}")
