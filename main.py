import sys


from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import*
from uart import*
from config import config
from bien import*
from GUI import*
AIO_FEED_IDs = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "holong"
AIO_KEY = "aio_Ahvt472c11ui846b1nKbVJ62ZF3S"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
       client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)


def read_serial_ack(client,toppic_ack,ack):
    if readSerialWithAck(ack, 1)==True:

        client.publish(toppic_ack, ack)
        print("Result :"+toppic_ack +"-" +ack)
        # if toppic_ack=="ack2"& ack=="20":
        #     config.setAge(config,1)
        # else: config.setAge(config,0)
# Hàm này sẽ chạy trên một thread mới
def read_serial_2():  #not used
    if readSerialWithAck("21", 1):

        client.publish("ack2", 11)
    print("Result 2:")

# Tạo hai thread mới để chạy hàm read_serial_1 và read_serial_2


lock = threading.Lock()
# Chờ hai thread kết thúc


# def message(client, feed_id, payload):
#     global var1
#     print("Nhan du lieu: " + payload+ "  feed id:" +feed_id)
#     if var1==0:
#         if feed_id == "nutnhan1":
#             if payload =="0":
#                 writeData("1")
#                 print("waitting1")
#                 if readSerialWithAck("11",4):
#                      var1 = 1
#                      client.publish("ack", 11)
#
#                      # writeData("2")
#
#                     #         neeus ack=0 laf ko nhan dc ack tra ve
#
#             else:
#                 writeData("2")
#                 print("waitting1")
#                 if readSerialWithAck("10",4):
#                      var1 = 1
#                      client.publish("ack", 10)
#                      # writeData("1")
#         if feed_id == "nutnhan2":
#             if payload == "0":
#                  writeData("3")
#                  print("waitting2")
#                  if readSerialWithAck("21",0.1) :
#                      var1 = 1
#                      client.publish("ack2", 21)
#
#                      # writeData("4")
#             else:
#                 writeData("4")
#                 print("waitting2")
#                 if readSerialWithAck("20",0.1):
#                      var1 = 1
#                      client.publish("ack2", 20)
#
#                      # writeData("3")
#     else:
#         var1 = 0
ktra =0

def message(client, feed_id, payload):
    a=config.getName(config)
    print(a)
    if a==0:

        print("Nhan du lieu: " + payload+ "  feed id:" +feed_id)

        if feed_id == "nutnhan1":
            if payload =="0": #off led
                    writeData("1")
                    print("waitting1")
                    with lock:
                        thread1 = threading.Thread(target=read_serial_ack, args=(client,"ack", "10"))
                        thread1.start()
                        thread1.join()


            else:
                    writeData("2")
                    print("waitting1")
                    with lock:
                        thread2 = threading.Thread(target=read_serial_ack, args=(client,"ack", "11"))
                        thread2.start()
                        thread2.join()

        if feed_id == "nutnhan2":
                if payload == "0":
                     writeData("3")
                     config.setAge(config, 1)
                     print("waitting2")
                     with lock:
                         thread3 = threading.Thread(target=read_serial_ack, args=(client,"ack2", "20"))
                         thread3.start()
                         thread3.join()

                         # writeData("4")
                else:
                    writeData("4")
                    config.setAge(config, 0)
                    print("waitting2")
                    with lock:
                        thread4 = threading.Thread(target=read_serial_ack, args=(client,"ack2", "21"))
                        thread4.start()
                        thread4.join()
                         # writeData("3")
    else: config.setName(config,0)
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 3


sensor_type = 0
counter_ai = 50
ai_result = ""
while True:
    # counter = counter - 1
    counter_ai = counter_ai - 1
    # if  counter <= 0:
    #     counter = 3
    #     # todo
    #     print("random data")
    #     if sensor_type == 0:
    #        temp = random.randint(10,20)
    #        client.publish("cambien1",temp)
    #        sensor_type =1
    #     elif sensor_type == 1:
    #       humi = random.randint(50,70)
    #       client.publish("cambien3",humi)
    #       sensor_type = 2
    #     elif sensor_type == 2:
    #      light = random.randint(100,500)
    #      client.publish("cambien2",light)
    #      sensor_type = 0
    # time.sleep(1)
    readSerial(client)
    if counter_ai <= 0:
        counter_ai = 5
        old_ai_result = ai_result
        ai_result,data= image_detector()
        print("AI Ouput:   ", ai_result)
        client.publish("image", data)
        if old_ai_result != ai_result:
            client.publish("ai", ai_result)
        if config.getAge(config) == 0:
            if ai_result=="có rác":
                writeData("7")
                print("dax gui")
    time.sleep(1)

pass