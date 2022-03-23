#Solve a second degree equation
from math import sqrt
print("This program will solve the equation ax^2+bx+c=0")
a=int(input("Please, give coefficient a "))
b=int(input("Please, give coefficient b "))
c=int(input("Please, give coefficient c "))
print("Your equation is "+str(a)+"*x^2+"+str(b)+"*x+"+str(c)+"=0")
if (a==0):
    if (b==0):
        if(c==0):
            print("Your equation admits an infinity of solution")
        else:
            print("Your equation admits no solution")
    else:
        print("Your equation admits one solution:",-c/b)
else:
    delta=b**2-4*a*c

    if delta==0:
        print("Your equation admits a double solution:",-b/(2*a))
    elif delta>0:
        print("Your equation admits two real solutions solution:",(-b-sqrt(delta))/(2*a),"and",(-b+sqrt(delta))/(2*a))
    else:
        print("Your equation admits two complex solutions solution:",(-b-1j*sqrt(-delta))/(2*a),"and",(-b+1j*sqrt(-delta))/(2*a))
