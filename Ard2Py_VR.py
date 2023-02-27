import serial
print(serial.__version__)

ser = serial.Serial(port='COM4', baudrate=115200, timeout=1)

while True:
    while ser.inWaiting() == 0:
        pass
    VR1 = ser.readline()
    #print(VR1)
    VR1 = str(VR1, 'UTF-8')
    VR1 = VR1.strip('\r\n')
    print(VR1)

ser.close()
