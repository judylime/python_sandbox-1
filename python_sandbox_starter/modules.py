# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
# from camelcase import camelcase

# import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()

# c = Camelcase()
# print(c.hump('hello there world'))
# print(timestamp)

email = 'test3test.com'
if validate_email(email):
  print('email is valid')
else:
  print('email is bad')