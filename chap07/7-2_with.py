text = input('今日は何をした? >>')
# with open('diary6.txt', 'a') as file:
with open('diary5.txt', 'a', encoding='utf-8') as file:
    file.write(text + '\n')