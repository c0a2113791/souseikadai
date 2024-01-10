import network
import socket
import time
from machine import Pin, SoftI2C

#アクセスポイントに接続
#wlan:APを基盤に通信する際に使われる単語

#サーバのIPアドレストポートを設定
server_ip = "192.168.4.2"
server_port = 12345


#UDPソケットを作成
sock2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock2.bind(("",server_port))

count = 0
rssi_data = 0
num_packets = 100
num =0
while True:
    msg = "test"
    sock2.sendto(msg,(server_ip,server_port))
    time.sleep_ms(200)
    num += 1
    print(f"sent: test")
