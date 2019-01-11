import csv

arr = [[0] for i in range(4)]
idx = [[0] for i in range(4)]
for num in range(1, 4):
    fname = "TEST "+str(num)+".csv"
    file = open(fname)
    data = csv.reader(file, delimiter=',')
    data = list(data)
    print(len(data))
    for elem in range(17, len(data)):
        try:
            arr[num].append(float(data[elem][4]))
            try:
                if abs(arr[num][len(arr[num]-5 : arr[num])-1])-:len(arr[num])-1]-arr[num][len(arr[num]-10 : arr[num])-61]) <=0.002:
                    idx[num].append(elem)
            except Exception as e:
                print("1",e)
                continue
        except Exception as e:
            print("2",e)
            continue
print(idx)
f = open("TESTSUM.csv", 'w', encoding='utf-8', newline='')
wf = csv.writer(f)

for j in range(max(len(arr[1]), len(arr[2]), len(arr[3]))):
    try:
    wf.writerow([arr[1][j],arr[2][j],arr[3][j]])
