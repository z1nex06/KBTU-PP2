import sys

# Читаем всю строку
input_data = sys.stdin.read().strip()

# 1. Находим оператор (+, -, *)
op = ""
if "+" in input_data:
    op = "+"
elif "-" in input_data:
    op = "-"
elif "*" in input_data:
    op = "*"

# 2. Разрезаем строку на два числа по знаку
parts = input_data.split(op)
first_part = parts[0]
second_part = parts[1]

# 3. Функция перевода СЛОВО -> ЧИСЛО через if-else
def word_to_num(text):
    result_str = ""
    # Идем по строке, берем по 3 буквы
    for i in range(0, len(text), 3):
        triplet = text[i:i+3]
        if triplet == "ZER": result_str += "0"
        elif triplet == "ONE": result_str += "1"
        elif triplet == "TWO": result_str += "2"
        elif triplet == "THR": result_str += "3"
        elif triplet == "FOU": result_str += "4"
        elif triplet == "FIV": result_str += "5"
        elif triplet == "SIX": result_str += "6"
        elif triplet == "SEV": result_str += "7"
        elif triplet == "EIG": result_str += "8"
        elif triplet == "NIN": result_str += "9"
    return int(result_str)

num1 = word_to_num(first_part)
num2 = word_to_num(second_part)

# 4. Считаем результат
if op == "+":
    total = num1 + num2
elif op == "-":
    total = num1 - num2
elif op == "*":
    total = num1 * num2

# 5. Перевод ЧИСЛО -> СЛОВО через if-else
final_str = ""
for digit in str(total):
    if digit == "-": continue # на случай отрицательных
    
    if digit == "0": final_str += "ZER"
    elif digit == "1": final_str += "ONE"
    elif digit == "2": final_str += "TWO"
    elif digit == "3": final_str += "THR"
    elif digit == "4": final_str += "FOU"
    elif digit == "5": final_str += "FIV"
    elif digit == "6": final_str += "SIX"
    elif digit == "7": final_str += "SEV"
    elif digit == "8": final_str += "EIG"
    elif digit == "9": final_str += "NIN"

print(final_str)