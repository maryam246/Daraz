from modules import urls
from modules import colors
from modules import clrscr
 
def get_link():
    print(f'''
    {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}
    [+] Groceries & Pets                 [1]
    [+] Health & Beauty                  [2]
    [+] Women's Fashion                  [3]
    [+] Men's Fashion                    [4]
    [+] Babies & Toys                    [5]
    [+] Home & Lifestyle                 [6]
    [+] Electronic Devices               [7] 
    [+] Electronic Accessories           [8]
    [+] Tv & Home Appliances             [9]
    [+] Sports & Outdoor                 [10]
    [+] Watches, Bags & Jewellery        [11]
    [+] Automotive & Motorbike           [12]
    {colors.bcolors.ENDC}''')

    user_input = input("--> ")
    


    # Groceries_and_Pets
    if user_input == '1':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Beverages                       [1]
        [+] Fresh Products                  [2]
        [+] Breakfast, Choco & Snacks       [3]
        [+] Food Staples                    [4]
        [+] Dairy & Chilled                 [5]
        [+] Laundry & Household             [6]
        [+] Cat                             [7]
        [+] Dog                             [8]
        [+] Fish                            [9]
        [+] Frozen Food                     [10]
    {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Groceries_and_Pets['Beverages']
        elif user_input_var == '2':
            return urls.Groceries_and_Pets['Fresh Products']
        elif user_input_var == '3':
            return urls.Groceries_and_Pets['Breakfast, Choco & Snacks']
        elif user_input_var == '4':
            return urls.Groceries_and_Pets['Food Staples']
        elif user_input_var == '5':
            return urls.Groceries_and_Pets['Dairy & Chilled']
        elif user_input_var == '6':
            return urls.Groceries_and_Pets['Laundry & Household']
        elif user_input_var == '7':
            return urls.Groceries_and_Pets['Cat']
        elif user_input_var == '8':
            return urls.Groceries_and_Pets['Dog']
        elif user_input_var == '9':
            return urls.Groceries_and_Pets['Fish']
        elif user_input_var == '10':
            return urls.Groceries_and_Pets['Frozen Food']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Health_and_Beauty
    elif user_input == '2':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Bath & Body                     [1]
        [+] Beauty Tools                    [2]
        [+] Fragrances                      [3]
        [+] Hair Care                       [4]
        [+] Makeup                          [5]
        [+] Mens Care                       [6]
        [+] Personal Care                   [7]
        [+] Skin Care                       [8]
        [+] Sexual Wellness                 [9]
        [+] Medical Supplies                [10]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Health_and_Beauty['Bath & Body']
        elif user_input_var == '2':
            return urls.Health_and_Beauty['Beauty Tools']
        elif user_input_var == '3':
            return urls.Health_and_Beauty['Fragrances']
        elif user_input_var == '4':
            return urls.Health_and_Beauty['Hair Care']
        elif user_input_var == '5':
            return urls.Health_and_Beauty['Makeup']
        elif user_input_var == '6':
            return urls.Health_and_Beauty['Mens Care']
        elif user_input_var == '7':
            return urls.Health_and_Beauty['Personal Care']
        elif user_input_var == '8':
            return urls.Health_and_Beauty['Skin Care']
        elif user_input_var == '9':
            return urls.Health_and_Beauty['Sexual Wellness']
        elif user_input_var == '10':
            return urls.Health_and_Beauty['Medical Supplies']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Womens_Fashion
    elif user_input == '3':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Unstitched Fabric               [1]
        [+] Kurtas & Shalwar Kameez         [2]
        [+] Muslim Wear                     [3]
        [+] Tops                            [4]
        [+] Bras, Panties & Lingerie        [5]
        [+] Sleepwear & Innerwear           [6]
        [+] Pants, Jeans & Leggings         [7]
        [+] Dresses & Skirts                [8]
        [+] Winter Clothing                 [9]
        [+] Shoes                           [10]
        [+] Girls Clothing                  [11]
        [+] Girls Shoes                     [12]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Womens_Fashion['Unstitched Fabric']
        elif user_input_var == '2':
            return urls.Womens_Fashion['Kurtas & Shalwar Kameez']
        elif user_input_var == '3':
            return urls.Womens_Fashion['Muslim Wear']
        elif user_input_var == '4':
            return urls.Womens_Fashion['Tops']
        elif user_input_var == '5':
            return urls.Womens_Fashion['Bras, Panties & Lingerie']
        elif user_input_var == '6':
            return urls.Womens_Fashion['Sleepwear & Innerwear']
        elif user_input_var == '7':
            return urls.Womens_Fashion['Pants, Jeans & Leggings']
        elif user_input_var == '8':
            return urls.Womens_Fashion['Dresses & Skirts']
        elif user_input_var == '9':
            return urls.Womens_Fashion['Winter Clothing']
        elif user_input_var == '10':
            return urls.Womens_Fashion['Shoes']
        elif user_input_var == '10':
            return urls.Womens_Fashion['Girls Clothing']
        elif user_input_var == '10':
            return urls.Womens_Fashion['Girls Shoes']
        else :
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Mens_Fashion
    elif user_input == '4':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] T-Shirts & Tanks                [1]
        [+] Shirts & Polo                   [2]
        [+] Pants & Jeans                   [3]
        [+] Shorts, Joggers & Sweats        [4]
        [+] Kurtas & Shalwar Kameez         [5]
        [+] Winter Clothing                 [6]
        [+] Inner Wear                      [7]
        [+] Shoes                           [8]
        [+] Accessories                     [9]
        [+] Boys Clothing                   [10]
        [+] Boys Shoes                      [11]
        [+] Boys Accessories                [12]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Mens_Fashion['T-Shirts & Tanks']
        elif user_input_var == '2':
            return urls.Mens_Fashion['Shirts & Polo']
        elif user_input_var == '3':
            return urls.Mens_Fashion['Pants & Jeans']
        elif user_input_var == '4':
            return urls.Mens_Fashion['Shorts, Joggers & Sweats']
        elif user_input_var == '5':
            return urls.Mens_Fashion['Kurtas & Shalwar Kameez']
        elif user_input_var == '6':
            return urls.Mens_Fashion['Winter Clothing']
        elif user_input_var == '7':
            return urls.Mens_Fashion['Inner Wear']
        elif user_input_var == '8':
            return urls.Mens_Fashion['Shoes']
        elif user_input_var == '9':
            return urls.Mens_Fashion['Accessories']
        elif user_input_var == '10':
            return urls.Mens_Fashion['Boys Clothing']
        elif user_input_var == '11':
            return urls.Mens_Fashion['Boys Shoes']
        elif user_input_var == '12':
            return urls.Mens_Fashion['Boys Accessories']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Babies_and_Toys
    elif user_input == '5':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Diapering & Potty               [1]
        [+] Milk Formula & Baby Food        [2]
        [+] Feeding                         [3]
        [+] Baby Gear                       [4]
        [+] Baby & Toddler Toys             [5]
        [+] Remote Control & Vehicles       [6]
        [+] Sports & Outdoor Play           [7]
        [+] Nursery                         [8]
        [+] Baby Personal Care              [9]
        [+] Clothing & Accessories          [10]
        [+] Toys & Games                    [11]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Babies_and_Toys['Diapering & Potty']
        elif user_input_var == '2':
            return urls.Babies_and_Toys['Milk Formula & Baby Food']
        elif user_input_var == '3':
            return urls.Babies_and_Toys['Feeding']
        elif user_input_var == '4':
            return urls.Babies_and_Toys['Baby Gear']
        elif user_input_var == '5':
            return urls.Babies_and_Toys['Baby & Toddler Toys']
        elif user_input_var == '6':
            return urls.Babies_and_Toys['Remote Control & Vehicles']
        elif user_input_var == '7':
            return urls.Babies_and_Toys['Sports & Outdoor Play']
        elif user_input_var == '8':
            return urls.Babies_and_Toys['Nursery']
        elif user_input_var == '9':
            return urls.Babies_and_Toys['Baby Personal Care']
        elif user_input_var == '10':
            return urls.Babies_and_Toys['Clothing & Accessories']
        elif user_input_var == '11':
            return urls.Babies_and_Toys['Toys & Games']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Home_and_Lifestyle
    elif user_input == '6':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Bath                            [1]
        [+] Bedding                         [2]
        [+] Decor                           [3]
        [+] Furniture                       [4]
        [+] Kitchen & Dining                [5]
        [+] Lighting                        [6]
        [+] Laundry & Cleaning              [7]
        [+] Tools, DIY & Outdoor            [8]
        [+] Stationery & Craft              [9]
        [+] Media, Music & Books            [10]
        [+] Charity & Donation              [11]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Home_and_Lifestyle['Bath']
        elif user_input_var == '2':
            return urls.Home_and_Lifestyle['Bedding']
        elif user_input_var == '3':
            return urls.Home_and_Lifestyle['Decor']
        elif user_input_var == '4':
            return urls.Home_and_Lifestyle['Furniture']
        elif user_input_var == '5':
            return urls.Home_and_Lifestyle['Kitchen & Dining']
        elif user_input_var == '6':
            return urls.Home_and_Lifestyle['Lighting']
        elif user_input_var == '7':
            return urls.Home_and_Lifestyle['Laundry & Cleaning']
        elif user_input_var == '8':
            return urls.Home_and_Lifestyle['Tools, DIY & Outdoor']
        elif user_input_var == '9':
            return urls.Home_and_Lifestyle['Stationery & Craft']
        elif user_input_var == '10':
            return urls.Home_and_Lifestyle['Media, Music & Books']
        elif user_input_var == '11':
            return urls.Home_and_Lifestyle['Charity & Donation']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Electronic_Devices
    elif user_input == '7':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Smart Phones                    [1]
        [+] Feature Phones                  [2]
        [+] Tablets                         [3]
        [+] Landline Phones                 [4]
        [+] Laptops                         [5]
        [+] Desktops                        [6]
        [+] Smart Watches                   [7]
        [+] Gaming Consoles                 [8]
        [+] Cameras & Drones                [9]
        [+] Security Cameras                [10]
        [+] Insurance & Protection          [11]
        [+] Daraz Like New                  [12]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Electronic_Devices['Smart Phones']
        elif user_input_var == '2':
            return urls.Electronic_Devices['Feature Phones']
        elif user_input_var == '3':
            return urls.Electronic_Devices['Tablets']
        elif user_input_var == '4':
            return urls.Electronic_Devices['Landline Phones']
        elif user_input_var == '5':
            return urls.Electronic_Devices['Laptops']
        elif user_input_var == '6':
            return urls.Electronic_Devices['Desktops']
        elif user_input_var == '7':
            return urls.Electronic_Devices['Smart Watches']
        elif user_input_var == '8':
            return urls.Electronic_Devices['Gaming Consoles']
        elif user_input_var == '9':
            return urls.Electronic_Devices['Cameras & Drones']
        elif user_input_var == '10':
            return urls.Electronic_Devices['Security Cameras']
        elif user_input_var == '11':
            return urls.Electronic_Devices['Insurance & Protection']
        elif user_input_var == '12':
            return urls.Electronic_Devices['Daraz Like New']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Electronic_Accessories
    elif user_input == '8':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Mobile Accessories              [1]
        [+] Headphones & Headsets           [2]
        [+] Wearable                        [3]
        [+] Camera Accessories              [4]
        [+] Computer Accessories            [5]
        [+] Storage                         [6]
        [+] Printers                        [7]
        [+] Computer Components             [8]
        [+] Network Components              [9]
        [+] Portable Speakers               [10]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Electronic_Accessories['Mobile Accessories']
        elif user_input_var == '2':
            return urls.Electronic_Accessories['Headphones & Headsets']
        elif user_input_var == '3':
            return urls.Electronic_Accessories['Wearable']
        elif user_input_var == '4':
            return urls.Electronic_Accessories['Camera Accessories']
        elif user_input_var == '5':
            return urls.Electronic_Accessories['Computer Accessories']
        elif user_input_var == '6':
            return urls.Electronic_Accessories['Storage']
        elif user_input_var == '7':
            return urls.Electronic_Accessories['Printers']
        elif user_input_var == '8':
            return urls.Electronic_Accessories['Computer Components']
        elif user_input_var == '9':
            return urls.Electronic_Accessories['Network Components']
        elif user_input_var == '10':
            return urls.Electronic_Accessories['Portable Speakers']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # TV_and_Home_Appliances
    elif user_input == '9':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] LED Televisions                 [1]
        [+] Smart Televisions               [2]
        [+] Home Audio                      [3]
        [+] TV Accessories                  [4]
        [+] Home Audio & Theater            [5]
        [+] Kitchen Appliances              [6]
        [+] Small Kitchen Appliances        [7]
        [+] Cooling & Heating               [8]
        [+] Irons & Garment Care            [9]
        [+] Vacuums & Floor Care            [10]
        [+] Generator & Portable Power      [11]
        [+] Washers & Dryers                [12]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.TV_and_Home_Appliances['LED Televisions']
        elif user_input_var == '2':
            return urls.TV_and_Home_Appliances['Smart Televisions']
        elif user_input_var == '3':
            return urls.TV_and_Home_Appliances['Home Audio']
        elif user_input_var == '4':
            return urls.TV_and_Home_Appliances['TV Accessories']
        elif user_input_var == '5':
            return urls.TV_and_Home_Appliances['Home Audio & Theater']
        elif user_input_var == '6':
            return urls.TV_and_Home_Appliances['Kitchen Appliances']
        elif user_input_var == '7':
            return urls.TV_and_Home_Appliances['Small Kitchen Appliances']
        elif user_input_var == '8':
            return urls.TV_and_Home_Appliances['Cooling & Heating']
        elif user_input_var == '9':
            return urls.TV_and_Home_Appliances['Irons & Garment Care']
        elif user_input_var == '10':
            return urls.TV_and_Home_Appliances['Vacuums & Floor Care']
        elif user_input_var == '11':
            return urls.TV_and_Home_Appliances['Generator & Portable Power']
        elif user_input_var == '12':
            return urls.TV_and_Home_Appliances['Washers & Dryers']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Sports_and_Outdoor
    elif user_input == '10':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Exercise & Fitness              [1]
        [+] Supplements                     [2]
        [+] Shoes & Clothing                [3]
        [+] Team Sports                     [4]
        [+] Racket Sports                   [5]
        [+] Outdoor Recreation              [6]
        [+] Fitness Gadgets                 [7]
        [+] Sports Accessories              [8]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Sports_and_Outdoor['Exercise & Fitness']
        elif user_input_var == '2':
            return urls.Sports_and_Outdoor['Supplements']
        elif user_input_var == '3':
            return urls.Sports_and_Outdoor['Shoes & Clothing']
        elif user_input_var == '4':
            return urls.Sports_and_Outdoor['Team Sports']
        elif user_input_var == '5':
            return urls.Sports_and_Outdoor['Racket Sports']
        elif user_input_var == '6':
            return urls.Sports_and_Outdoor['Outdoor Recreation']
        elif user_input_var == '7':
            return urls.Sports_and_Outdoor['Fitness Gadgets']
        elif user_input_var == '8':
            return urls.Sports_and_Outdoor['Sports Accessories']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Watches_Bags_and_Jewellery
    elif user_input == '11':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Mens Watches                    [1]
        [+] Womens Watches                  [2]
        [+] Kids Watches                    [3]
        [+] Womens Bags                     [4]
        [+] Mens Bags                       [5]
        [+] Luggage & Suitcase              [6]
        [+] Womens Jewellery                [7]
        [+] Mens Jewellery                  [8]
        [+] Mens Accessories                [9]
        [+] Womens Accessories              [10]
        [+] Sunglasses & Eyewear            [11]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Watches_Bags_and_Jewellery ['Mens Watches']
        elif user_input_var == '2':
            return urls.Watches_Bags_and_Jewellery ['Womens Watches']
        elif user_input_var == '3':
            return urls.Watches_Bags_and_Jewellery ['Kids Watches']
        elif user_input_var == '4':
            return urls.Watches_Bags_and_Jewellery ['Womens Bags']
        elif user_input_var == '5':
            return urls.Watches_Bags_and_Jewellery ['Mens Bags']
        elif user_input_var == '6':
            return urls.Watches_Bags_and_Jewellery ['Luggage & Suitcase']
        elif user_input_var == '7':
            return urls.Watches_Bags_and_Jewellery ['Womens Jewellery']
        elif user_input_var == '8':
            return urls.Watches_Bags_and_Jewellery ['Mens Jewellery']
        elif user_input_var == '9':
            return urls.Watches_Bags_and_Jewellery ['Mens Accessories']
        elif user_input_var == '10':
            return urls.Watches_Bags_and_Jewellery ['Womens Accessories']
        elif user_input_var == '11':
            return urls.Watches_Bags_and_Jewellery ['Sunglasses & Eyewear']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    # Automotive_and_Motorbike
    elif user_input == '12':
        clrscr.clear_screen()
        print(f'''
        {colors.bcolors.BOLD} Select only one option from below list {colors.bcolors.ENDC} \n {colors.bcolors.HEADER}{colors.bcolors.OKGREEN}
        [+] Automotive                      [1]
        [+] Motorcycle                      [2]
        [+] Cars                            [3]
        [+] Loaders & Rickshaw              [4]
        [+] Fuel                            [5]
        {colors.bcolors.ENDC}''')
        user_input_var = input("--> ")

        if user_input_var == '1':
            return urls.Automotive_and_Motorbike['Automotive']
        elif user_input_var == '2':
            return urls.Automotive_and_Motorbike['Motorcycle']
        elif user_input_var == '3':
            return urls.Automotive_and_Motorbike['Cars']
        elif user_input_var == '4':
            return urls.Automotive_and_Motorbike['Loaders & Rickshaw']
        elif user_input_var == '5':
            return urls.Automotive_and_Motorbike['Fuel']
        else:
            print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
            exit()


    else:
        print(f"{colors.bcolors.RED}Invalid input please try again{colors.bcolors.ENDC}")
        exit()