import requests
import hashlib
import json

filename = input("What is the file path ?\n")
flag =0
with open(filename, "rb") as f:
    file_contents = f.read()
md5_hash = hashlib.md5()
md5_hash.update(file_contents)
hash_digest = md5_hash.hexdigest()

print("MD5 hash of file", filename, "is:", hash_digest)

url = "https://www.virustotal.com/api/v3/search?query="+hash_digest

headers = {
    "accept": "application/json",
    "x-apikey": "bb5908629d18dd2a3ead98b0af3da453f00261af9949c82b218215ffbfc76af6"
}

response = requests.get(url, headers=headers)
data = response.json()
##print("for more details "+response.text)

try  :
    if(data['data'][0]['attributes']['type_description']!="unknown"):
        flag=1
except Exception as e:
    if(len(data['data'])):
        flag=1

if(flag==1):
    print("YOU GOT "+data['data'][0]['attributes']['names'][0]+" VIRUS"+"\nthis file is potentially harmful or malicious and should not be opened or executed")
else:
    print("nothing has being detected")
    
print("Press any key to exit...")
input()


