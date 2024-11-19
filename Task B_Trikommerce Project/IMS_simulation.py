from restock import restock_inventory
from sales import daily_sales
import random

def run_simulation(total_days, inventory_records):
    available_items = 2000  # Initial stock on Day 0

    for current_day in range(total_days):
        # If it's a restocking day, update inventory using the restock function
        if current_day % 7 == 0:
            restocked_units, available_items = restock_inventory(available_items, current_day)
        else:
            restocked_units = 0

        # If it's a sales day, update inventory using the sales function
        if current_day % 7 != 0:
            sold_units, available_items = daily_sales(available_items, current_day)
        else:
            sold_units = 0

        # Append to inventory records
        inventory_records.append((current_day, sold_units, restocked_units, available_items))

    return inventory_records
