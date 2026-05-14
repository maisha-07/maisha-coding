phones = {"Maisha": "07111", "Hafiz": "07222", "Mom": "07333"}

name = input("name = ")

if name in phones:
    print(phones[name])
else:
    print("Not in phone book")
