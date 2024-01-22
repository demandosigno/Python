# i = 1
# j = 1
# for i <= 9:
#     for j <= 9:
#         print(i * j, end='')
for i in range(9):
    for j in range(9):
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')

print(' ')

for k in range(9):
    if (k+1) % 2 == 0:
        continue
    for l in range(9):
        print(f'{k+1}×{l+1}={(k+1)*(l+1)}')

print(' ')

for m in range(9):
    if (m+1) % 2 == 0:
        continue
    for n in range(9):
        if (m+1)*(n+1) > 50:
            break
        print(f'{m+1}×{n+1}={(m+1)*(n+1)}')