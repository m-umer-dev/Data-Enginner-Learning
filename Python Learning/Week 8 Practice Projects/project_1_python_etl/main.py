import csv

def extract(path):
    try:
        with open(path,newline='') as f:
            return list(csv.DictReader(f))
    except:
        return FileNotFoundError
    
def transform(data):
    cleaned = []
    for row in data:
        if not row["city"].strip():
            continue
        try:
            name = row["name"]
            amount = int(row["amount"].strip())
        except ValueError:
            continue
        if amount < 0 :
            continue
        if amount >= 1000:
            status = "high"
        elif amount >= 500:
            status = "medium"
        else:
            status = "low"
        cleaned.append({
            "name" : name,
            "amount" : amount,
            "status" : status
        })
    return cleaned

def load(path,data):
    with open(path,'w',newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "amount", "status"]
        )
        writer.writeheader()
        writer.writerows(data)

def run_pipeline():
    data = extract('sales_raw.csv')
    business = transform(data)
    load('cleaned_sales.csv',business)
    
run_pipeline() 