num=int(input("enter the nuber :"))
if (num%2)==0:
    print("{0} is even number".format(num))
    print ("multiplication table")
    for i in range(1,11):
        print(num,'x',i,'=',num*i)
else:
    print("{0} is odd number".format(num))
    print ("multiplication table")
    for i in range(1,11):
        print(num,'x',i,'=',num*i)