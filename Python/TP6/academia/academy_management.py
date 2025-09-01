from models.course import Course
from models.subject import Subject
from models.teacher import Teacher
from models.student import Student


class AcademyManagement:
    def __init__(self) -> None:
        self.courses: list['Course'] = []
        self.subjets: list['Subject'] = []
        self.teachers: list['Teacher'] = []
        self.students: list['Student'] = []

def create_course(self, name: str, code: str) -> Course:
#Adress y Peson heredan de Teacher y Student
