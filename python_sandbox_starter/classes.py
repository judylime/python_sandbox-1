# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
import email


class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
  
  def greeting(self):
    return f'my name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1
    
# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
    
  def set_balance(self, balance):
    self.balance = balance
    
  def greeting(self):
    return f'my name is {self.name} and I am {self.age} and my balance is {self.set_balance}'

# Init user object
brad = User('Brad Traversy', 'test@test.com', 37)

# Init customer object
janet = Customer('Janet Johnson', '123@123.com', 25)
janet.set_balance = 500

print(janet.greeting())
print(type(brad))
print(brad.age)
brad.has_birthday()
print(brad.greeting())