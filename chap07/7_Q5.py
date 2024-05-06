import os
print(os.getcwd())

file_r = open('./chap07/sample.txt', 'r')
# file = open('.\chap07\sample.txt', 'r')
# file = open('.\\chap07\\sample.txt', 'r')
file_w = open('./chap07/copy.txt', 'w')

for line in file_r:
    file_w.write(line)
file_r.close()
file_w.close()