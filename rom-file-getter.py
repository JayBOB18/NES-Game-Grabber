import requests
import subprocess
import os
import pathlib
import glob
import sys
from bs4 import BeautifulSoup
import linecache

rom_number = "omega lul"

gamelist = open("games.txt")
romlist = open("temp_urls.txt")

page_url = "https://archive.org/download/NintendoNintendoEntertainmentSystem20140825.7z/Nintendo%20-%20Nintendo%20Entertainment%20System%20%2820140825%29.7z/"
page_reqs = requests.get(page_url, allow_redirects=True)
open('temp_urls.txt', 'wb').write(page_reqs.content)

search = input("Search for a game (case sensitive) or enter tutorial   ")
if search == "tutorial":
    print("Simply search for a game and enter the number above it when prompted.")
    search = input("Search for a game (case sensitive)   ")
print("Showing results for " + search)


soup = BeautifulSoup(page_reqs.text, 'html.parser')

urls = []



searchlines = gamelist.readlines()
for position, line in enumerate(searchlines):
    if search in line:
        rom_number = position
        print(rom_number)
        print(line)


searchlines = romlist.readlines()
chosen_rom = int(input("Enter the number for your game.   "))

chosen_rom = chosen_rom + 1656

rom_url = linecache.getline("C:/Users/jakob/Downloads/Misc/Python/Projects/nes-game-grabber/temp_urls.txt",chosen_rom)
rom_url = rom_url.replace('<tr><td><a href="//', '')
sep = '">Nintendo'
rom_url = rom_url.split(sep, 1)[0]
rom_url = "https://" + rom_url


rom_reqs = requests.get(rom_url, allow_redirects=True)
open('game.nes', 'wb').write(rom_reqs.content)


path = r"./*.nes"
file = str(glob.glob(path))
file = file.replace("[", "")
file = file.replace("]", "")
file = file.replace("\\", "")
file = file.replace(".", "",1)
file = file.replace("'" , "")

emu_path = input("Give the path to your emulator  ")

gamelist.close()
romlist.close()


subprocess.Popen([emu_path, file])
done = input("Are you done? (y/n)   ")
if done == "n":
    pass
elif done == "y":
    os.remove("./game.nes")
    exit()
