def int_input(msg):
    # 計算データの入力
    return int(input(f'{msg}を入力してください >>'))

def calc_payment(amount, people=2):
    # 割り勘の計算
    dnum = amount / people   # 総額を人数で割る(端数も保持)
    # print(dnum)
    pay = dnum // 100 * 100  # 100円未満を切り捨てる
    # print(pay)
    if dnum > pay:           # 元の値と比較して、
        pay = int(pay + 100) # 小さければ100円未満があったので上乗せ

    # 幹事の支払額の計算
    payorg = amount - pay * (people - 1)

    return [int(pay), int(payorg)]

def show_payment(pay, payorg, people=2):
    # 結果の表示
    print('*** 支払額 ***')
    print(f'1人あたり{pay}円({people}人)、幹事は{payorg}円です')

amount = int_input('支払い総額')
people = int_input('参加人数')
[pay, payorg] = calc_payment(amount, people)
show_payment(pay, payorg, people)