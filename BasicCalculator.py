def calculator(option):
    if(option in[1,2,3,4]):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))

        if(option==1):
            result=num1+num2
        elif(option==2):
            result=num1-num2
        elif(option==3):
            result=num1*num2    
        else:
            result=num1//num2
        return result
    else:
        print("Invalid option.Please select a valid option.")  
        
while(1):
    print("\nWelcome to the calculator world")
    print("1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    option=int(input("Please enter an option:"))
    result=0
    result=calculator(option)
    print("The result is: ",result)



