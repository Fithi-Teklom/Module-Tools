class Person:
    def __init__(
        self,
        name: str,
        age: int,
        preferred_operating_system: str
    ):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18


def get_address(person: Person) -> str:
    return person.address


imran = Person("Imran", 22, "Ubuntu")

print(imran.name)
print(is_adult(imran))