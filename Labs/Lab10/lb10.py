firstname = "Yanfei"
lastname="Wu"
country="China"
school="Baruch and QCC"
print(firstname)
question1=input("What's your name?")
print("Hi, my name is "+firstname,lastname)
question2=input("Where do you come from?")
print("I was born in"+" "+country+", the south part of China.")
print("How are you?" +" " + "Hi, my name is "+firstname,lastname + ".")
question3="Which school do you study?"
print("I am a senior at"+" "+school+".")
print("My name is"+ firstname,lastname+"."+" "+"I am a senior at"+" "+school+".")







import math
r = int(input("What is the redius of your circle?"))
C = 2*r*math.pi
A = math.pi*r**2
print("C=",C," A=",A)


import math
r=int(input("What is the redius of your cylinder?"))
h=int(input("What is the height of your cylinder?"))
V=math.pi*r**2*h
print("The volume of the cylinder is V =",V)