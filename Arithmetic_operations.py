class arithmetic_operations:

    def addition(self,num1,num2):#function for addition
        result=num1+num2
        print(result)

     def subtraction(self,a,b):#function for subtraction
        result=a-b
        print(result)

    def multiplication(self,a,b):#function for multiplication
        result=a*b
        print(result)
    
    def division(self,a,b):#function for division
        if b!= 0:
            quotient= a/b
            print(quotient)
        else:
            print("divide by 0 exception")
