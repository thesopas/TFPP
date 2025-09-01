from datetime import date
from .address import Address

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
