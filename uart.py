import serial.tools.list_ports
import time
import threading
from config import*
from GUI import*



def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        print(strPort)
        if "CP210x" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
    # return "COM4"
if getPort() != "None" :
        ser = serial.Serial( port=getPort(), baudrate=9600)
        print(ser)
mess = ""


def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")

    print(splitData)
    if splitData[1] == "couter":
        client.publish("cambien1", splitData[2])
        # temp_label.config(text="Nhiệt độ hiện tại: {}°C".format(splitData[2]))
    elif splitData[1] == "LIGHT":
        client.publish("cambien2", splitData[2])
        # Light_label.config(text="Nhiệt độ hiện tại: {}°C".format(splitData[2]))
    elif splitData[1] == "button2":
        config.setName(config,1)

        if splitData[2]=="0":
            writeData("5")
            client.publish("nutnhan2", "0")
        elif   splitData[2]=="1":
                writeData("6")
                client.publish("nutnhan2", "1")
mess = ""
def readSerial(client):
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        print(mess)
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client,mess[start:end + 1])
            if (end == len(mess)):
                mess = ""

            else:
                mess = mess[end+1:]
def writeData(data):
    ser.write(str(data).encode())

lock = threading.Lock()
def readSerialWithAck(ack, timer):
    start_time = time.time()
    ack_received =""
    # with lock:
    while time.time() - start_time < timer:
            bytesToRead = ser.inWaiting()
            if bytesToRead > 0:
                ack_received = ack_received + ser.read(bytesToRead).decode("UTF-8")
                if ack_received == ack:
                    print("Ack received: " + ack_received)
                    return True
                else:
                    print("Invalid ack received: " + ack_received)
                    return False
    print("Timed out waiting for ack.")
    return False

# def readSerialWithAck():
#     start_time = time.time()
#     while time.time() - start_time < 2:
#         bytesToRead = ser.inWaiting()
#         if bytesToRead > 0:
#             ack = ser.read(1).decode('UTF-8')
#             if ack == 0:
#                 return 0
#             elif ack == '1':
#                 print(ack)
#                 return 1
#             print(ack)
#     return 0