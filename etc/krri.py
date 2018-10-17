import csv


f = open('Graph8_Wave_Tshort.csv', 'w', encoding='utf-8', newline='')
wf = csv.writer(f)

arr = [[""]*15 for i in range(600000)]
setting = [[""]*8 for i in range(27)]

for i in range(0, 4):
    for j in range(0, 10):
        try:
            rname= "Graph8_Wave_Tshort_00" + str(i) + str(j) + ".csv"
            print(rname)
            rf = open(rname)
            reader = csv.reader(rf, delimiter=',')
            reader = list(reader)
            if i==0 and j==0:
                for k in range(0,27):
                    setting[k] = reader[k]
            for k in range(27, 60027):
                arr[k-27 + j*60000][i*3 +1] = reader[k][1]
        except:
            pass
print(setting)
for i in range(0, 27):
    wf.writerow(setting[i])
for i in range(0, 600000):
    wf.writerow(arr[i])
