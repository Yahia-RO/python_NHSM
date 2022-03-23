   #subtraction for kids
from random import randint
num1=randint(0,101)#generate a random integer between 0,100
num2=randint(0,101)#generate a random integer between 0,100
if num1<num2:# swap the numbers, if the first number is less than second number
    num1,num2=num2,num1
answer=int(input("What's "+str(num1)+"-"+str(num2)+"?\n"))# read the answer of the user
if answer==num1-num2:#verify if the answer is correct
    print("Great job")
else:#verify if the answer is not correct
    print("Sorry, your answer is incorrect")
