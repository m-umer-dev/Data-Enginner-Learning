with open("sales.csv","r") as f:
    data = f.readlines()

with open("processed_data.csv","w") as f:
    f.write("name,amount\n")

    for line in data[1:]:
        name, amount = line.strip().split(",")
        amount = int(amount) * 1.1
        f.write(f"{name},{amount}\n")
