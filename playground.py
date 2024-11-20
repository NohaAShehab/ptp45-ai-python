
#
# l = [45,243,24]
# print(type(l))
# l.append("new item")


#################33
# class Student:
#     pass

# %%
class Student:
    no_of_objects = 0  # class variable ? this value depends on class not objects

    # constructor define object structure
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade
        Student.no_of_objects += 1

    # instance method
    def printstd(self):
        print(f"My name is {self.name}, My id is {self.id}, my grade is {self.grade}")


# get no of objects ?
print(Student.no_of_objects)
s = Student("abbass", 1, 100)
s2 = Student("mm", 2, 23213)
s3 = Student("abbass", 1, 100)
print(Student.no_of_objects)
print(s3.__dict__)