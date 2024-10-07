@echo off
title ENoW builder
del .\dist\ENoW.exe
pyinstaller --onefile main.py
rename .\dist\main.exe ENoW.exe