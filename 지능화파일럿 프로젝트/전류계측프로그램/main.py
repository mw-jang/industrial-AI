import self as self
import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial(
    port='COM3',
    baudrate=230400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=1)

print("connected to: " + ser.portstr)

RX485RXArray = []
R_Current = []
S_Current = []
T_Current = []

count = 0

end = 2952

while True:
    for mHex in ser.read(1):
        RX485RXArray.append(mHex)
        #RX485RXArray.insert(count, mHex).

        count = count + 1

        if count == 192:
            count = 0

            ser.flushInput()

            RX485RXArrayCOPY = RX485RXArray.copy()
            del RX485RXArray[:]
            R_Current = RX485RXArrayCOPY[0:64]
            S_Current = RX485RXArrayCOPY[64:128]
            T_Current = RX485RXArrayCOPY[128:192]

            print(end)
            print("R :", R_Current)
            print("S :", S_Current)
            print("T :", T_Current)

            plt.figure(figsize=(12, 8))

            xaxis = np.arange(0, 64)

            plt.plot(xaxis, R_Current, 'r-', label='R')
            plt.plot(xaxis, S_Current, 'g-', label='S')
            plt.plot(xaxis, T_Current, 'b-', label='T')
            plt.legend()

            #plt.show()

            plt.savefig('역상파형/{0}.png'.format(end))
            if end >= 3000:
                ser.close()
                break
            end = end+1


