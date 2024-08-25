import csv
import sympy as sp
from uncertainties import ufloat

def load_data_from_csv(filename="data.csv"):
    """Loads data from a CSV file.

    Args:
        filename (str, optional): The name of the CSV file. Defaults to "data.csv".

    Returns:
        list: A list of tuples, where each tuple represents a row of data.
    """
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            data = [tuple(float(value) for value in row) for row in reader]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except ValueError:
        print("Error: Invalid data format in the CSV file.")
        return []
    return data

def calculate_uncertainty(formula, values, uncertainties):
    # ... (same as before)

def main():
    formulas = load_formulas()

    # ... (same as before)

    data = load_data_from_csv()

    results = []
    for row in data:
        try:
            values = {var_name: value for i, (var_name, value) in enumerate(zip(variables, row[::2]))}
            uncertainties = {var_name: uncertainty for i, (var_name, uncertainty) in enumerate(zip(variables, row[1::2]))}
            uncertainty_evaluated = calculate_uncertainty(formula_str, values, uncertainties)
            result = ufloat(formula_str.subs(values), uncertainty_evaluated)
            results.append(result)
        except (ValueError, ZeroDivisionError, sympy.SympifyError) as e:
            print(f"Error processing row: {row}")
            print(f"Error message: {e}")

    print("Results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
