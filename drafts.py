import json

contacts = [{"name": "waga", "tel": "123"}]
def save_2_file():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)