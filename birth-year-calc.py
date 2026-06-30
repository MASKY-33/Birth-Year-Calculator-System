# Learning "try...except" inside the "while-loop" using (math - substracting)


while True:
    age = input("Give in your age: ")

    if age == "stop":
        break

    try:
        age_digit = int(age)
        born_year = 2026 - age_digit
        print(f"You were born in: {born_year}")

    except ValueError:
        print("Wrong, only put in numbers.")
    
    except TypeError:
        print("System error: Incorrect datatype used during the calculation.")
