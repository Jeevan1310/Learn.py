print("welcome to world of coding")
print("please fill the details")
name=input("enter your name -")
age=input("enter your age -")
designation=input("enter your designation -")
list=[]
for i in range(3):
    skills=input("please enter your skills:\n")
    list.append(skills)
print("my name is :",name)
print("my age is :",age)
print("I am ",designation)
print('i am mastered in ',*list,sep= "," )
