def main():
    print("Welcome to the Collaborative Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    # Add more operations as students contribute
    choice = int(input("Enter your choice: "))
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    else:
        print("Invalid choice!")

# Example function
def add(a, b):
    return a + b


def subtract(a,b):
    return a-b


# More functions to be added by students

if __name__ == "__main__":
    main()
