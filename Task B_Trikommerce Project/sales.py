# sales.py
import random

def daily_sales(available_items, current_day):
    """
    Handles daily sales if it's not a restocking day.

    :param available_items: Available items before sales
    :param current_day: Current day of the simulation
    :return: Sold units and updated available items
    """
    if current_day % 7 != 0:  # Sales occur only on non-restocking days
        sold_units = random.randint(0, min(200, available_items))
        available_items -= sold_units
    else:
        sold_units = 0
    return sold_units, available_items
