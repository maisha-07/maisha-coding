
name = input("What is your name? ")
age = int(input("What is your age? "))

if age >= 100:
    print(f"Hello {name}, wow you are old!")
elif age >= 18:
    print(f"Hello {name}, you can vote")
else:
    print(f"Hello {name}, sorry you cannot vote")

