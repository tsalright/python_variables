# Variable names must start with a letter or underscore.
validName = "Valid Name"
print(validName)

_anotherValidName = "Another Valid Name"
print(_anotherValidName)

# Variables cannot start with a number.
#1invalidName = "Invalid Name"

# Variables can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 = "all valid characters"
print(ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890)

# Variables are case-sensitive
CaseSensitive = "Hello World!"
print(CaseSensitive)

caseSensitive = "This is not Hello World!"
print(caseSensitive)

# Variables do not need to be declared with any particular type and can even change type after they have been set.

numbers = 1
print(numbers)

while numbers < 10:
  numbers = numbers + 1
  print(numbers)


numbers = "Hello"
print(numbers)
