print ("PRIME NUBER CHECKER:")
print ("write the num to check if it is prime number or not")
n =int(input("......................."))
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
            
    return True 
print (is_prime(n))

  

print("==============================================================================================")
def calculator(num1, num2, op):
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation"


a = float(input("a = ........................ "))
b = float(input("b = ........................ "))

operation = input("operation = ........................ ")


result = calculator(a, b, operation)
print("Result =", result)

