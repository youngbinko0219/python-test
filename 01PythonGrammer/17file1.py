print('='*30)
print('myfile001.txt')
print('='*30)

f_open = open('./saveFiles/myfile001.txt',mode = 'wt', encoding = 'utf-8')
for i in range(1,21):
    data = '%d번째 줄입니다.\n'%i
    f_open.write(data)
f_open.close()

f_read = open('./saveFiles/myfile001.txt',mode = 'rt', encoding = 'utf-8')
while True:
    line = f_read.readline()
    if not line: break
    print(line)
f_read.close()

f_add = open('./saveFiles/myfile001.txt',mode = 'at', encoding = 'utf-8')
f_add.write('추가하는 내용입니다.')
f_add.writelines(['줄바꿈은 되나요?\n', '안되면 개행문자를 넣어주세요.'])
f_add.write('마지막 라인입니다.')
f_add.close()

print('='*30)
print('myfile002.txt')
print('='*30)

with open('./saveFiles/myfile002.txt',mode = 'wt', encoding = 'utf-8') as myfile:
    for i in range(1,10):
        data = '%d 라인 입력합니다.\n' % i
        myfile.write(data)
with open('./saveFiles/myfile002.txt',mode = 'rt', encoding = 'utf-8') as myfile:
    line = None
    while line != '':
        line = myfile.readline()
        print(line.strip('\n'))