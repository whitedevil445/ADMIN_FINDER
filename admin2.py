import requests

import os

from colorama import Fore #module for giving colours to your results

print("""
   █████████   ██████████   ██████   ██████ █████ ██████   █████           ███████████ █████ ██████   █████ ██████████   ██████████ ███████████  
  ███░░░░░███ ░░███░░░░███ ░░██████ ██████ ░░███ ░░██████ ░░███           ░░███░░░░░░█░░███ ░░██████ ░░███ ░░███░░░░███ ░░███░░░░░█░░███░░░░░███ 
 ░███    ░███  ░███   ░░███ ░███░█████░███  ░███  ░███░███ ░███            ░███   █ ░  ░███  ░███░███ ░███  ░███   ░░███ ░███  █ ░  ░███    ░███ 
 ░███████████  ░███    ░███ ░███░░███ ░███  ░███  ░███░░███░███            ░███████    ░███  ░███░░███░███  ░███    ░███ ░██████    ░██████████  
 ░███░░░░░███  ░███    ░███ ░███ ░░░  ░███  ░███  ░███ ░░██████            ░███░░░█    ░███  ░███ ░░██████  ░███    ░███ ░███░░█    ░███░░░░░███ 
 ░███    ░███  ░███    ███  ░███      ░███  ░███  ░███  ░░█████            ░███  ░     ░███  ░███  ░░█████  ░███    ███  ░███ ░   █ ░███    ░███ 
 █████   █████ ██████████   █████     █████ █████ █████  ░░█████ █████████ █████       █████ █████  ░░█████ ██████████   ██████████ █████   █████
░░░░░   ░░░░░ ░░░░░░░░░░   ░░░░░     ░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░ ░░░░░       ░░░░░ ░░░░░    ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░   ░░░░░ 
                                                                                                                                                 
                                                                                                                                                 
                                                                                                                                                 
""")





admin=input("your file name:") #your file name or path..
#file must be in same folder if you are giving name only like admin.txt

admin_words = open(admin, 'r' )#for reading the list we r using 'r' 

website = input("your website name here :")

correct_url = "https://"+website #it is used for only if u r giving name example google.com

http = requests.get(correct_url).status_code

if http ==200:
    print("your target is up")
    for i in admin_words:
        https = requests.get(correct_url+"/"+i).status_code
        if https ==200:
            print(Fore.GREEN+"Admin url find :"+correct_url+"/"+i)
            pass
        else:
            print(Fore.RED+"your url is not exist:"+correct_url+"/"+i)
            pass



else:
    print("your website is down")  