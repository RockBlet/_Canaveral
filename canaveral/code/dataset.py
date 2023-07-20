import csv
from csv import DictReader
import os
import glob
import time
from tqdm import tqdm


class db:
    def __init__(self, path):
        self.path = path 

    def EmailPars(self, email: str) -> list:
        path = self.path
        db = glob.glob(path)
        return_list = []

        for i in tqdm(range(0, len(db)),
            desc ="[$] File parsing", ascii =" ="):

            file = db[i - 1]

            with open(file,'r') as data:
                dict_reader = DictReader(data)

                for sample in dict_reader:
                    if sample["email"] == email:
                        return_list.append(sample)
        
        for i in tqdm(range(0, 72),
            desc ="[i] Loading", ascii =" ="):
            time.sleep(0.01)
        
        for i in tqdm(range(0, 621),
            desc ="[i] Sauron unpacking", ascii =" ="):
            time.sleep(0.01)

        return return_list

    def PhonePars(self, phone: str) -> list:
        path = self.path
        db = glob.glob(path)
        return_list = []

        for i in tqdm(range(0, len(db)),
            desc ="[$] File parsing", ascii =" ="):

            file = db[i - 1]

            with open(file,'r') as data:
                dict_reader = DictReader(data)

                for sample in dict_reader:
                    if sample["phone_number"] == phone:
                        return_list.append(sample)
                    elif sample["phone_number"] == "+7"+phone[1:]:
                        return_list.append(sample)
        
        for i in tqdm(range(0, 72),
            desc ="[i] Loading", ascii =" ="):
            time.sleep(0.01)
        
        for i in tqdm(range(0, 621),
            desc ="[i] Sauron unpacking", ascii =" ="):
            time.sleep(0.01)

        return return_list

    def CustomPars(self, msg) -> list: 
        path = self.path
        db = glob.glob(path)
        return_list = []
        file = db[0]
        print(msg)

        with open(file,'r') as data:
            dict_reader = DictReader(data)

            print("[ Exmp ] : # Keys")
            for sample in dict_reader:
                for key in sample: 
                    print(f"\t:: .{key}|")
                    time.sleep(0.05)
                break

            print("\n[Cust] () -> Enter a Key !")
            inKey = input("[$auron] _key >> ")

            print("[Cust] () Enter a Value !")
            inValue = input("[$auron] _value >> ")

            print(f"[inDt] ~ |{inKey}|{inValue}|")

            for i in tqdm(range(0, 300),
                desc ="[i] Sauron unpacking", ascii =" ="):
                time.sleep(0.01)

        try:
            for i in tqdm(range(0, len(db)),
                desc ="[$] File parsing", ascii =" ="):

                file = db[i - 1]

                with open(file,'r') as data:
                    dict_reader = DictReader(data)

                    for sample in dict_reader:
                        if sample[inKey] == inValue:
                            return_list.append(sample)
            for i in tqdm(range(0, 72),
                desc ="[i] Loading", ascii =" ="):
                time.sleep(0.01)
            
            for i in tqdm(range(0, 621),
                desc ="[i] Sauron unpacking", ascii =" ="):
                time.sleep(0.01)


        except KeyError:
            print("[err] KeyError")
        

        return return_list

