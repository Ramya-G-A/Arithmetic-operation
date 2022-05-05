class aithmetic_operations:

    def addition(self,a,b):#function for addition
        sum=a+b
        print(sum)

    def subtraction(self,a,b):#function for subtraction
        diff=a-b
        print(diff)
    
    def division(self,a,b):
        if b!= 0:
            quotient= a/b
            print(quotient)
        else:
            print("divide by 0 exception")