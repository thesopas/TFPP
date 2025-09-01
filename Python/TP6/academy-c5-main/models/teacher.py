from datetime import date
from typing import TYPE_CHECKING
from .person import Person

if TYPE_CHECKING:
    from .subject import Subject

class Teacher(Person):
    def __init__(self, first_name:str, last_name:str, dob:date, 
                 state:str, city:str, street:str, number:str, zip_code:str,
                 subjects:list['Subject'] | None = None) -> None:
        super().__init__(first_name, last_name, dob,
                         state, city, street, number, zip_code)
        self.subjects = subjects if subjects else []
