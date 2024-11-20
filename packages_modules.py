

"""

 any .py file is considered to be a python module ??
    module --> import part of the module  . or all the module
"""

## I need to create new program for cal

# def askforInt(message="Please enter a number: "):
#     while True:
#         num = input(message)
#         if num.isdigit():
#             num = int(num)
#             return num
#
#         print("---- Please enter valid number ")

# import from module
# num1 = askforInt('please enter first number: ')
# num2 = askforInt('please enter second number: ')
# res= num1 + num2
# print(res)
"1- import the module then use the function "

# import inputsmodule
# num1 = inputsmodule.askforInt('please enter num1 : ')
# num2 = inputsmodule.askforInt('please enter num2 ')
# res = num1 + num2
# print(res)

""" 2- you can alias the module name """
# import inputsmodule as myin
# num1 = myin.askforInt('please enter num1 : ')
# num2 = myin.askforInt('please enter num2 ')
# res = num1 + num2
# print(res)

"""3- import part of the module """
# from inputsmodule import askforInt
#
# print(askforInt("please enter day number: "))

"4- alias block name "
# from inputsmodule import askforInt as numfun
#
# print(numfun("please enter day number: "))
#

########################
# import inputsmodule
# print(inputsmodule.askforInt("please enter age : "))




""" import module from package """

# import  aimans45.mathoperations
# print(aimans45.mathoperations.sumnums(24,4))

""" alias the package """

# import  aimans45.mathoperations as abbass
# print(abbass.sumnums(344,24))

"""import part of module from package """

# from aimans45.mathoperations import sumnums
# print(sumnums(123,234))


""" import form iti """

# import  iti.duck
# print(iti.duck.cal_money(10))

# from iti.duck import  cal_money
# print(cal_money(23))


#
# from iti import welcomemessage
# welcomemessage("Ahmed")

# import  iti
# print(iti.cal_money(234))
from iti import cal_money
print(cal_money(2423))


###############
import os
print(os.getcwd())

print(os.name)

print(os.system('ls -l'))

os.system('pwd')


#############################
import  math
print(math.pi)


#####
import re # regix --> match ,matchall


import time
print(time.time())


####
import random
print(random.random())








