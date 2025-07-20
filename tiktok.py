import time, os, random

#------------------- COLORS -------------------#
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
C = '\033[1;36m'
P = '\033[95m'
W = '\033[1;37m'
B = '\033[1;34m'

#------------------- LOGO -------------------#
def logo():
    os.system('clear')
    print(f"""{P}
╔══════════════════════════════════════════╗
║      {G}TIKTOK FOLLOWERS GENERATOR - 2025     {P}║
╠══════════════════════════════════════════╣
║        {Y}HACKING WORLD - VIP EDITION         {P}║
╚══════════════════════════════════════════╝
""")

#------------------- ANIMATION -------------------#
def loading(text, sec):
    for i in range(sec):
        dots = "." * (i % 4)
        print(f"{C}{text}{dots}", end='\r')
        time.sleep(1)

#------------------- FAKE FOLLOW SYSTEM -------------------#
def follow_gen():
    logo()
    username = input(f"{Y}Enter TikTok Username: {W}@")
    time.sleep(1)
    print(f"{C}[✓] Connecting to TikTok server...")
    loading("Syncing Followers Database", 4)
    
    print(f"{G}[✓] Username Found: {username}")
    time.sleep(1)
    print(f"{Y}[✓] Account Status: Public")
    time.sleep(1.5)
    
    followers = random.randint(5000, 20000)
    print(f"{P}[+] Generating {followers} Followers...")
    loading("Injecting Followers", 6)
    
    print(f"{G}\n[✓] Success! {followers} Followers Sent To @{username}")
    print(f"{B}[!] Note: May take 24 hours to reflect!")
    
    input(f"\n{W}Press Enter To Return to Menu...")

#------------------- MAIN MENU -------------------#
def menu():
    while True:
        logo()
        print(f"{W}[1] Start Followers Generator")
        print(f"{W}[2] Exit Tool")
        print(f"{W}--------------------------------------")
        choice = input(f"{Y}[?] Choose Option: ")
        if choice == '1':
            follow_gen()
        elif choice == '2':
            exit()
        else:
            print(f"{R}[!] Invalid Option!")
            time.sleep(1)

#------------------- START -------------------#
menu()