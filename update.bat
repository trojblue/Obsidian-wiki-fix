@echo off

cd D:\CSC2\Obsidian-wiki-fix\src
python app.py
cd D:\quartz

for /F "tokens=2" %%i in ('date /t') do set mydate=%%i
set mytime=%time%

git add .
git commit -m "automatic commit %mydate% : %mytime%"
git push

echo.
echo.

echo ==============================================
echo  upload done! will auto-exit after 10 seconds
echo ==============================================
choice /d y /t 20 > nul
echo "exit.."