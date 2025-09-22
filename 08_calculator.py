import math

def get_numbers(prompt="Enter a number: ", count=2):
    numbers = []
    for i in range(1, count + 1):
        try:
            num = float(input(f"{prompt}{i}: "))
            numbers.append(num)
        except ValueError:
            print("❌ Invalid input, please enter a number.")
            return None
    return numbers

def addition():
    count = int(input("How many numbers to add? "))
    nums = get_numbers(count=count)
    return sum(nums) if nums else None

def subtraction():
    count = int(input("How many numbers to subtract? "))
    nums = get_numbers(count=count)
    return nums[0] - sum(nums[1:]) if nums else None

def multiplication():
    count = int(input("How many numbers to multiply? "))
    nums = get_numbers(count=count)
    if nums is None:
        return None
    result = 1
    for n in nums:
        result *= n
    return result

def division():
    nums = get_numbers(count=2)
    if nums is None:
        return None
    try:
        return nums[0] / nums[1]
    except ZeroDivisionError:
        print("❌ Division by zero is not possible.")
        return None

def modulus():
    nums = get_numbers(count=2)
    if nums is None:
        return None
    try:
        return nums[0] % nums[1]
    except ZeroDivisionError:
        print("❌ Modulus by zero is not possible.")
        return None

def exponent():
    nums = get_numbers(prompt="Enter number ", count=2)
    return nums[0] ** nums[1] if nums else None

def sqrt():
    try:
        num = float(input("Enter the number to find the square root: "))
        if num < 0:
            print("❌ Cannot take square root of negative number.")
            return None
        return math.sqrt(num)
    except ValueError:
        print("❌ Invalid input.")
        return None

# Main menu
while True:
    print("\n__Calculator__")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Advanced options")
    print("6. Quit")

    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        print("Sum:", addition())
    elif choice == "2":
        print("Difference:", subtraction())
    elif choice == "3":
        print("Product:", multiplication())
    elif choice == "4":
        print("Quotient:", division())
    elif choice == "5":
        print("Advanced options:\n1. Modulus\n2. Exponent\n3. Square Root")
        adv_choice = input("Enter your choice: ").strip()
        if adv_choice == "1":
            print("Modulus:", modulus())
        elif adv_choice == "2":
            print("Exponent:", exponent())
        elif adv_choice == "3":
            print("Square Root:", sqrt())
        else:
            print("❌ Invalid input.")
    elif choice == "6":
        print("Thanks, have a great day ❤️")
        break
    else:
        print("❌ Invalid choice T_T")
