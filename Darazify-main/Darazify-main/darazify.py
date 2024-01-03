from modules import colors
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from modules import options
from modules import clrscr
from modules import banner
from modules.scrape import Daraz

clrscr.clear_screen()
banner.Banner()

link = options.get_link()
percent = int(input(f"{colors.bcolors.LOGGING}Enter Minimum Discount Percentage [1-100] : {colors.bcolors.ENDC}"))
bswr = input(
    f"{colors.bcolors.OKGREEN}Do you want to search in browser{colors.bcolors.ENDC} {colors.bcolors.NOTICE}(It can take more time){colors.bcolors.ENDC} [Y/n] : ")

# Provide a default value for browser
browser = None

if bswr.lower() == "y":
    options = Options()
    options.headless = False  # Set it to True if you don't want to see the browser
    browser = webdriver.Firefox(options=options)
    browser.minimize_window()
elif bswr.lower() != "n":
    print(f'{colors.bcolors.RED}Invalid input. Try again.{colors.bcolors.ENDC}')
    exit()

clrscr.clear_screen()
open('output.txt', 'w').close()
i = 1

while True:
    url = link + str(i)
    print("<=================================================================================>".center(167))
    print(
        f'{colors.bcolors.RED}{[i]}{colors.bcolors.ENDC} Trying on --> {colors.bcolors.HEADER}{url}{colors.bcolors.ENDC}'.center(
            185))
    print("<=================================================================================>".center(167))
    print('\n')

    # Pass the browser instance to the Daraz class
    daraz_instance = Daraz(url, percent, browser)
    i += 

