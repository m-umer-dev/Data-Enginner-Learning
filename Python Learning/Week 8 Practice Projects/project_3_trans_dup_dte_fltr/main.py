import csv

def extract(path):
    try:
        with open(path,newline='') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []
    

def transform(data):
    dup_clean = set()
    cleaned = []
    for row in data:
        try:
            transaction_id = int(row["transaction_id"].strip())
            customer = row["customer"].strip()
            amount = int(row["amount"].strip())
            date = row["date"].strip()
            year = int(row["date"].split("-")[0].strip())
        except (KeyError,ValueError):
            continue
        if amount < 0:
            continue
        if year != 2024:
            continue
        if transaction_id in dup_clean:
            continue
        dup_clean.add(transaction_id)
        if amount >= 1000:
            size = "Large"
        elif amount >= 500:
            size = "Medium"
        else: 
            size = "Small"
        cleaned.append({
            "transaction_id" : transaction_id,
            "customer" : customer,
            "amount" : amount,
            "date" : date,
            "size" : size
        })

    return cleaned



def load(path,data):
    try:
        with open(path,'w',newline='') as f:
            writer = csv.DictWriter(f,fieldnames=["transaction_id","customer","amount","date","size"])
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        return []
    

data = extract('transactions.csv')
business = transform(data)
load('transactions_cleaned.csv',business)