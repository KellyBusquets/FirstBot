from tkinter import MOVETO


try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time
   from datetime import datetime 
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """      

         /¯¯¯/¯¯|°/¯¯¯¯/¯¯¯¯¯¯¯/ /¯¯¯/¯\              /¯¯¯/¯¯\  '                /¯¯¯/¯¯¯¯¯\        /¯¯¯/¯¯¯\        /¯¯¯/¯\    
/¯¯¯/¯¯\¯¯|    | \¯¯¯ \   \/      /   \¯¯¯\   \           |¯¯¯|  |\_/                  \¯¯¯\      \)  |__'  |¯¯¯|    |\  '\  '  /     /    /    
\¯¯¯\     \  |    |   \      \      \¯ '     \     \   \¯¯/¯¯\ \¯¯¯\  ¯¯¯¯¯\               \     \             \ \¯¯¯\    \ \  '\/___/      \   
  \     \     \|    |°    \      \    / '        \     \   \/     /   ¯¯¯)¯¯¯)    /'                \     \      \)   /   \     \    \|   |\___\_/\    \  
    \___\'____/        \___'\/    '          \___\___'/         |___'|__/°                   \___\____/      \___\___/      '\___\__| 

 """
                

class bot1:

    def __init__(self):
        self.delay = 0.5
        

    def get_positions(self):
        self.print_console("Press P to set your first position for the bot.")
        while True:
            if keyboard.is_pressed("P"):
                self.firstbot_input = pyautogui.position()
                break
        time.sleep(0.5)
    
    def bot_1(self):
       pyautogui.moveTo(self.firstbot_input)
       pyautogui.click()
       time.sleep(self.delay)

    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score Botter | Developed by @useragents on Github")
        print(Fore.RED + ascii_text)
        self.get_positions()
        shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut: "))
        self.print_console("Slow PC", "1")
        self.print_console("Fast PC", "2")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Option: "))
        if options == 1:
            self.delay = 2
        self.print_console("Press P when ready.")   

        while True:
            if keyboard.is_pressed("P"):
                break
        os.system("cls")
        print(Fore.RED + ascii_text)
        self.print_console("Bot is getting to work")
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("F4"):
                break
        self.print_console(f"Bot ended.")

obj = bot1()  
obj.main()
