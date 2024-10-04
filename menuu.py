def print_menu():
    print("MENU:")
    print("1. Calculate the sum of a list")
    print("2. Print a pattern")
    print("3. Print numbers 1-10")
    print("4. Print multiplication table of a given number")
    print("5. Display numbers divisible by 3 from a list")
    print("6. Calculate the sum of given numbers")
    print("7. Print the pattern (descending)")
    print("8. Print all even numbers in a range")
    print("9. Print the star pattern")
    print("10. Calculate the cube of a number")
    print("0. Exit")

def sum_of_list():
    num_list = [10, 20, 30, 40, 50]
    print(f"Sum: {sum(num_list)}")

def print_pattern():
    for i in range(2, 5):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def print_numbers():
    for i in range(10, 0, -1):
        print(i)

def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

def divisible_by_3():
    num_list = [3, 1, 2, 6, 11, 7]
    print([num for num in num_list if num % 3 == 0])

def sum_of_given_numbers():
    num_list = [10, 20, 30]
    print(f"Sum: {sum(num_list)}")

def print_descending_pattern():
    for i in range(3, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def even_numbers():
    range_limit = int(input("Enter range limit: "))
    even_nums = [num for num in range(1, range_limit + 1) if num % 2 == 0]
    print(even_nums)

def star_pattern():
    for i in range(1, 6):
        print('*' * i)

def calculate_cube():
    num = int(input("Enter a number: "))
    print(f"The cube of {num} is {num**3}")

def menu():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            sum_of_list()
        elif choice == '2':
            print_pattern()
        elif choice == '3':
            print_numbers()
        elif choice == '4':
            multiplication_table()
        elif choice == '5':
            divisible_by_3()
        elif choice == '6':
            sum_of_given_numbers()
        elif choice == '7':
            print_descending_pattern()
        elif choice == '8':
            even_numbers()
        elif choice == '9':
            star_pattern()
        elif choice == '10':
            calculate_cube()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please select again.")

# Call the menu
menu()
