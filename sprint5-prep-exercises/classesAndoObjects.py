class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

#The error is that the code tries to access an attribute called address, but the Person class does not define an address attribute. 
#Mypy knows that imran and eliza are Person objects, so it can detect that .address does not exist before we run the program.