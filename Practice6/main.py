import os
from functools import reduce

# Папка с файлами
folder = "student_analyzer"

students = []

# STEP 1: читаем файлы
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)

        with open(filepath, "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                students.append((name, int(score)))

# STEP 2: отдельные списки
names = [s[0] for s in students]
scores = [s[1] for s in students]

# STEP 3: анализ

# 1. Количество студентов
total_students = len(students)

# 2. Сумма баллов
total_score = sum(scores)

# 3. max / min
highest = max(scores)
lowest = min(scores)

# 4. Увеличение на 5
increased_scores = list(map(lambda x: x + 5, scores))

# 5. >85
top_students = list(filter(lambda x: x[1] > 85, students))

# 6. Произведение
product_scores = reduce(lambda x, y: x * y, scores)

# 7. enumerate
print("Students with index:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

# 8. zip
combined = list(zip(names, scores))

# 9. сортировка
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted students:")
for name, score in sorted_students:
    print(name, score)

# Средний балл
average = total_score / total_students

# STEP 4: запись в файл
with open("report.txt", "w") as report:
    report.write(f"Total students: {total_students}\n")
    report.write(f"Average score: {average:.2f}\n")
    report.write(f"Highest score: {highest}\n")
    report.write(f"Lowest score: {lowest}\n\n")

    report.write("Top students:\n")
    for name, score in top_students:
        report.write(f"{name} {score}\n")