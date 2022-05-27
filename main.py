
import threading
import time
import colorama
import requests

from colorama import Fore, Style, init

colorama.init(autoreset=True, convert=True)

class Username:

    def __init__(self):

        # Loading Colours
        self.w = Style.BRIGHT + Fore.WHITE
        self.r = Style.BRIGHT + Fore.RED
        self.g = Style.BRIGHT + Fore.GREEN
        self.b = Style.BRIGHT + Fore.BLUE

        # Loading Usernames
        self.Names = []

        for name in open("Users/all.txt", "r"):
            if name != "":
                self.Names.append(
                    name.replace("\n", "").replace("\r\n", "").replace("\r", ""))

        self.url = "https://github.com/"

    # Main Function
    def main(self, name, delay):

        headers = {"Host": "github.com",
                     "Connection": "keep-alive", 
                     "Cache-Control": "max-age=0", 
                     "Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", 
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
                     "Referer": "{}".format("https://github.com/"), 
                     "Accept-Encoding": "gzip, deflate, br", 
                     "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"}

        try:

            req = requests.get(f"{self.url}{name}", headers=headers)

            if req.status_code == 200:
                print(f"{self.w}[{self.r}!{self.w}] {self.r}{name} is Invalid!")
                file = open("results/invalid.txt", "a")
                file.write("{}\n".format(name))
                file.close()

            elif req.status_code == 404:
                print(f"{self.w}[{self.g}#{self.w}] {self.g}{name} is valid or banned!")
                file = open("results/validOrBanned.txt", "a")
                file.write("{}\n".format(name))
                file.close()

            elif req.status_code == 429:
                print(f"{self.w}[{self.r}!{self.w}] {self.r}Rate limited, Waiting for 2 seconds....")
                time.sleep(2)

            else:
                print(f"{self.w}[{self.r}@{self.w}] {self.b}{name} Had an error!")
                file = open("results/error.txt", "a")
                file.write("{}\n".format(name))
                file.close()


            time.sleep(delay)

        except Exception as e:
            print(f"Error: {e}")
        
    # Theading Function
    def choice(self):

        print(f'[>] Github UserFinder')
        print(f'[>] Made by prefez')
        print("-="*20)
        while True:
            try:
                print(f"{self.w}[{self.g}-{self.w}] Enter How Many Threads >> ", end="")
                threads = input()
                threads = int(threads)
                break

            except Exception:
                print(f"{self.w}[{self.r}!{self.w}] {self.r}Invalid Choice")

        while True:
            try:
                print(f"{self.w}[{self.g}-{self.w}] Enter Delay, {self.g}0 {self.w}= {self.g}No Delay {self.w}>> ", end="")
                d = input()
                d = float(d)
                break

            except Exception:
                print(f"{self.w}[{self.r}!{self.w}] {self.r}Invalid Choice")

        for i in range(int(threads)):
            for name in self.Names:
                s = threading.Thread(target=self.main(name, d))
                s.start()

        print("-="*20)
        print("finished!")

if __name__ == "__main__":
    client = Username()
    client.choice()
    
