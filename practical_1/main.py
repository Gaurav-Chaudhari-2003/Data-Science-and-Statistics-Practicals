def greet(name):
    return f"Hello, {name}!"


def main():
    # Variables and Data Types
    name = "Alice"
    age = 25
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


if __name__ == "__main__":
    main()
