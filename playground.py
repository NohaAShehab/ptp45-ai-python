# class Employee:
#     commission = 10
#
#     def __init__(self, name, salary=1000):
#         self.name = name
#         self.salary = salary
#
#     # please consider the first arguement in the function refers to the class not the instance
#     # I need to use this function without using instance
#     # I need to till the interpreter that this methods refers to the class --> define class behaviour
#     # Usually first parameter of such methods is named 'cls'
#     @classmethod
#     def modifyCommission(cls, newvalue):
#         print(cls)  # first parameter refer to the class
#         if isinstance(newvalue, int):
#             # Employee.commission = newvalue
#             cls.commission = newvalue






# class Employee:
#     commission = 10
#     def __init__(self, name, salary ):
#         self.name= name
#         self.salary = salary
#
#     def printEmp(self):
#         print(f"I am employee {self.name}")
#     @classmethod
#     def change_comm(cls, val):
#         if isinstance(val, int):
#
#             cls.commission = val


# Employee.change_comm(189274)
#
# emp = Employee("Amr", 2003)
# emp2 = Employee("Adham", 100)

# e= Employee("<NAME>", 5000)
# Employee.printEmp(e)  # this methods needs instance from the object .
# e.printEmp()


#######################################################
# class Employee:
#     commission = 10
#     def __init__(self, name, salary ):
#         self.name= name
#         self.salary = salary
#
#     @classmethod
#     def create_obj_cp(cls, emp):
#         if isinstance(emp, cls):
#             return cls(emp.name,emp.salary)
#
#
# menna = Employee("menna", 5000)
# print(menna)
# obj2 = Employee.create_obj_cp(menna)
# print(obj2)



l = [32,324]
l.append("abc")
# list class inherits from class object ??


class Course:
    pass

c = Course()
print(c.__dict__)











