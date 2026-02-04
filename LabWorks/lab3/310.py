import sys

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, gpa):
        # Вызываем конструктор родительского класса Person для сохранения имени
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        # Выводим данные в строгом соответствии с форматом
        print(f"Student: {self.name}, GPA: {self.gpa}")

def solve():
    # Считываем данные из стандартного ввода
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    name = input_data[0]
    gpa = input_data[1]

    # Создаем объект класса Student
    student = Student(name, gpa)
    
    # Вызываем метод вывода
    student.display()

if __name__ == "__main__":
    solve()