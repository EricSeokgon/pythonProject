import os

print(os.getcwd())

print(os.listdir())

folderFile = os.listdir()
type(folderFile)
print(folderFile)

f = open('a.txt', 'r', encoding='UTF8')
diary = f.read()
print(diary)

print(diary[:5])
f.close()

f1 = open('a.txt', 'a', encoding='UTF8')
f1.write(' 학교에 가지 않을 날이 올까?')
f1.close()

f2 = open('a.txt', 'r', encoding='UTF8')
print(f2.read())
f2.close()

f3 = open('abcde.txt', 'w', encoding='UTF8')
f3.write('I went to school today.')

with open('test.txt', 'w', encoding='UTF8') as f:
    f.write('오늘 나는 학교에 갔습니다.')
