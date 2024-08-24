import sympy as sp
import os
from uncertainties import ufloat

def save_formula(formula_name, formula, filename="formulas.txt"):
    with open(filename, "a") as file:
        file.write(f"{formula_name}: {formula}\n")

def load_formulas(filename="formulas.txt"):
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "formulas.txt")
    formulas = {}
    with open(file_path, "r") as file:
        for line in file:
            name, formula = line.strip().split(": ")
            formulas[name] = formula
    return formulas


def main():
    #Get the formulas from the file
    formulas = load_formulas()

    # Get the formula from the user
    print("Available formulas:")
    for name, formula in formulas.items():
        print(f"- {name}: {formula}")

    formula_name = input("Enter the formula name: ")
    formula_str = formulas[formula_name]

    formula = sp.simplify(formula_str)

    # Create dictionaries to store variable values and uncertainties
    values = {}
    uncertainties = {}

    # Ask for variable values and uncertainties
    while True:
        var_name = input(f"Enter variable name (e.g., x, y): ")
        if not var_name:
            break  # Stop input when user enters an empty name

        value = float(input(f"Enter value for {var_name}: "))
        uncertainty = float(input(f"Enter uncertainty for {var_name}: "))

        values[var_name] = value
        uncertainties[var_name] = uncertainty

    # Substitute values and uncertainties into the formula
    substituted_formula = formula.subs(values)

    # Calculate the overall uncertainty
    total_uncertainty = 0
    for var_name, uncertainty in uncertainties.items():
        partial_derivative = sp.diff(formula, var_name)
        total_uncertainty += (partial_derivative * uncertainties[var_name])**2

    total_uncertainty = sp.sqrt(total_uncertainty)

    #Enssure that the value of total_uncertainty is a number
    #total_uncertainty.evalf(subs=values)
    uncertainty_evaluated = total_uncertainty.subs(values)

    # Create a ufloat object with the result
    result = ufloat(substituted_formula, uncertainty_evaluated)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
