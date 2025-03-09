# Question Number 1
def collect_user_data():
    user_data = {}  # Dictionary to store user details

    # Get user input
    user_data["name"] = input("Enter your name: ").strip()
    user_data["age"] = input("Enter your age: ").strip()
    user_data["email"] = input("Enter your email: ").strip()
    user_data["favorite_number"] = input("Enter your favorite number: ").strip()

    # Validate email format
    if "@" not in user_data["email"] or "." not in user_data["email"]:
        print("Invalid email format. Please enter a valid email.")
        return collect_user_data()  # Ask for details again if invalid

    # Display formatted output
    print("\nUser Information:")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")

# Call function
collect_user_data()

# Question Number 2
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# User Input
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")

# Question Number 3
def convert_temperature(temp, scale):
    if scale.upper() == "C":
        return (temp * 9/5) + 32  # Convert Celsius to Fahrenheit
    elif scale.upper() == "F":
        return (temp - 32) * 5/9  # Convert Fahrenheit to Celsius
    else:
        return "Invalid scale! Use 'C' for Celsius or 'F' for Fahrenheit."

# User Input
temperature = float(input("Enter temperature value: "))
scale = input("Enter scale (C/F): ").strip().upper()
converted_temp = convert_temperature(temperature, scale)

print(f"Converted Temperature: {converted_temp}")


# Question Number 4
def find_max_min(numbers_list):
    return max(numbers_list), min(numbers_list)

# User Input
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

max_value, min_value = find_max_min(numbers)

print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")


# Question Number 5
def collect_student_data():
    students = []  # List to store student tuples

    # Collect data for 3 students
    for _ in range(3):
        name = input("Enter student name: ").strip()
        age = input("Enter student age: ").strip()
        grade = input("Enter student grade: ").strip()
        students.append((name, age, grade))  # Store as tuple

    # Convert list into dictionary
    student_dict = {student[0]: (student[1], student[2]) for student in students}

    # Display the dictionary
    print("\nStudent Data:")
    for name, data in student_dict.items():
        print(f"{name} - Age: {data[0]}, Grade: {data[1]}")

# Call function
collect_student_data()


# Question Number 6
def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)  # Ensure no negative quantity
    else:
        print(f"Item '{item}' not found in inventory.")

    return inventory_dict  # Return updated inventory

# Initialize inventory
inventory = {
    "Apples": 10,
    "Bananas": 5,
    "Oranges": 8,
    "Grapes": 12,
    "Mangoes": 7
}

# Display initial inventory
print("Initial Inventory:", inventory)

# User updates
for _ in range(3):
    item_name = input("Enter item name to update: ").strip().capitalize()
    quantity_change = int(input(f"Enter quantity to add/remove for {item_name} (use negative for removal): "))
    inventory = update_inventory(inventory, item_name, quantity_change)

# Display updated inventory
print("\nUpdated Inventory:", inventory)


