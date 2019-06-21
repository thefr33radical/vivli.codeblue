from  config import path1,path2,path3

from cryptography.fernet import Fernet
import pandas as pd

key = Fernet.generate_key()
f = Fernet(key)

def encrypt():

    data=pd.read_csv(path1)
    #key = Fernet.generate_key()

    data.fillna(0,inplace=True)
    print("Data Encrypted")
    for col in range(len(data.columns)):
        for rows in range(200):
            data.iloc[rows,col]=f.encrypt(str(data.iloc[rows,col]).encode())
            print(data.iloc[rows,col])
    data.to_csv(path3)


def decrypt():
    data=pd.read_csv(path2)

    #f = Fernet(key)
    #data.fillna(0,inplace=True)
    print("Data Decrypted")
    for col in range(len(data.columns)):
        for rows in range(len(data)):
            #data.iloc[rows,col]=f.decrypt(str(data.iloc[rows,col]).encode())
            print(data.iloc[rows,col])
encrypt()
decrypt()
