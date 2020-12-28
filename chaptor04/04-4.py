import csv, os

os.chdir(r'C:\Users\sklee\PycharmProjects\pythonProject\chaptor04')
import usecsv
apt=usecsv.switch(usecsv.opencsv('apt_202012.csv'))

print(apt[:3])