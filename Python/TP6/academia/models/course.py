from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student import Student
    from .subject import Subject

class Course:
    def __init__(self, name:str, code:str) -> None:
        self.name = name
        self.code = code
        self.subjects:list[Subject] = []
        self.students:list[Student] = []
