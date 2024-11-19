import csv
from utils import delete_existing_report
from report_generation import generate_report
from IMS_simulation import run_simulation

def check_report_correctness():
    file = "inventory_report_Tshirts.csv"
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip the header
        data = list(reader)

    initial_stock = 2000  # Initial stock at the beginning of the simulation
    total_restocked = sum(int(row[2]) for row in data)  # Sum of restocked units
    total_sold = sum(int(row[1]) for row in data)  # Sum of sold units
    last_remaining_units = int(data[-1][3]) if data else initial_stock  # Remaining units in the last recorded day

    # Calculate the expected remaining units
    expected_remaining_units = initial_stock + total_restocked - total_sold

    if expected_remaining_units != last_remaining_units:
        print(f"Error: Totals do not match in file {file}. Expected {expected_remaining_units}, found {last_remaining_units}")
    else:
        print("ALL CHECKS PASSED :) for file {file}")


def report_check():
    total_days = 50
    inventory_records = []
    run_simulation(total_days, inventory_records)  # Ensure this function is updated correctly
    generate_report(inventory_records)  # Make sure this generates the correct CSV
    check_report_correctness()
