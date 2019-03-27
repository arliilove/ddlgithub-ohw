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
    else :
	    print ("No Arduino Device was found connected to the computer")
#***************************************************************************
time.sleep(2)
while True:
    command = input("Please enter the command: ")
    if command.strip() == "q":
        ser.close()
        break;
    else:
        ser.write(command.encode())
        time.sleep(1)
input("press <enter> to quit")
