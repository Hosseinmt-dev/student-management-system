# Student Management System

A simple command-line application for managing student records, built with Python and MySQL.

## Features

- Add new students
- View all students
- Search for a student by student number
- Update student information
- Delete a student record

## Tech Stack

- **Python** – core application logic
- **MySQL** – database for storing student records
- **python-dotenv** – for securely managing database credentials

## Project Structure

students-management/
├── main.py
├── .env          # database credentials (not tracked in git)
├── .gitignore
└── README.md

## Setup & Installation

1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd students-management
```

2. Install dependencies:
```bash
   pip install mysql-connector-python python-dotenv
```

3. Create a `.env` file in the project root with your database credentials:
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=student_management

4. Create the database and table in MySQL:
```sql
   CREATE DATABASE student_management;
   USE student_management;

   CREATE TABLE students (
       student_number VARCHAR(20) PRIMARY KEY,
       name VARCHAR(100),
       age INT,
       major VARCHAR(100),
       average FLOAT
   );
```

5. Run the program:
```bash
   python main.py
```

## Usage

After running the program, you'll see a menu:

1. add student
2. show all students
3. update student
4. delete student
5. search student
6. exit

Enter the number for the action you want to perform and follow the prompts.

## What I Learned

- Connecting Python to a MySQL database using `mysql-connector-python`
- Writing parameterized SQL queries to prevent SQL injection
- Managing sensitive credentials securely using environment variables (`.env` + `python-dotenv`)
- Structuring a simple CRUD (Create, Read, Update, Delete) application

## Future Improvements

- Add input validation and error handling
- Refactor into a REST API
