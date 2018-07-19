import serial

port = "COM3"
serialFromArduino = serial.Serial(port, 115200)
serialFromArduino.flushInput()
while True:
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
    print(BPM, IBI, SIGNAL)
