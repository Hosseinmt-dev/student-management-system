import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
db = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
) 

cursor = db.cursor()

def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")

def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")
def add_students():
    student_number = input("student_number = ")
    name = input("name =  ")
    age = get_int_input("age = ")
    major = input("major = ")
    average = get_float_input("average = ")

    sql = """
    insert into students(student_number, name, age, major, average)
    values(%s,%s,%s,%s,%s)
    """
    
    values = (student_number,name,age,major,average)
    cursor.execute(sql , values)
    db.commit()
    print("student added successfully.")

def show_all_students():
    sql = "select * from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_students():
    student_number = input("student_number = ")
    sql = "select * from students where student_number=%s"
    cursor.execute(sql,(student_number,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print("student not found !!")
        
def delete_students():
    student_number = input("enter student_number = ")
    sql = "delete from students where student_number=%s"
    cursor.execute(sql,(student_number,))
    db.commit()    
    print("delete student is seccess")

def update_student():
        student_number = input("enter student_number = ")
        new_name = input("new name = ")
        sql = "update students set name = %s where student_number=%s"
        cursor.execute(sql,(new_name,student_number))
        db.commit()
        print("update successfully.")

while True:
    print("\n 1. add student")
    print("2. show all students")
    print("3. update student ")
    print("4. delete student ")
    print("5. search student ")
    print("0. exit")

    choice=input("choice = ")
    if choice =="1":
        add_students()
    elif choice == "2":
        show_all_students()
    elif choice== "3":
        update_student()    
    elif choice== "4": 
        delete_students()
    elif choice== "5":
        search_students()
    elif choice == "0":
        break