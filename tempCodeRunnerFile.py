#creating a basic calculator 
print("*********************Calculator**********************")
print("what do you want to do:")
print("1.add \n2.subst \n3.mul \n4.div  ")


class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1 
        self.num2 = num2 

    def add_number(self):
        return self.num1 + self.num2

    def subst_number(self):
        return self.num1 - self.num2 

    def mul_number(self):
        return self.num1 * self.num2
    
    def div_number(self):
        return self.num1/self.num2


while True:
    
    
    user_choice = input("Choose the above option you like:")
    if user_choice == "1":
        user_input1 = int(input("Please enter the first input value:"))
        user_input2 = int(input("Please enter the second input value:"))
        output = calculator(user_input1,user_input2)
        print(f" The addition of the user value is {output.add_number()}")
        break

    elif user_choice == "2":
        user_input1 = int(input("Please enter the first input value:"))
        user_input2 = int(input("Please enter the second input value:"))
        output = calculator(user_input1,user_input2)
        print(f"The substraction of the user values is{output.subst_number()}")
        break
    elif user_choice == "3":
        user_input1 = int(input("Please enter the first input value:"))
        user_input2 = int(input("Please enter the second input value:"))
        output = calculator(user_input1,user_input2)
        print(f"The multiplication of the user valuse is{output.mul_number()}")
        break
    else:
        user_input1 = int(input("Please enter the first input value:"))
        user_input2 = int(input("Please enter the second input value:"))
        output = calculator(user_input1,user_input2)
        if user_choice == "4":
            if user_input2!= 0:
                   print(f"The division of the user values is {output.div_number()}")
            else:
                print("Can't divide by zero")
        else :
            print("Please enter the above options only")
       





  
