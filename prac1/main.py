
def greet(name):
    return f"Hello, {name}!"


def main():
    # Variables and Data Types
    name = "Gaurav"
    age = 20
    is_student = True

    # Basic Operations
    next_year_age = age + 1
    age_status = "young" if age < 30 else "adult"

    # Function Call
    greeting = greet(name)

    # Output
    print(greeting)
    print(f"Next year, {name} will be {next_year_age} years old and is considered {age_status}.")
    print(f"Is {name} a student? {'Yes' if is_student else 'No'}")
    print(f"{name} can tell the numbers from 1 to 10 as: ")
    for i in range(1, 11):
        print(f"{i} ", end=", ")


if __name__ == "__main__":
    main()
