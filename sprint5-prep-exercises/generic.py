from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: list


fatma = Person(name="Fatma", age= 26, children=[])
aisha = Person(name="Aisha", age = 20, children=[])

imran = Person(name="Imran", age = 45, children=[fatma, aisha])


def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")


print_family_tree(imran)