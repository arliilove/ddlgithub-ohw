#通过串口控制mCookie，与mCookie程序mCookieComTest.xml配合使用
import serial
import serial.tools.list_ports
import time

#打开链接mCookie的串口
print("hello serial")
ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    for q in p:
        print(q)
    if "SERIAL" in p[1] or "UART" in p[1]:
	    ser=serial.Serial(port=p[0])
	    break
    else :
	    print ("No Arduino Device was found connected to the computer")
#***************************************************************************
time.sleep(2)
f = open("songs.csv",'r')
data = f.read()
print(data)
data_list = data.split('\n')
print(data_list)
song1_list = data_list[0].split(',')
song2_list = data_list[1].split(',')
song3_list = data_list[2].split(',')
print("song1:",song1_list)
print("song2:",song2_list)
print("song3:",song3_list)
while True:
    command = input("Please enter the command: ")
    if command.strip() == "q":
        ser.close()
        break;
    elif command.strip() == song1_list[0]:
        for note in song1_list[1:]:
            ser.write(note.encode())
            time.sleep(1)
        note = '0'
        ser.write(note.encode())
    elif command.strip() == song2_list[0]:
        for note in song2_list[1:]:
            ser.write(note.encode())
            time.sleep(1)
        note = '0'
        ser.write(note.encode())
    elif command.strip() == song3_list[0]:
        for note in song3_list[1:]:
            ser.write(note.encode())
            time.sleep(1)
        note = '0'
        ser.write(note.encode())
    else:
        print("wrong song name!")
        continue
input("press <enter> to quit")
