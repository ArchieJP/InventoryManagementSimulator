# restock.py
def restock_inventory(available_items, current_day):
    """
    Restocks inventory if it's a restocking day (every 7th day).

    :param available_items: Available items before restocking
    :param current_day: Current day of the simulation
    :return: Restocked units and updated available items
    """
    if current_day % 7 == 0:  # Restocking happens every 7th day
        restocked_units = 2000 - available_items
        available_items = 2000
    else:
        restocked_units = 0
    return restocked_units, available_items
