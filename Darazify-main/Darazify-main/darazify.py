from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from colorama import init, Fore, Style  # Import colorama
from modules import clrscr
from modules import banner
from modules import options
from modules.scrape import DarazScraper

# Initialize colorama
init()

clrscr.clear_screen()
banner.Banner()

link = options.get_link()
percent = int(input(f"{Fore.GREEN}Enter Minimum Discount Percentage [1-100]: {Style.RESET_ALL}"))
bswr = input(
    f"{Fore.YELLOW}Do you want to search in browser (It can take more time) [Y/n]: {Style.RESET_ALL}")

browser = None

if bswr.lower() == "y":
    options = Options()
    options.headless = False

    # Use webdriver_manager to automatically download geckodriver
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    browser.minimize_window()
elif bswr.lower() != "n":
    print(f'{Fore.RED}Invalid input. Try again.{Style.RESET_ALL}')
    exit()

# Rest of the code remains unchanged...


clrscr.clear_screen()
open('output.txt', 'w').close()
i = 1

last_page_css_selector = ".title--sUZjQ"  # Update this with the actual CSS selector for the last page

while True:
    url = link + str(i)
    print("<=================================================================================>".center(167))
    print(
        f'{Fore.RED}[{i}]{Style.RESET_ALL} Trying on --> {Fore.BLUE}{url}{Style.RESET_ALL}'.center(185))
    print("<=================================================================================>".center(167))
    print('\n')

    daraz_scraper = DarazScraper(browser)
    if not daraz_scraper.scrape_product_data(url, percent, last_page_css_selector):
        break  # Stop the loop if the last page is reached

    i += 1

# Close the browser after the loop
if browser is not None:
    browser.quit()
