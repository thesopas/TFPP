from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .teacher import Teacher

class Subject:
    def __init__(self, name:str, code:str) -> None:
        self.name = name
        self.code = code
        self.teachers:list[Teacher] = []