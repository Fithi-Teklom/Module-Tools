# Better organisation — behaviour related to a class stays together with that class.

# Easier to discover — if I have a Person, I can look at the Person class to see what it can do.

# More readable — person.is_adult() clearly shows that is_adult is behaviour associated with a Person.

# Encapsulation — other code doesn't need to know the internal details of how Person calculates something.

# Easier maintenance/refactoring — if the internal representation changes, such as changing age to date_of_birth, we can update the method while callers can continue using person.is_adult().