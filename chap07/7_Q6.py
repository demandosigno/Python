# import random
from random import randint

print('数当てゲームを始めます。3桁の数を当ててください！')
answer = list()
prediction = list()

for n in range(3):
    answer.append(randint(0, 9))
print(answer)

is_continue = True
while is_continue == True:
    prediction = list()
    for n in range(3):
        prediction.append(int(input(f'{n + 1}桁目の予想を入力(0~9) >> ')))
    print(prediction)

    hit = 0
    for n in range(3):
        if answer[n] == prediction[n]:
            hit += 1

    print(f'{hit}ヒット！{3-hit}ボール！\n')

    if(hit == 3):
        print('正解です！')
        is_continue = False
        # break
    else:
        is_continue = int(input('続けますか？ 1：続ける 2：終了 >> '))
        if is_continue == 2:
            is_continue = False