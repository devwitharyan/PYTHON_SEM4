# WAP to create custom module an to define a  fucntion to check for odd or even number

def odd_even_function(n):
    
    if (n == 0):
        return "Number is 0"
    else:
        if(n % 2== 0):
            return "Number is even"
        elif(n % 2 == 1):
            return "Number is odd"
        else:
            return "input is invalid"
    