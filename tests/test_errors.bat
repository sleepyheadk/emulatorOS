@echo off
cd /d "%~dp0.."
echo [TEST] Несуществующая VFS и несуществующий скрипт
call run.bat --vfs no_such_dir --script no_such_file.txt
echo [TEST] Неизвестный параметр
call run.bat --unknown
