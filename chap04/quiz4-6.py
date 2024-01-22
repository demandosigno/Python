numbers = [1 ,2]
print(numbers)
print(numbers[0])
print(type(len(numbers)))
i = len(numbers) - 1
print(numbers[i])
print(numbers[len(numbers) - 1])
print(numbers[len(numbers) - 2])
print(type(numbers[len(numbers) - 2]))
print(numbers[len(numbers) - 1] + numbers[len(numbers) - 2])
for max in range(3) :
    numbers.append(numbers[len(numbers)-1]+numbers[len(numbers)-2])
    print(numbers[max+2])
print(numbers)

ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratios.append(numbers[count + 1] / numbers[count])
print(ratios)

for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)