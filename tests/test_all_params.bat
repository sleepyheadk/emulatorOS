@echo off
cd /d "%~dp0.."
echo [TEST] Оба параметра, скрипт с ошибочными строками
call run.bat --vfs vfs --script scripts\startup_errors.txt

