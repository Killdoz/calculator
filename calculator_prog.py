import time
print("Hi!")
print("choose your first number")
number = int(input())
print("choose your symbol")
symbol = input()
print("choose your second number")
sec_number = int(input())
if (symbol == '+'):
    print(number + sec_number)
if (symbol == "-"):
    print(number - sec_number)
if (symbol == "*"):
    print(number * sec_number)
if (symbol == "/"):
    print(number / sec_number)
print("thank you to use this calculator :)")
time.sleep(5)





