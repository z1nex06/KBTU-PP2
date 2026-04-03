import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()


# ➕ Добавить контакт
def add_contact():
    n = int(input("How many contacts: "))

    for i in range(n):
        print(f"\nContact {i+1}")
        name = input("Name: ")
        phone = input("Phone: ")

        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )

    conn.commit()
    print("\nВсе контакты добавлены!\n")


# 📥 Импорт из CSV
def import_csv():
    try:
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) < 2:
                    continue

                name, phone = row[0], row[1]

                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )

        conn.commit()
        print("CSV импортирован!\n")

    except Exception as e:
        print("Ошибка:", e)


# 📋 Показать все
def show_contacts():
    cur.execute("SELECT name, phone FROM contacts")
    rows = cur.fetchall()

    if not rows:
        print("Пусто\n")
    else:
        for row in rows:
            print(f"{row[0]} | {row[1]}")
        print()


# 🔍 Поиск
def search():
    value = input("Search: ")

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s OR phone ILIKE %s",
        ('%' + value + '%', '%' + value + '%')
    )

    rows = cur.fetchall()

    if not rows:
        print("Не найдено\n")
    else:
        for row in rows:
            print(row)
        print()


# ✏️ Обновить
def update():
    name = input("Name to update: ")
    phone = input("New phone: ")

    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (phone, name)
    )
    conn.commit()
    print("Обновлено!\n")


# ❌ Удалить
def delete():
    value = input("Enter name or phone: ")

    cur.execute(
        "DELETE FROM contacts WHERE name=%s OR phone=%s",
        (value, value)
    )
    conn.commit()
    print("Удалено!\n")


# 🔁 Меню
while True:
    print("1.Add")
    print("2.Import CSV")
    print("3.Show")
    print("4.Search")
    print("5.Update")
    print("6.Delete")
    print("7.Exit")

    ch = input("Choose: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        import_csv()
    elif ch == "3":
        show_contacts()
    elif ch == "4":
        search()
    elif ch == "5":
        update()
    elif ch == "6":
        delete()
    elif ch == "7":
        break
    else:
        print("Ошибка выбора\n")


# закрытие
cur.close()
conn.close()