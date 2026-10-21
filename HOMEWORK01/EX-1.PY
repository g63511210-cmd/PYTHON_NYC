# ask the user to give a number adb udentify if the number is odd or even . even numbers are divisble by 2 which means the remainder is 0.

number = int(input("enter a number :" ))
if number % 2 ==0:
    print("even number")
elif number % 2 !=0 :
    print("odd number ")