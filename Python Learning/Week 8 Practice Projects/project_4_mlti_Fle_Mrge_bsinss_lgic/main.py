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
    


print(extract_cust('customers.csv'))
print(extract_order('orders.csv'))