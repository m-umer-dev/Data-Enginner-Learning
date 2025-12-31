with open("transection.txt","r") as f1, open("filtered_transection.txt","w") as f2:
    for line in f1:
        name, amount = line.strip().split(",")
        amount = int(amount)
        if amount >= 100:
            f2.write(line)