from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .subject import Subject
    from .student import Student

class Course:
    def __init__(self, name:str, code:str) -> None:
        self.name = name
        self.code = code
        self.subjects:list[Subject] = []
        self.students:list[Student] = []