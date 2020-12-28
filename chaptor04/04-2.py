import csv, os

os.chdir(r'C:\Users\sklee\PycharmProjects\pythonProject\chaptor04')
f = open('a.csv', 'r', encoding='utf-8')
new = csv.reader(f)
new
a_list = []
for i in new:
    print(i)
    a_list.append(i)
print(a_list)
