msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(msg)
print(quote)

print("Hello" in quote)

print(len(quote))

print(quote[2])
print(quote[-2])

#Adittion with strings (concatenates)
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + " " + my_str_2
print(str_plus_str) # Hello World

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26


name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26


name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

