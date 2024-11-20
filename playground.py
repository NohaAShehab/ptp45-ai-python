
# print("00000 this is my first program 00000")
# num = int(input("Enter a number: "))
# print(num, type(num))

# try:
#     num2 = int(input("Enter a number: "))
#     print(num2, type(num2))
# except:
#     print(f"=== Error happened ")
#     print(num2)

##################33
count= 0
while True:
    try:
        num = int(input("please enter num "))
        print(num)
        break
    except:
        print("--- please enter valid number ")
        count +=1
        if count == 4:
            print("----- sorry locked")
            break









