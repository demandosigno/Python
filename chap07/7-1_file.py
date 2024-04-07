text = input('何を記録しますか? >>')
file = open('diary4.txt', 'a', encoding='utf-8')
file.write(text + '\n')
file.close()