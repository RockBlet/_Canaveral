from loggs import LogFormat
import logging
import colorama
import os
import time
import pyfiglet


class Canaveral:
    def __init__(self):
        self.command_list = ["osint db", "nmap"]

    def inp(self) -> str:
        symb = colorama.Fore.CYAN + ">" + colorama.Style.RESET_ALL + "> "
        req = str(input(symb))

        return req

    def list_choser(self, command_list: list) -> int:
        colorama.init()
        mode = colorama.Fore.CYAN+ "[mode]" + colorama.Style.RESET_ALL
        arr = colorama.Fore.CYAN+ ">" + colorama.Style.RESET_ALL

        print("\n")

        for key, value in enumerate(command_list):
            print(f"{mode}{key} -{arr} {value}")

        return int(self.enter())


    def logo(self) -> int:
        colorama.init()
        collor = colorama.Fore.CYAN

        logo = pyfiglet.figlet_format("Canaveral", font="bulbhead")
        logo = collor + logo + colorama.Style.RESET_ALL
        byName = collor + "[c] - By Nemizuki" + colorama.Style.RESET_ALL
        cnv = collor + "Canaveral" + colorama.Style.RESET_ALL


        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        ch.setFormatter(LogFormat())

        os.system("clear")
        logger.addHandler(ch)


        os.system("clear")
        for i in logo:
            print(i, end='')
            time.sleep(0.001)

        time.sleep(0.25)
        

        print(byName,"\n\n")
        print("[!] for |> Sudo")














