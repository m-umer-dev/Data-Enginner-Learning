import csv

def extract(path):
    try:
        with open(path,newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def transform(data):
    total_spent = {}
    cleaned = []
    for row in data:
        try:
            amount = int(row["amount"].strip())
            customer = row["customer"]
        except ValueError:
            continue
        if amount < 0:
            continue
        if customer not in total_spent:
            total_spent[customer] = 0
        total_spent[customer] += amount

    for customer, total in total_spent.items():
        if total >= 1000:
            category = "VIP"
        elif total >= 500:
            category = "Regular"
        else:
            category = "Low"
        cleaned.append({
            "customer" : customer,
            "total_spent" : total,
            "category" : category
        })
        
    return cleaned


def load(path,data):
    try:
        with open(path,'w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=["customer","total_spent","category"])
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        return []
    

data = extract('orders.csv')
business = transform(data)
load('customer_summary.csv',business)