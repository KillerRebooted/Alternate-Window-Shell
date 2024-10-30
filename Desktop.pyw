import os
from icoextract import IconExtractor
import customtkinter as ctk
from PIL import Image
import win32com.client 
import getpass

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

win = ctk.CTk(fg_color="#121212")
win.title("Hidden Files")

User = getpass.getuser()

dir = [fr"C:\Users\{User}\Desktop", r"C:\Users\Public\Desktop"]

files = []

for file in os.listdir(dir[0]):

    file_path = os.path.join(dir[0], file)

    #hidden_attribute = os.popen(f'attrib "{file_path}"').read().split()[1]
    
    files.append(file_path)

for file in os.listdir(dir[1]):

    file_path = os.path.join(dir[1], file)

    #hidden_attribute = os.popen(f'attrib "{file_path}"').read().split()[1]
    
    files.append(file_path)

r, c = 0, 0

for file in files:

    try:

        print(file)

        if file.endswith("desktop.ini"):
            continue

        if file.endswith(".lnk"):

            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(file)
            target = shortcut.Targetpath

            extractor = IconExtractor(target)
            data = extractor.get_icon(num=0)
            img = Image.open(data)

        elif file.endswith(".exe"):

            target = file

            extractor = IconExtractor(target)
            data = extractor.get_icon(num=0)
            img = Image.open(data)

        elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            
            img = Image.open(file)

        else:

            img = Image.open(os.path.join(os.path.dirname(__file__), "placeholder.png"))


        button = ctk.CTkButton(win, text=os.path.basename(file), height=50, width=50, image=ctk.CTkImage(dark_image=img, size=(50,50)), command=lambda file=file: os.startfile(file))

    except Exception as e:

        print(e)

        img = Image.open(os.path.join(os.path.dirname(__file__), "placeholder.png"))
        
        button = ctk.CTkButton(win, text=os.path.basename(file), height=50, width=50, image=ctk.CTkImage(dark_image=img, size=(50,50)), command=lambda file=file: os.startfile(file))

    button.grid(row=r, column=c)

    if c == 7:
        r += 1
        c = -1
    c += 1

    print()

win.mainloop()