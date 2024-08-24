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
    formulas = load_formulas()

    print("Available formulas:")
    for name, formula in formulas.items():
        print(f"- {name}: {formula}")

    formula_name = input("Enter the formula name: ")
    formula_str = formulas[formula_name]

    # Rest of your code using formula_str
    print(formula_str)
if __name__ == "__main__":
    main()
