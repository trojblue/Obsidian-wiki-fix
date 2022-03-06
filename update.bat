@echo off

set FIX_DIR = "D:\CSC2\Obsidian-wiki-fix\src"
set QUARTZ_DIR = "D:\quartz"

cd %SOURCE_DIR%
python app.py
cd %QUARTZ_DIR%

for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%

git add .
git commit -m "automatic commit %mydate% : %mytime%"
git push


echo "upload done! will auto-exit after 10 seconds"
choice /d y /t 10 > nul
echo "exit.."