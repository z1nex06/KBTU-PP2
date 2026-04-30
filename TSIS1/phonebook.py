from connect import get_connection
import json

def menu():
    print("\n1.View\n2.Search\n3.Add phone\n4.Move group\n5.Export\n6.Import\n0.Exit")
    return input("Choose: ")

def view():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT c.id, c.first_name, c.surname, c.email, g.name
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    """)

    for r in cur.fetchall():
        print(r)

    conn.close()

def search():
    q = input("Search: ")
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for r in cur.fetchall():
        print(r)

    conn.close()

def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    t = input("Type: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, t))
    conn.commit()

    print("OK")

def move():
    name = input("Name: ")
    group = input("Group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL move_to_group(%s,%s)", (name, group))
    conn.commit()

    print("Moved")

def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts('')")

    data = []
    for r in cur.fetchall():
        data.append({
            "name": r[1],
            "email": r[2],
            "birthday": str(r[3]),
            "group": r[4],
            "phones": r[5]
        })

    with open("contacts.json","w") as f:
        json.dump(data,f,indent=4)

    print("Exported")

def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    conn = get_connection()
    cur = conn.cursor()

    for d in data:
        cur.execute("""
        INSERT INTO contacts(first_name,surname,email,birthday)
        VALUES (%s,%s,%s,%s)
        """, tuple(d["name"].split()) + (d["email"], d["birthday"]))

    conn.commit()
    print("Imported")

def main():
    while True:
        c = menu()
        if c=="1": view()
        elif c=="2": search()
        elif c=="3": add_phone()
        elif c=="4": move()
        elif c=="5": export_json()
        elif c=="6": import_json()
        elif c=="0": break

main()