from datetime import date
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day
            ):
            age -= 1

        return age >= 18


imran = Person("Imran", date(2000, 10, 10), "Ubuntu")
print(imran.is_adult())