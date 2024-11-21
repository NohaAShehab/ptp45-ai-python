

class Employee:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        self.__salary = salary


emp = Employee('abc', "abc@gmail.com", 4000)

print(emp.name)
emp.name = 'updated'

# protected
print(emp._email)  # please don't write this
emp._email = "updated@gmail.com"

# print(emp.__salary)  # AttributeError: 'Employee' object has no attribute '__salary'
#

# print(emp.__dict__)
#
# """
#     {'name': 'updated', '_email': 'updated@gmail.com', '_Employee__salary': 4000}
#
# """
# print(emp._Employee__salary)
#
# emp._Employee__salary= 78416782467846
#
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.salary = salary  # use property setter while creating the object
#
#     @property  #
#     def salary(self):
#         return self.__abbasss * .8
#
#     @salary.setter
#     def salary(self, salary):
#         if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
#             self.__abbasss = salary
#         else:
#             raise ValueError('salary must be an integer or float')
#
#
#
# emp = Employee("abc", "adasd", 2312312)
# print("0000 hii ---")
# emp.salary = 324  # call salary.setter
#
# print(emp.__dict__)

#############################3












