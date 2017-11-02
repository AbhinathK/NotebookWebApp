@echo off
:: Comment - Replace ALL Occurences of "C:\Users\M...." with "C:\Users\YOUR_UER_NAME...."
mkdir C:\Users\M\NoteApp\Backups
cd C:\Users\M\NoteApp\Backups
git clone https://github.com/AbhinathK/NotebookWebApp
ren NotebookWebApp Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%
cd Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%