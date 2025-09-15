import csv
from collections import defaultdict
from itertools import islice

def summarize_orders(csv_path):
    totals = defaultdict(float)
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip rows missing required fields
            if not all(field in row and row[field] for field in ['customer', 'amount']):
                continue
            try:
                amount = float(row['amount'])
            except ValueError:
                continue  # Skip rows with invalid amount
            customer = row['customer']
            totals[customer] += amount

    # Print results sorted by customer name
    for customer in sorted(totals):
        print(f"{customer}: {int(totals[customer]) if totals[customer].is_integer() else totals[customer]}")

# --- TESTS ---
def create_sample_csv(path, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['order_id', 'customer', 'amount'])
        writer.writerows(rows)

if __name__ == "__main__":
    # Small dataset test
    sample_rows = [
        [1, 'Alice', 120],
        [2, 'Bob', 90],
        [3, 'Alice', 60],
        [4, 'Charlie', ''],         # Malformed: missing amount
        [5, '', 50],                # Malformed: missing customer
        [6, 'Bob', 'not_a_number']  # Malformed: invalid amount
    ]
    create_sample_csv('orders_small.csv', sample_rows)
    print("Small dataset summary:")
    summarize_orders('orders_small.csv')

    