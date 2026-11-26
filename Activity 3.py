def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    P / Q
print("Enter your operation: ")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
choice = input("Enter your choice of operation(A, B, C, or D): ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if choice == "a":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "b":
    print(num1, "+", num2, "=", subtract(num1, num2))
elif choice == "c":
    print(num1, "+", num2, "=", multiply(num1, num2))
elif choice == "d":
    print(num1, "+", num2, "=", divide(num1, num2))
else:
    print("Invalid choice.")