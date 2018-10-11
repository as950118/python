import serial
import sqlite3
import csv
import time
#test
f = open('golden2.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

#My Dog Name
name = "Popcorn"

#Connect DB
conn = sqlite3.connect("Dogs_DB.db")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE DOGS_DATA(num integer primary key autoincrement, name text not null, IBI integer not null, BPM integer not null, SIGNAL integer not null);")
    print("Success")
except:
    print("Already Exists")
    pass

#Set Port
port = "COM4"

#Input Serial
serialFromArduino = serial.Serial(port, 115200)
serialFromArduino.flushInput()

starttime = time.time()
wr.writerow([starttime])
while 1:
    try:
        #Serial Parsing
        input = serialFromArduino.readline()
        input = str(input)
        input = input.split(',')

        BPM = str(input[0])
        IBI = int(input[1])
        SIGNAL = str(input[2])
        temperature = str(input[3])

        BPM = str(BPM.split("'")[1])
        SIGNAL = str(SIGNAL.split("\\")[0])
        temperature = str(temperature.split("\\")[0])

        BPM = int(BPM)
        SIGNAL = int(SIGNAL)

        #test
        print(BPM, IBI,SIGNAL, temperature)
        wr.writerow([time.time()-starttime, BPM, IBI, SIGNAL, temperature, 0])
    except:
        wr.writerow([time.time()-starttime, 0, 0, 0, 0, 1])
    #Serial Insert to DB
    #cur.execute("INSERT INTO DOGS_DATA(name, IBI, BPM, SIGNAL) VALUES(?, ?, ?, ?)", (name, IBI, BPM, SIGNAL))
f.close()
