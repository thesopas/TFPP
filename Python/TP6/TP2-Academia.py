from datetime import date

class Person:
    def __init__(self, first_name:str, last_name:str, dob:date, 
                 state:str, city:str, street:str, number:str, zip_code:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = Address(state, city, street, number, zip_code)

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.dob.year

        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1

        return age

class Student(Person):
    def __init__(self, first_name:str, last_name:str, dob:date, 
                 state:str, city:str, street:str, number:str, zip_code:str,
                 file_no:str, course:'Course') -> None:
        super().__init__(first_name, last_name, dob,
                         state, city, street, number, zip_code)
        self.file_no = file_no
        self.course = course

class Teacher(Person):
    def __init__(self, first_name:str, last_name:str, dob:date, 
                 state:str, city:str, street:str, number:str, zip_code:str,
                 subjects:list['Subject'] | None = None) -> None:
        super().__init__(first_name, last_name, dob,
                         state, city, street, number, zip_code)
        self.subjects = subjects if subjects else []

class Address:
    def __init__(self, state:str, city:str, street:str, number:str, zip_code:str):
        self.state = state
        self.city = city
        self.street = street
        self.number = number
        self.zip_code = zip_code

class Subject:
    def __init__(self, name:str, code:str) -> None:
        self.name = name
        self.code = code
        self.teachers:list[Teacher] = []

class Course:
    def __init__(self, name:str, code:str) -> None:
        self.name = name
        self.code = code
        self.subjects:list[Subject] = []
        self.students:list[Student] = []

class AcademyManagement:
    def __init__(self) -> None:
        self.courses:list[Course] = []
        self.subjects:list[Subject] = []
        self.teachers:list[Teacher] = []
        self.students:list[Student] = []

    
        