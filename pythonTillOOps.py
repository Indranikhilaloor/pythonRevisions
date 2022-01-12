from math import *
charecter_name="Booming bob"
print("Hello world")
print("Boom "+ charecter_name)
print("I will complete this in a day or two")
print("Two max")
#comments
#variables and data types
name="Booming bob"
#int,float,str and boolean too are the data types
print("Girrafe might be the tallest living animal\nI guess")
phrase="Variable phrase value"
print(phrase+" is cooling cool")
print(phrase)
#press phrase. you get a load of methods you can use them actually
print(len(phrase))
print(phrase[0])
print(phrase.index("a"))
print(phrase.replace("is","was"))
#Working with numbers
print(2.0987456)
print(-20)
print(3+4.5)
print((3*4)+5)
my_num=-5
print("your number is"+" "+str(my_num))
print(abs(my_num))
print(pow(2, 4))
print(max(100, 400))
print(min(100,10 ))
print(round(3.14141414141414))
#getting input from users
user_var=int(input("Put some shit in here that shit should be a number\n"))
print("Goddamn this is some serious gourmet shit. You picked "+str(user_var)+" this number")
#Building a calculator
num1=float(input("Enter first number\n"))
num2=float(input("Enter second one\n"))
result=num1*num2
print("The product is "+str(result))
#madlibs game
hero_name=input("Give me your Hero name")
super_power=input("Whats your superpower")
city_name=input("Put your favourite city")
print("Well well well look who\'s here "+hero_name)
print("really! you think you can show up after fuckin everything up with your fucking "+super_power)
print("You still remember the shit you did to our "+city_name)
print("You disgusting,pillpopping scum")
#lists-lists-lists
anime_to_watch=["Fire Force","Monster","Odd Taxi","Your lie in april","Anohana",False,5]
print(anime_to_watch[0])
#same index starts from zero
print(anime_to_watch[1:])
print(anime_to_watch[1:3])
print(anime_to_watch[3])
#list functions
anime_to_watch.append("Soul eater")#adds at end
anime_to_watch.remove("Odd Taxi")#removes
anime_to_watch.insert(1,"One piece")#appends at required index
anime_to_watch.pop()#removes last element in list
anime_to_watch.index("Your lie in april")#returns index of your lie in april
anime_to_watch.index("bleach")#returns -1
print(anime_to_watch)
#anime_to_watch.sort()#sorts numbers
anime_to_watch2=anime_to_watch.copy()#copies
#Tuples-Tuples-Tuples
coordinate=(4,5)
print(coordinate[0])
coordinate[1]=10
#store data which cant be mutable in tuples it can but people wont use to change values in tuples
#functions functions functions
def first_function(name):
    print("Hi "+name)
first_function("Boom")
first_function("Boomer")
print("top")
first_function("Tom")
print("Final")
#return statement function
def returnFunction():
    return  "shit returned"
returnFunction()
#if-else-elif
#calculator
num11=float(input("first number"))
num22=float(input("Second number"))
op=input("What you want to do?")
if(op=='+'):
    print("addition is "+(num11+num22))
elif(op=='-'):
    print("Difference is "+(num11-num22))
elif(op=='*'):
    print("Product is "+ (num11*num22))
elif(op=='/'):
    print("Quotient is "+(num11/num22))
else:
    print("Check once again")

#dictionaries
dictionary_no_1={
    'Key1':"Defnition of key1",
    'key2':"Defnition of key2"
}
#keys should be unique
print(dictionary_no_1[0])#givces defnition of key1
print(dictionary_no_1.get("key1"))#gets key1 value
print(dictionary_no_1.get("key3","Not a valid one"))#if input isnt in dictionary then not a valid one will be printed
#loops-while
#runs until the contidions is unsatisfied
attempts=5
numberfound=False
number_pc_gave=10
guess=""
while(attempts<=0 or numberfound==True):
    guessed_word=input("Enter number less than 20")
    if(int(guessed_word)==number_pc_gave):
        print("You won my man")
        numberfound=True
    elif(int(guessed_word)>number_pc_gave):
        print("Move further and greater")
        attempts-=1
    elif(int(guessed_word)<number_pc_gave):
        print("Move lesser")
        attempts-=1
    else:
        print("Try again")
if(numberfound==True):
    print("Won")
else:
    print("Lost")
#for loops
#for i in range(1,10) stops at 9
#for i in range(1,11,2) stops at 9 and increments 2 so i value will be 1,3,5,7,9
#in arrays use for arrayindex in array A print every elements or traverse through all
#exponent function
print(2**3)#two raised power of 3 whjich is 2^3
def raise_to_power(base_num,power):
    result=1
    for index in range(power):
        result=result*base_num
    return result
#above function is power function
#2d lists and nested loops
number_grid=[
    [1,2,3],[4,5,6],[0]
]
print(number_grid[0][1])#prints 2 in [1,2,3] list which is at 0 index and it has 2 in 1 index
for row in number_grid:
    print(row)#row refers to inner lists i.e [1,2,3][4,5,6][0]
    for column in row:
        print(column)#column refers to elements in the row i.e 1,2,3 in [1,2,3]
#translator
def translate(phrase):
    variable_final=""
    king="KING"
    for index in phrase:
        if(index=="a" or index=="e" or index=="i" or index=="o" or index=="u"):#you can write like this if index in "AEIOUaeiou
            variable_final=variable_final+king
        else:
            variable_final=variable_final+index

translate("shit")
#comments usage
#you know how to use coz you already used *insert baby smirk*
#exceptions try and catch
number_exceptions=int(input("Enter shit"))
try:
    print("number "+number_exceptions)
except ZeroDivisionError:
    print("division by zero etrror")
except ValueError:
    print("Invalid input")

#reading and opening and writing files
#have a employess.txt file
employee=open("employees.txt","r")#w-to write r-to read r+-read and write a- append
print(employee.readable())#gives boolean
print(employee.readline())#first line and moves cursor to next line
print(employee.readlines())#all lines accessed
employee.close()
#writing and appending
employee_write=open("employee.txt","a")#addding something at end
employee_write.write("some shit")
employee_write.write("\nanother shit")#adds in fresh file
employee_write.close()
employee_write_real=open("employee.txt","w")#completely erases everything and starts from beginning
employee_write_real.write("Oh yeah everything is eradicated because of me!!!")
#you can also write html pages in python by adding tags like <p></p> or any tags
#using modules and packages
#import someshit_you_created
#print(someshit_you_created.methiods_in it())
#pip install package name you can install open source modules
#use this command in cmd
#it will be downloaded in lib folder
#oops classes objects
#creating student class
class Student:
    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation
    def getStudent(self):
        print("GETS STUDENT")

#in other file
#from Student import Student
student1=Student("jim","MBA","8.5",True)
print(student1.name)
print(student1.getStudent())
student2=Student("Pam","Marketing","9.5",False)
student2.getStudent()
#quiz project
question_prompts=[
    "What color are apples?\n(a)Red\n(b)Pink\n\n",
    "Who is Ironman?\n(a)RDJ\n(b)ABC\n\n",
    "Who is Ironman?\n(a)RDJ\n(b)ABC\n\n"
]
class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer


questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"a")
]
def runTest(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if(answer==question.answer):
            score+=1
    print("You got "+str(score)+ " for "+str(len(questions)))
runTest(questions)
#inheritance inheritance
class StudentUniversity(Student):
    def newMethod(self):
        print("new")
student3=StudentUniversity()
student3.getStudent()#it is the method of student
