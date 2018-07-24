import serial
import sqlite3

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
port = "COM3"

#Input Serial
serialFromArduino = serial.Serial(port, 115200)
serialFromArduino.flushInput()

while True:
    #Serial Parsing
    input = serialFromArduino.readline()
    input = str(input)
    input = input.split(',')

    BPM = str(input[0])
    IBI = int(input[1])
    SIGNAL = str(input[2])

    BPM = str(BPM.split("'")[1])
    SIGNAL = str(SIGNAL.split("\\")[0])

    BPM = int(BPM)
    SIGNAL = int(SIGNAL)

    #Serial Insert to DB
    cur.execute("INSERT INTO DOGS_DATA(name, IBI, BPM, SIGNAL) VALUES(?, ?, ?, ?)", (name, IBI, BPM, SIGNAL))
