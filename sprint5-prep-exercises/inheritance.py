class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""

        if len(self.previous_last_names) > 0:
            suffix = f" (previously {self.previous_last_names[0]})"

        return f"{self.first_name} {self.last_name}{suffix}"


person1 = Child("Sara", "Ali")

print(person1.get_name())
print(person1.get_full_name())

person1.change_last_name("Ahmed")

print(person1.get_name())
print(person1.get_full_name())


person2 = Parent("Sara", "Ali")

print(person2.get_name())

# These lines would cause errors because these methods
# only exist in Child, not Parent:

# print(person2.get_full_name())
# person2.change_last_name("Ahmed")

print(person2.get_name())

# This would also cause an error:
# print(person2.get_full_name())


# The important inheritance relationship is:

# Parent
#   │
#   ├── get_name()
#   │
#   ▼
# Child
#   ├── inherits get_name()
#   ├── adds change_last_name()
#   └── adds get_full_name()

# So a Child can use the inherited Parent method, but a Parent cannot use methods that only exist in Child.