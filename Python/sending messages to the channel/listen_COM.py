import serial
ser = serial.Serial('COM9', 115200, timeout=0)

while ser.inWaiting():
             data = ser.read()
             print(data)
             continue