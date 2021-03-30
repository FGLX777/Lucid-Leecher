import requests, os, colorama, random, string,time,re
from bs4 import BeautifulSoup
from time import sleep
from os import system
from colorama import Fore, Style
colorama.init()


system('mode con: cols=35 lines=13')

def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring

def logo():
    msg = Fore.LIGHTBLUE_EX +"""
          ╦  ┬ ┬┌─┐┬┌┬┐
          ║  │ ││  │ ││
          ╩═╝└─┘└─┘┴─┴┘
    """
    print(msg)
    
def menu():
    print("{} ╔═════════Lucid Menu══════════╗{}".format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX))
    print(Fore.LIGHTMAGENTA_EX + " ║" + Fore.LIGHTBLUE_EX + "[1] -" + Fore.RESET + "Searcher" + Fore.LIGHTMAGENTA_EX + " ║"+ Fore.LIGHTBLUE_EX + " [2] -" + Fore.RESET + "Leecher " + Fore.LIGHTMAGENTA_EX + "║")
    print("{} ╚═════════════════════════════╝{}".format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTWHITE_EX))
    print("")

def leech():
    com = 0
    failed = 0
    combo = 0
    logo()
    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+"Import Links")
    txt = input("")
    with open(txt) as f:
            for line in f:
                paste = line.strip("\n")
                try:
                    res = requests.get(f"{paste}")
                    com += 1
                    os.system("cls")
                    logo()
                    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Scaped Links [{com}]")
                    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Failed [{failed}]")
                    with open("combos.txt", "a+") as k:
                        k.writelines(res.text)
                except:
                    failed += 1
                    os.system("cls")
                    logo()
                    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Scaped Links [{com}]")
                    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Failed [{failed}]")
    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+"Remove duplicates (y/n)")
    rd = input("")
    if rd == "y":
        with open('combos.txt') as result:
            uniqlines = set(result.readlines())
            with open('combos.txt', 'w') as rmdup:
                rmdup.writelines(set(uniqlines))
    else:
        pass
    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+"Count the number of combos (y/n)")
    count = input("")
    if count == "y":
        with open("combos.txt") as f:
            for line in f:
                combo += 1
                os.system("cls")
                logo()
                print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Accounts [{combo}]")
    else:
        pass
    main()
    
def search():
    key = 0
    lin = 0
    logo()
    print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+"Import Keywords")
    txt = input("")
    os.system("cls")
    logo()
    with open(txt) as f:
            for line in f:
                keyword = line.strip("\n")
                url = f"https://www.google.com/search?q=site:pastebin.com+{keyword}"
                key += 1
                links=[]
                website = requests.get(url)
                website_text = website.text
                soup = BeautifulSoup(website_text,"html.parser")
                for link in soup.find_all('a'):
                    links.append(link.get('href'))
                for link in links:
                    if "https://pastebin.com/" in link:
                        split_string = link.split("&", 1)
                        link = split_string[0]
                        newlink = link.replace('/url?q=', '')
                        os.system("cls")
                        logo()
                        print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Keywords Used [{key}]")
                        print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+f"Links Found [{lin}]")
                        lin += 1
                        with open("Links.txt", "a+") as (f):
                            f.writelines(insertChar(newlink,21, 'raw/')+"\n")
                    else:
                        pass
    main()

def main():
    os.system("cls")
    logo()
    menu()
    option = int(input(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX))
    while option != 0:
        if option == 1:
            os.system("cls")
            search()
        elif option == 2:
            os.system("cls")
            leech()
        else:
            os.system("cls")
            print(Fore.RESET +"~$>"+Fore.LIGHTMAGENTA_EX+"Error")

main()
