numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = len(numbers)
b=[]

for number in numbers:
    if number is not None:
        b.append(number)

srznach = sum(b) / a

i = 0

while i < len(numbers):
    if numbers[i] is None:
        numbers[i] = srznach
    i += 1


print("Измененный список:", numbers)
