def process_students(students):
    averages = {}
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        name = student["info"][1]
        averages[name] = avg
        print(f"{name}'s Average Marks: {avg:.2f}")

    skill_count = {}
    for student in students:
        for skill in student["skills"]:
            skill_count[skill] = skill_count.get(skill, 0) + 1

    print("\nSkill Frequency:")
    for skill, count in skill_count.items():
        print(f"{skill}: {count}")

    top_student = max(averages, key=averages.get)
    print(f"\nTop Performing Student: {top_student} ({averages[top_student]:.2f})")


students = [
    {
        "info": (101, "Amit"),
        "marks": [85, 90, 88],
        "skills": {"Python", "C", "Java"}
    },
    {
        "info": (102, "Neha"),
        "marks": [78, 82, 80],
        "skills": {"Python", "C++"}
    },
]

process_students(students)
