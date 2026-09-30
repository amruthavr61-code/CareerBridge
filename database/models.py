from database.database import get_connection


def add_student(name, email, skills, career_goal):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (name, email, skills, career_goal)
        VALUES (?, ?, ?, ?)
    """, (name, email, skills, career_goal))

    connection.commit()
    connection.close()


def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()
    return students


def add_skill(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO skills (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    connection.close()


def get_skills():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM skills")
    skills = cursor.fetchall()

    connection.close()
    return skills


def add_job(title, company, skills):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO jobs (title, company, skills)
        VALUES (?, ?, ?)
    """, (title, company, skills))

    connection.commit()
    connection.close()


def get_jobs():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()

    connection.close()
    return jobs