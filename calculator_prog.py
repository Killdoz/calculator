import time
print("Hi!")
print("choose your first number")
number = int(input())
print("choose your symbol")
znak = input()
print("choose your second number")
sec_number = int(input())
if (znak == '+'):
    print(number + sec_number)
if (znak == "-"):
    print(number - sec_number)
if (znak == "*"):
    print(number * sec_number)
if (znak == "/"):
    print(number / sec_number)
print("thank you to use this calculator :)")
time.sleep(5)





