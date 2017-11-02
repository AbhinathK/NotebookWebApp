:: Comment - Replace ALL Occurences of "C:\Users\M...." with "C:\Users\YOUR_UER_NAME...."
mkdir C:\Users\M\NoteApp\DatabaseOnlyBackups
cd C:\Users\M\NoteApp\DatabaseOnlyBackups
git clone https://github.com/AbhinathK/NotebookWebApp
ren NotebookWebApp Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%
cd Backup_%time:~0,2%%time:~3,2%-%date:~-10,2%%date:~3,2%%date:~-4,4%
mkdir temp
move db.sqlite3 temp
erase /f /q *.*
move temp\* .
rmdir temp
rmdir /S /Q notebook
rmdir /S /Q notebooks