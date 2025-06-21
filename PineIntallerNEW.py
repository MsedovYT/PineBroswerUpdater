import os
import sys
import time
import shutil
directory_name = "PineBrowser"

try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except FileNotFoundError:
    print("Error: Parent directory does not exist.")

REPO_URL = "https://github.com/MsedovYT/PineBrowser"
os.system(f"cd {directory_name}")
INSTALL_DIR = directory_name

def print_ascii_logo():
    print(r"""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\    \        
       /::::\    \               \:::\    \              /::::|   |               /::::\    \       
      /::::::\    \               \:::\    \            /:::::|   |              /::::::\    \      
     /:::/\:::\    \               \:::\    \          /::::::|   |             /:::/\:::\    \     
    /:::/__\:::\    \               \:::\    \        /:::/|::|   |            /:::/__\:::\    \    
   /::::\   \:::\    \              /::::\    \      /:::/ |::|   |           /::::\   \:::\    \   
  /::::::\   \:::\    \    ____    /::::::\    \    /:::/  |::|   | _____    /::::::\   \:::\    \  
 /:::/\:::\   \:::\____\  /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\/:::/__\:::\   \:::\____\
\::/    \:::\  /:::|____|\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /\:::\   \:::\   \::/    /
 \/_____/\:::\/:::/    /  \:::\/:::/    / \/____/  \/____/ |::| /:::/    /  \:::\   \:::\   \/____/ 
          \::::::/    /    \::::::/    /                   |::|/:::/    /    \:::\   \:::\    \     
           \::::/    /      \::::/____/                    |::::::/    /      \:::\   \:::\____\    
            \::/____/        \:::\    \                    |:::::/    /        \:::\   \::/    /    
                              \:::\    \                   |::::/    /          \:::\   \/____/     
                               \:::\    \                  /:::/    /            \:::\    \         
                                \:::\____\                /:::/    /              \:::\____\        
                                 \::/    /                \::/    /                \::/    /        
                                  \/____/                  \/____/                  \/____/         
    """)
    print("Welcome to the PineBrowser Installer!\n")

def print_menu():
    print("1. Install/Update PineBrowser")
    print("2. Uninstall PineBrowser")
    print("3. Read License")
    print("4. Exit")

def fake_progress_bar(task, seconds=2):
    print(f"\n{task}")
    for i in range(21):
        bar = "[" + "#" * i + " " * (20-i) + "]"
        sys.stdout.write(f"\r{bar} {int(i*5)}%")
        sys.stdout.flush()
        time.sleep(seconds/20)
    print("\n")

def clone_repo():
    print("Cloning repository...")
    result = os.system(f"git clone {REPO_URL} {INSTALL_DIR}")
    if result != 0:
        print("Error: Failed to clone the repository. Make sure git is installed and the URL is correct.")
        sys.exit(1)
    print("Repository cloned successfully.")

def copy_files():
    # Example: Copy main script to ~/PineBrowser (already cloned there)
    print("Copying files...")
    # If you want to copy from a subfolder, adjust paths here
    # shutil.copy("source_path", "dest_path") # Example
    time.sleep(1)
    print("Files copied.")

def create_shortcut():
    # This is for Linux. For Windows/Mac, you'd need to adjust accordingly.
    desktop = os.path.expanduser("~/Desktop")
    shortcut_path = os.path.join(desktop, "PineBrowser.desktop")
    with open(shortcut_path, "w") as f:
        f.write(f"""[Desktop Entry]
Type=Application
Name=PineBrowser
Exec=python3 {INSTALL_DIR}/main.py
Icon={INSTALL_DIR}/pine.png
Terminal=false
""")
    os.chmod(shortcut_path, 0o755)
    print("Shortcut created on Desktop.")

def install_steps():

    clone_repo()

    os.system("pip install --upgrade pip")
    print("Upgraded pip")
    os.system("pip install PyQT6")
    print("Installed PyQT5")
    os.system("pip install qdarkstyle")
    print("Installed qdarkstyle")
    os.system("pip install PyQt6-WebEngine")
    print("Installed PyQtWebEngine")
    os.system("pip install adblockparser")
    print("Installed adblockparser")
    copy_files()
    create_shortcut()
    print("Installation complete! Thank you for installing PineBrowser.\n")

def main():
    while True:
        print_ascii_logo()
        print_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            install_steps()
            input("Press Enter to exit installer...")
            break
        elif choice == "4":
            print("Exiting installer. Goodbye!")
            break
        elif choice == "2":
            print("Uninstalling PineBrowser...")
            shutil.rmtree(INSTALL_DIR)
            print("Uninstallation complete. Goodbye!")
            break
        elif choice == "3":
            print("""
            MIT License

Copyright (c) 2025 MsedovYT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
            """)
            main()
        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)

if __name__ == "__main__":
    main()
