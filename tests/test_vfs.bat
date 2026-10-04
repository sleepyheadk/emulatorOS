@echo off
cd /d "%~dp0.."
echo [TEST] Только --vfs
call run.bat --vfs vfs
