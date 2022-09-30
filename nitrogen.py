import random, string, os, time
from colorama import Fore, Style
from pystyle import Colorate, Colors
file = open("oxygen_nitros.txt", "w")
os.system("title Oxygen Nitro Generator | Made by NoKiX")
def clear():
    os.system("cls")
clear()

print(Colorate.Horizontal(Colors.cyan_to_blue, """
  /$$$$$$                                                   
 /$$__  $$                                                  
| $$  \ $$ /$$   /$$ /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$  | $$|  $$ /$$/| $$  | $$ /$$__  $$ /$$__  $$| $$__  $$
| $$  | $$ \  $$$$/ | $$  | $$| $$  \ $$| $$$$$$$$| $$  \ $$
| $$  | $$  >$$  $$ | $$  | $$| $$  | $$| $$_____/| $$  | $$
|  $$$$$$/ /$$/\  $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$
 \______/ |__/  \__/ \____  $$ \____  $$ \_______/|__/  |__/
                     /$$  | $$ /$$  \ $$                    
                    |  $$$$$$/|  $$$$$$/                    
                     \______/  \______/                     """, 1))

codes = 0
def nitro(size=16, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
print(f"\n{Fore.CYAN}[Oxygen Generator] {Fore.WHITE}https://discord.gift/{Style.RESET_ALL}"+nitro())
while(True):
        print(f"{Fore.CYAN}[Oxygen Generator] {Fore.WHITE}https://discord.gift/{Style.RESET_ALL}"+nitro())
        file.write("[Oxygen Generator] https://discord.gift/"+nitro()+"\n")
time.sleep(1)
