# __init__ --> initialization
# this is the entry / initialization file for the package
# when you import package or part of it
# the content of this file is executed
print("-- welcome to ITI package ")

### you can use this file to import from package directly
#
def welcomemessage(name):
    print(f"Welcome {name}")


#### you can register package content here ??
from iti.duck import  cal_money

