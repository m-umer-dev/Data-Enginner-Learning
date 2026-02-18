import csv

def extract_cust(path):
    try:
        with open(path,newline='') as f:
            customer_data = list(csv.DictReader(f))
            return customer_data
    except FileNotFoundError:
        return []
    

def extract_order(path):
    try:
        with open(path,newline='') as f:
            order_data = list(csv.DictReader(f))
            return order_data
    except FileNotFoundError:
        return []
    
def transform(cust_data, order_data):
    cleaned_cust = []
    cleaned_order = []
    final_data = []

    for row in cust_data:
        try:
            customer_id = int(row["customer_id"].strip())
            name = row["name"].strip()
            city = row["city"].strip()
        except:
            continue

        if not city:
            continue

        cleaned_cust.append({
            "customer_id": customer_id,
            "name": name,
            "city": city
        })

    # Create lookup dictionary (Very Important Technique 🔥)
    cust_lookup = {c["customer_id"]: c for c in cleaned_cust}

    for row in order_data:
        try:
            order_id = int(row["order_id"].strip())
            customer_id = int(row["customer_id"].strip())
            amount = int(row["amount"].strip())
        except:
            continue

        if amount < 0:
            continue

        if customer_id not in cust_lookup:
            continue

        customer = cust_lookup[customer_id]

        final_data.append({
            "order_id": order_id,
            "customer_name": customer["name"],
            "city": customer["city"],
            "amount": amount
        })

    return final_data

def load(path,data): 
    try: 
        with open(path,'w',newline='') as f: 
            writer = csv.DictWriter(
                f,
                fieldnames=["order_id","customer_name","city","amount"]) 
            writer.writeheader() 
            writer.writerows(data) 
    except FileNotFoundError: 
        return []



cust_data = extract_cust('customers.csv')
order_data = extract_order('orders.csv')
business = transform(cust_data,order_data)
load('final_data.csv',business)