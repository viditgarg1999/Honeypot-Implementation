
import hashlib 

def hash256(text,salt):
    text = text.encode()
    salt = salt.encode()
    return hashlib.sha256(text+salt).hexdigest()

secret_key = "s3cr3t"

def password(plaintext,salt):
    salt1 = hash256(secret_key,salt)
    hsh = hash256(plaintext,salt1)
    return "".join((salt1,hsh))

def generatepassword(plaintext,salt,alp,length=10):
    alphabet = ('abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789')
    if(alp == 1):
        alphabet = alphabet + '!@#$%^&*()-_'

    hexdig = password(plaintext,salt)
    num = int(hexdig,16)

    num_chars = len(alphabet)

    chars = []
    while len(chars) < length:
        num, idx = divmod(num, num_chars)
        chars.append(alphabet[idx])

    return ''.join(chars)

a=input("Enter username");
b=input("Enter website name");
c=int(input("Enter 1 if you want special character or else enter 0"));
d=generatepassword(a,b,c);

import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a') as fp:
        #json.dump("data=",fp)
        json.dump(data, fp)


# Example

path = './'
fileName='data'
data = {}
data['username1'] = a
data['password1']=d
 
writeToJSONFile(path,fileName,data)





