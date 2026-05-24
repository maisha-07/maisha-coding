def avg(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total/ len (numbers)

age = [10,20,24,45,56]
result = (avg(age))
print(f"average of age = {result}")