

print("------- Welcome to Noha's customized inputs module ----")


def askforInt(message="Please enter a number: "):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num

        print("---- Please enter valid number ")


#
# salary = askforInt("please enter your salary : ")
# print(salary, type(salary))

track = 'AI'
""" restrict these lines will be not executed unless this file -inputs modules is called directly """
if __name__ == "__main__":
    print("------- Welcome to Noha's customized inputs module ----")
    salary = askforInt("please enter your salary : ")
    print(salary, type(salary))










