@echo off
:: Comment - This script assumes you have the app saved as NotebookWebApp in NoteApp Directory, Change ALL'M'to your User Name
mkdir C:\Users\M\NoteApp\LocalHostDatabaseOnlyBackups\newFolder
cd C:\Users\M\NoteApp\LocalHostDatabaseOnlyBackups
xcopy /R /E /S /Y C:\Users\M\NoteApp\NotebookWebApp C:\Users\M\NoteApp\LocalHostDatabaseOnlyBackups\newFolder
ren newFolder Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%
mkdir temp
move db.sqlite3 temp
erase /f /q *.*
move temp\* .
rmdir temp
rmdir /S /Q notebook
rmdir /S /Q notebooks