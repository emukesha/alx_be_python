number = input("Enter a number to see its multiplication table: ")

for num in range(1,11):
    prod = int(number) * num
    print(f"{number} * {num} = {prod}")