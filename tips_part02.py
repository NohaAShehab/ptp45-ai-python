

def sumnum(num1, num2):
    res  = num1 + num2
    return res



# lambda

myfun = lambda x, y : x + y

print(myfun(434,435))
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("abc", 100)
s2 = Student("mm", 213)
items = [s2 , s1]
# items.sort()

# lambda



# def sort_object(obj1, obj2):
#     if obj1.grade >= obj2.grade:
#         return obj1
#     else:
#         return obj2

###########################################################
nums = [4,5,6]

def mulby10(num):
    return num * 10

newll=  map(mulby10, nums)
print(newll)  # map object
# casting to a list
print(list(newll))

# new mapping
newl = map(lambda x: x+10 , nums)
#
print(list(newl))
#
# newl2 = map(lambda  x: x*5, nums)




###########################





it= filter(lambda x:x%5==0, [-15, -8, -5, 3, 5, 9, 25])
print(it)

print(list(it))








