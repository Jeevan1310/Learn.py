print("Lets start calculating...")
def script():
    # define functions  
    def add(x, y):  
        return x + y 
    def subtract(x, y): 
        return x - y 
    def multiply(x, y):  
        return x * y 
    def divide(x, y): 
        return x / y 
    def percentage(x,y):
        return (x/y)*100
    def squart(x):
        return 
    def power(x,y):
        return
    print("Select operation.")  
    print("1.Add")  
    print("2.Subtract")  
    print("3.Multiply")  
    print("4.Divide")
    print("5.percentage")
    print("6.squareroot")
    print("7.power of n") 
  
    choice = input("Enter choice(1/2/3/4/5/6/7):")  
  
    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))  
  
    if choice == '1':  
        print(num1,"+",num2,"=", add(num1,num2))  
    elif choice == '2':  
        print(num1,"-",num2,"=", subtract(num1,num2))  
  
    elif choice == '3':  
        print(num1,"*",num2,"=", multiply(num1,num2))  
    elif choice == '4':  
        print(num1,"/",num2,"=", divide(num1,num2))
    elif choice == '5':
        print("percentage=",percentage(num1,num2),"%")
    elif choice == '6':
        number = int(input("enter a number: "))
        sqrt = number ** 0.5
        print("square root:", sqrt)
    elif choice == '7':
        num = int(input("Enter the number of which you have to find power: "))
        pw = int(input("Enter the power: "))
        kj = 1
        for n in range(pw):
            kj = kj*num
        print(kj)
    else:  
        print("Invalid input") 
    restart =input("Would you like to continue ")
    if restart == "yes" or restart == "y":
            script()
    if restart == "n" or restart == "no":
            print ("Thank you for using me")
script()