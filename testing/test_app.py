import unittest

from database.database import create_tables
from database.models import (
    add_student,
    get_students,
    add_skill,
    get_skills,
    add_job,
    get_jobs
)


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_student(self):
        add_student(
            "Test Student",
            "test@gmail.com",
            "Python, Java",
            "Software Developer"
        )

        students = get_students()

        self.assertTrue(len(students) > 0)

    def test_skill(self):
        add_skill("Python")

        skills = get_skills()

        self.assertTrue(len(skills) > 0)

    def test_job(self):
        add_job(
            "Python Developer",
            "ABC Company",
            "Python, SQL"
        )

        jobs = get_jobs()

        self.assertTrue(len(jobs) > 0)


if __name__ == "__main__":
    unittest.main()