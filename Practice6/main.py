import os
from functools import reduce

# Folder
folder = "student_analyzer"

students = []

# STEP 1
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)

        with open(filepath, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append((name, int(score)))

# STEP 2
names = [s[0] for s in students]
scores = [s[1] for s in students]

# STEP 3
total_students = len(students)
total_score = sum(scores)

# max / min
highest = max(scores)
lowest = min(scores)

increased_scores = list(map(lambda x: x + 5, scores))

# >85
top_students = list(filter(lambda x: x[1] > 85, students))

product_scores = reduce(lambda x, y: x * y, scores)

#enumerate
print("Students with index:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

#  zip
combined = list(zip(names, scores))

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted students:")
for name, score in sorted_students:
    print(name, score)

# average score
average = total_score / total_students

# STEP 4
with open("report.txt", "w") as report:
    report.write(f"Total students: {total_students}\n")
    report.write(f"Average score: {average:.2f}\n")
    report.write(f"Highest score: {highest}\n")
    report.write(f"Lowest score: {lowest}\n\n")

    report.write("Top students:\n")
    for name, score in top_students:
        report.write(f"{name} {score}\n")
