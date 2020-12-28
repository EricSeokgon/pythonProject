import os, re
import usecsv

os.chdir(r'C:\Users\sklee\PycharmProjects\pythonProject\chaptor04')
total = usecsv.opencsv('popSeoul.csv')
for i in total[:5]:
    print(i)
