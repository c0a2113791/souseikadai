import network
import socket
import time
from machine import Pin

p2 = Pin(2, Pin.OUT)
#クライアントのIPアドレスとポートの指定
server_ip = "192.168.4.2"
server_port = 12345

#UDPソケットを作成
#AF_INETでIPv4を指定,SOCK_DGRAMでUDP通信を指定
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ソケットにIP,portを紐づけ
sock.bind((server_ip,server_port))
sock.settimeout(2)
packet_loss = 0
total_packet = 1
rssi_num = 0
success_packet = 0

while not sta_if.isconnected():
    print("connecting...")
    utime.sleep_ms(1000)
    pass
print(sta_if.ifconfig())
print("AP connect")
p2.on()


time.sleep(20)
f = open("rssidata_2.txt","w")
while total_packet<=100:
    try:
        rssi = sta_if.status("rssi")
        data= sock.recvfrom(1024)
        print(f"packet{total_packet}",rssi)        
        f.write(f"{total_packet} {rssi}\n")
        total_packet += 1
        success_packet +=1
        rssi_num += rssi
        
    except Exception as e:
        print(f"Packet loss{total_packet}",e)
        f.write(f"{total_packet} packet loss\n")
        total_packet += 1
        packet_loss += 1

rssi_average = int(rssi_num/success_packet)
packet_loss_percentage = int((packet_loss / total_packet-1) * 100)
print(f"Packet loss rate: {packet_loss}/{total_packet-1} ({packet_loss_percentage}%)")
print(f"ave:{rssi_average}")

f.write(f"loss:{100+packet_loss_percentage}  ave:{rssi_average}")
f.close()
sock.close()



