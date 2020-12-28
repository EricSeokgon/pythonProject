import csv, os, re

os.chdir(r'C:\Users\sklee\PycharmProjects\pythonProject\chaptor04')
import usecsv

apt = usecsv.switch(usecsv.opencsv('apt_202012.csv'))

print(apt[:3])

print(len(apt))

for i in apt[:6]:
    print(i[0])

for i in apt[:6]:
    print(i[0], i[4], i[-4])

new_list = []
for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
            print(i[0], i[4], i[-4])
    except:
        pass
usecsv.writecsv('over120_lower3000.csv', new_list)
