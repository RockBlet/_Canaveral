from loggs import LogFormat
import logging 
import time
import pyfiglet
import os
from tqdm import tqdm
from colorama import init
from colorama import Fore, Back, Style
from dataset import db 
import glob
import random


def loggersSet():
	status = "0![_None_]"

	logger.debug(status)
	time.sleep(0.05)
	logger.info(status)
	time.sleep(0.1)
	logger.warning(status)
	time.sleep(0.05)
	logger.error(status)
	time.sleep(0.25)
	logger.critical(status) 
	time.sleep(0.1)

	for i in tqdm(range(0, 25), ncols = 100, 
			  desc ="Loading db", ascii =" ="):
		time.sleep(.1)
	
	for i in tqdm(range(0, 29),
              desc ="Objects Loading", ascii =" ="):
		time.sleep(.1)

	for i in tqdm(range(0, 17), ncols = 100,
               desc ="db Connecting", ascii =" ="):
		time.sleep(.1)

	for i in tqdm(range(0, 25),
              ascii =" =", desc = "Loading"):
		time.sleep(.1)


def logo():
    init()
    
    logo = pyfiglet.figlet_format("S a u r o n", font = "bulbhead" )
    logo = Fore.CYAN + logo + Style.RESET_ALL

    byName = Fore.CYAN + "[c] - By Nemizuki" + Style.RESET_ALL

    os.system("clear")

    for i in logo:
        print(i, end ='')
        time.sleep(0.002)

    print(byName)


def info(data):
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)

	logger.info(data)


def debug(data):
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	logger.debug(data)


def error(data):
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)
	
	logger.ERROR(data)


def showFiles():
    path = '../csv/*'
    db = glob.glob(path)
    count = 0

    for file in db:
        s = f"{file} - readble $ok"
        info(s)
        time.sleep(0.05)
        count += 1

        if random.randint(1, 5) == 1:
        	debug(f"{count} / 66 : files load")

    print(f"[$] Sauron : Status : Files count -> {count}")
    debug(f"files in db{count}")


def cutePrint(l):
    wall = arrow = Fore.CYAN + "|" + Style.RESET_ALL

    for obj in l:
        print("{")
        for key in obj:
            print(f"\t{key} : {obj[key]}{wall}")
            time.sleep(0.1)
        print("}")
        time.sleep(0.6)


def inp(*arg) -> str:
	if arg:
		arg = arg[0]
	else:
		arg = ''

	arrow = Fore.CYAN + ">>" + Style.RESET_ALL

	ans = str(input(f"{arg} {arrow} ")).replace(" ", "")
	return ans


def output(data):
	print(f"\n[$] <> {data}:")


def ShowAns(search_answer):
	stat = Fore.GREEN + "[+] Seaching : -> Succsess" + Style.RESET_ALL
	dlr = Fore.YELLOW + "$" + Style.RESET_ALL
	enter = Fore.BLUE + "Enter" + Style.RESET_ALL
	fail = Fore.RED + "Failed" + Style.RESET_ALL

	if search_answer:
		time.sleep(1)

		info(stat)
		output(f"{dlr} Press {enter} to show info")
		input()
		cutePrint(search_answer)
		info(f"Obj's count : {len(search_answer)}")

		output(f"{dlr} Press {enter} to countinue")
		input()

	else:
		info(f"Seaching ->= {fail} : Not found")
		output(f"{dlr} Press {enter} to countinue")
		input()


def menu():
	logo()
	output("Search type")
	print("\t0 - custom")
	print("\t1 - phone")
	print("\t2 - email")
	Stype = inp()

	path = '../csv/*'
	DataBase = db(path) 

	if Stype == "0":
		msg1 = Fore.RED +'\033[1m'
		msg2 = "This is a custom mode! \n\t[!Danger]"
		msg3 = '\033[0m' + Style.RESET_ALL
		msg = msg1 + msg2 + msg3

		search_answer = DataBase.CustomPars(msg)
		ShowAns(search_answer)

	elif Stype == "1":
		output("Enter a phone number, start from '8'")
		phone = inp("Number")
		phoneSTR = f"{phone} .&. +7{phone[1:]}"
		phoneSTR = Fore.YELLOW + phoneSTR + Style.RESET_ALL
		info(f"searching : {phoneSTR}")
		
		search_answer = DataBase.PhonePars(phone)
		ShowAns(search_answer)

	elif Stype == "2":
		output("Enter email")
		mail = inp("Email")
		info(f"searching : {mail}")

		search_answer = DataBase.EmailPars(mail)
		ShowAns(search_answer)


def load():
	status = "[$] Ready to load db : Sauron Status -> Succsess |"

	#loggerr.info(status)
	time.sleep(0.5)

	dbs = db('../csv/*')

	while True:
		cond = random.randint(1,7)

		if cond == 1 or cond == 2:
			showFiles()

		elif cond == 3 or cond == 4:
			os.system("brew config")
			time.sleep(0.3)
			os.system("arp -a")
			time.sleep(0.25)

		elif cond == 5 or cond == 6: 
			loggersSet()

		elif cond == 7: 
			answer = dbs.PhonePars("89654276611")
			cutePrint(answer)
			time.sleep(random.randint(4, 6))


if __name__ == "__main__":
	os.system("clear")
	
	# logger settings
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)


	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	ch.setFormatter(LogFormat())

	logger.addHandler(ch)

	# Set loggers 
	showFiles()
	loggersSet()

	#load()
	
	while True:
		menu()
		time.sleep(0.005)

