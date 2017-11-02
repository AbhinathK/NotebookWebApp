@echo off
:: Comment - This script assumes you have the app saved as NotebookWebApp in NoteApp Directory, Replace ALL Occurences of "C:\Users\M...." with "C:\Users\YOUR_UER_NAME...."
mkdir C:\Users\M\NoteApp\LocalHostBackups\newFolder
cd C:\Users\M\NoteApp\LocalHostBackups
xcopy /R /E /S /Y C:\Users\M\NoteApp\NotebookWebApp C:\Users\M\NoteApp\LocalHostBackups\newFolder
ren newFolder Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%