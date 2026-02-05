class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        # Считываем строку из консоли
        self.s = input()

    def printString(self):
        # Печатаем в верхнем регистре
        print(self.s.upper())

# Создаем объект и вызываем методы по порядку
handler = StringHandler()
handler.getString()
handler.printString()