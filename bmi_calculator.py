
# Beginner-Level BMI Calculator in Python

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):         # BMI categories based on WHO classification

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")

    # Step 1: Get valid user input
    weight = get_valid_input("Enter your weight in kilograms: ")
    height = get_valid_input("Enter your height in meters: ")

    # Step 2: Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Step 3: Classify BMI
    category = classify_bmi(bmi)

    # Step 4: Display result
    print(f" Your BMI is: {bmi:.2f}")
    print(f" BMI Category: {category}")

if __name__ == "__main__":
    main()
