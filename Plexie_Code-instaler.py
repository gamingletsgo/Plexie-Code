import os
os.system("pip install keyboard"
)
import keyboard
import subprocess
import webbrowser
import time
import base64

page = 11
prees = True

def dialog_load():
    time.sleep(0.1)
    global page, prees
    prees = True
    os.system("cls")

    if page == 11:
        print("""Welckome to Plexie Code Installer
Click on Install to start the Instalation and Cancel to Close the Installer
Use arow keys to Select and Enter to Confirm""")
        print("\n>Cancel             Install")
        while prees:
            if keyboard.is_pressed("right"):
                page = 12
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):
                quit()

    if page == 12:
        print("""Welckome to Plexie Code Installer
Click on Install to start the Instalation and Cancel to Close the Installer
Use arow keys to Select and Enter to Confirm""")
        print("\n Cancel            >Install")
        while prees:
            if keyboard.is_pressed("left"):
                page = 11
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):
                print("\nCreating Folder")
                os.makedirs("C:/Plexie_Code/servers", exist_ok=True)  
                print("Instaling Flask")
                os.system("pip install flask requests")                      
                print("Creating Sb3 File")
                with open("C:/Plexie_Code/main.sb3", "wb") as f:
                    f.write(base64.b64decode("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"))
                prees = False
                page = 41
                dialog_load()

    if page == 21:
        print("""Create Launcher?""")
        print("\n>Yes             No")
        while prees:
            if keyboard.is_pressed("right"):
                page = 22
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):
                with open("plexie_code_Launcher.py", "w") as f:
                    f.write(r"""import os
import subprocess


local_appdata = os.environ['LOCALAPPDATA']

tw_exe = os.path.join(local_appdata, 'Programs', 'TurboWarp', 'TurboWarp.exe')


project_file = r'C:\plexie_code\main.sb3'


subprocess.run([tw_exe, project_file])

# dieser code ist ki generiert. dieser kmand aber nciht."
# 
""")
                page = 31
                dialog_load()

    if page == 22:
        print("""Create Launcher?""")
        print("\n Yes            >No")
        while prees:
            if keyboard.is_pressed("left"):
                page = 21
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):          
                press = False
                page = 31
                dialog_load()


    if page == 41:
        print("""Is Turbowarp Instaled?""")
        print("\n>Yes             No")
        while prees:
            if keyboard.is_pressed("right"):
                page = 42
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):
                page = 22
                prees = False                
                dialog_load()

    if page == 42:
        print("""Is Turbowarp Instaled?""")
        print("\n Yes            >No")
        while prees:
            if keyboard.is_pressed("left"):
                page = 41
                prees = False
                dialog_load()
            if keyboard.is_pressed("enter"):
                webbrowser.open("https://desktop.turbowarp.org/")
                quit()

    if page == 31:
        time.sleep(1)
        print("Done.")
        while prees:
            if keyboard.is_pressed("enter"):
                quit()
        
    
dialog_load()
