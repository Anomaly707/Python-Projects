#Simple calculator
print("Welcome to Calculator")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
while True:
 print("1-Addition")
 print("2-Substraction")
 print("3-Multipilcation")
 print("4-Divion")
 print("5-Mod")
 print("E-Exit")
 print("R-Restart")
 x=input("Choose your operation")
 if x.upper()=="E":
   print("Goodbye!")
   break
 elif x.upper()=="R":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    continue
 elif x=="1" :
    c=a+b
    print(f"The sum of {a} and {b} number is:",c)
 elif x=="2":
  print(f"The substraction of {a} and {b} is:",a-b)
 elif x=="3":
     print(f"The multipication of {a} and {b} is:",a*b)
 elif x=="4":
   if b==0:
     print("Divion by zero is not possible")
   else:
    print(f"The divisor of {a} and {b} is:",a/b)
 
 elif x=="5":
   if b==0:
    print(" Mod by zero is not possible")
   else:
      print(f"The mod of {a} and {b} is:",a%b)
 else:
   print("Invaild operation E-Exit or R-Restart")
   