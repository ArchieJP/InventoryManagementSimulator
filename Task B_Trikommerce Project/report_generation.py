import csv

def generate_report(inventory_records):
    file_path = "inventory_report_Tshirts.csv"
    
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["Day", "Sold Units", "Restocked Units", "Available Units"])
        # Write inventory records
        for record in inventory_records:
            writer.writerow(record)
