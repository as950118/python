import csv

f = open('Graph8_Wave_Tshort_0000.csv')
reader = csv.reader(f, delimiter=',')
reader = list(reader)
for i in range(27, 60027):
    print(reader[i][1])
