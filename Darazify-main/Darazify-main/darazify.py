from modules.scrape import Daraz
from modules import options
from modules import colors
from modules import clrscr
from modules import banner
from selenium import webdriver

clrscr.clear_screen()
banner.Banner()
link = options.get_link()
percent = int(input(f"{colors.bcolors.LOGGING}Enter Minimum Discount Percentage [1-100] : {colors.bcolors.ENDC}"))
bswr = input(f"{colors.bcolors.OKGREEN}Do you want to search in browser{colors.bcolors.ENDC} {colors.bcolors.NOTICE}(It can take more time){colors.bcolors.ENDC} [Y/n] : ")

if bswr.lower() == "y":
    browser = webdriver.Firefox()
elif bswr.lower() == "n":
    browser = None
else:
    print(f'{colors.bcolors.RED}Invalid input. Try again.{colors.bcolors.ENDC}')
    exit()

clrscr.clear_screen()
open('output.txt', 'w').close()
i = 1

while True:
    url = link + str(i)
    print("<=================================================================================>".center(167))
    print(f'{colors.bcolors.RED}{[i]}{colors.bcolors.ENDC} Trying on --> {colors.bcolors.HEADER}{url}{colors.bcolors.ENDC}'.center(185))
    print("<=================================================================================>".center(167))
    print('\n')
    daraz_instance = Daraz(url, percent, browser)
    i += 1