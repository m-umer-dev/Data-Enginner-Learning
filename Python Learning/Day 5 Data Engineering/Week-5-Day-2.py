import json

with open("user.json", "r") as f:
    users = json.load(f)

clean_users = []

for user in users:
    if user["age"] >= 18:
        user["status"] = "adult"
        clean_users.append(user)

with open("processed_user.json", "w") as f:
    json.dump(clean_users, f, indent=4)
