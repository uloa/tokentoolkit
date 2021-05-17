@ECHO OFF

:without
echo GETTING THINGS READY...
pyinstaller --onefile GrabberInstaller.py
@RD /S /Q "build"
@RD /S /Q "__pycache__"
del NOGUIGrabberInstaller.spec
exit