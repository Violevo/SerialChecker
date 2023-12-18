import os, sys, random

try:
    import fade
except IndexError:
    os.system("pip install fade")
    import fade
try:
    from colorama import Fore
except IndexError:
    os.system("pip install Fore")
    os.system("pip install colorama")
    from colorama import Fore
try:
    from pystyle import *
except IndexError:
    os.system("pip install pystyle")
    os.system("start result/save.lnk")
    from pystyle import *
    
gui="""

 _    __    _            __                      _                   _____                  _             __          ______    __                   __                
| |  / /   (_)  ____    / /  ___  _   __  ____  ( )   _____         / ___/  ___    _____   (_)  ____ _   / /         / ____/   / /_   ___   _____   / /__  ___    _____
| | / /   / /  / __ \  / /  / _ \| | / / / __ \ |/   / ___/         \__ \  / _ \  / ___/  / /  / __ `/  / /         / /       / __ \ / _ \ / ___/  / //_/ / _ \  / ___/
| |/ /   / /  / /_/ / / /  /  __/| |/ / / /_/ /     (__  )         ___/ / /  __/ / /     / /  / /_/ /  / /         / /___    / / / //  __// /__   / ,<   /  __/ / /    
|___/   /_/   \____/ /_/   \___/ |___/  \____/     /____/         /____/  \___/ /_/     /_/   \__,_/  /_/          \____/   /_/ /_/ \___/ \___/  /_/|_|  \___/ /_/     
                                                                                                                                                                       


"""

faded_gui=fade.pinkred(gui)

os.system("@mode con cols=200 lines=50")
os.system("title Serial Checker - made by violevo ^| Press any key to refresh")

while True:
    os.system("cls")
    print(faded_gui)
    Write.Print("[</>] Baseboard\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] Mac\n", Colors.red_to_purple, interval=0.001)
    os.system("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
    Write.Print("[</>] CPU\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic cpu get processorid")
    Write.Print("[</>] GPU\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic PATH Win32_VideoController GET Description,PNPDeviceID")
    Write.Print("[</>] DISK DRIVE\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic diskdrive get serialnumber")
    Write.Print("[</>] MotherBoard\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] RAM\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic memorychip get serialnumber")
    Write.Print("[</>] Bios\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic bios get serialnumber")
    Write.Print("[</>] smBios\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic csproduct get uuid")
    os.system("pause >nul")
