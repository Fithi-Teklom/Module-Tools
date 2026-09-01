from dataclasses import dataclass
from enum import Enum
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


# 1. The library already has some laptops
laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


# 2. Get the person's name
name = input("Enter your name: ")


# Get age as text, then convert it to int immediately
age_input = input("Enter your age: ")

try:
    age = int(age_input)
except ValueError:
    print("Error: age must be a whole number.", file=sys.stderr)
    sys.exit(1)


# Get operating system as text, then convert it to an enum immediately
os_input = input(
    "Enter your preferred operating system "
    "(Ubuntu, Arch Linux, macOS): "
)

try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print(
        "Error: operating system must be Ubuntu, Arch Linux, or macOS.",
        file=sys.stderr,
    )
    sys.exit(1)


# Now we have correctly typed data, so create the Person
person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_os,
)


# 3. Count laptops with the person's preferred operating system
preferred_count = 0

for laptop in laptops:
    if laptop.operating_system == person.preferred_operating_system:
        preferred_count += 1


print(
    f"The library has {preferred_count} laptop(s) "
    f"with {person.preferred_operating_system.value}."
)


# 4. Check whether another operating system has more laptops
for operating_system in OperatingSystem:

    # Don't compare their preferred OS with itself
    if operating_system == person.preferred_operating_system:
        continue

    count = 0

    for laptop in laptops:
        if laptop.operating_system == operating_system:
            count += 1

    if count > preferred_count:
        print(
            f"If you are willing to use {operating_system.value}, "
            f"you are more likely to get a laptop because "
            f"the library has {count} available."
        )


