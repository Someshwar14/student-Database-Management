import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="studentdb",
    user="postgres",
    password="yourpassword"
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100)
)
""")
conn.commit()

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cur.execute(
        "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
        (name, age, course)
    )
    conn.commit()
    print("✅ Student Added Successfully!\n")

def view_students():
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print()

def update_student():
    student_id = int(input("Enter Student ID to Update: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")

    cur.execute(
        "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
        (name, age, course, student_id)
    )
    conn.commit()
    print("✅ Student Updated Successfully!\n")

def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("✅ Student Deleted Successfully!\n")

def menu():
    while True:
        print("===== Student Database Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid Choice!\n")

menu()

cur.close()
conn.close()
