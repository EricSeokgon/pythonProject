import os, re, codecs

os.chdir(r'C:\Users\sklee\PycharmProjects\pythonProject\chaptor03')
f = codecs.open('friends101.txt', 'r', encoding='utf-8')
script101 = f.read()
print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3]:
    print(item)

f.close()

f = open('monica.txt', 'w', encoding='utf-8')
monica = ''

for i in Line:
    monica += i
f.write(monica)
f.close()
