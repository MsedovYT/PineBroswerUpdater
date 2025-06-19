import requests
import os
print("Welcome to Pine updater!")
print("Press [Enter] to continue...")
input()
print("Fetching raw file...")
url = "https://raw.githubusercontent.com/MsedovYT/PineBrowser/refs/heads/main/pine.py"
print("Fetched!")
print("Updating...")
response = requests.get(url)
with open("pine.py", "wb") as f:
    f.write(response.content)
print("Updated!")
print("Installing dependencies...")
print("Running with admin privileges...")
os.system("pip install --upgrade pip")
print("Upgraded pip")
os.system("pip install PyQT5")
print("Installed PyQT5")
os.system("pip install qdarkstyle")
print("Installed qdarkstyle")
os.system("pip install PyQtWebEngine")
print("Installed PyQtWebEngine")
os.system("pip install adblockparser")
print("Installed adblockparser")
print("Installed dependencies!")
print("Finished!")
print("Press [Enter] to exit...")
print("Press [r] to run Pine...")
user = input()
if user == "r":
    os.system("python pine.py")
else:
    exit()

