'''
def input(a, b, c):
    max_number = max(a, b, c)
    print(max_number)

input(2, 6, 4)
'''

nums = list()
for n in range(3):
    data = int(input(f'{n + 1}個目の整数を入力してください >> '))
    nums.append(data)
print(max(nums))