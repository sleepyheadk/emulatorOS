@echo off
cd /d "%~dp0.."
echo [TEST] Только --script
call run.bat --script scripts\startup_ok.txt
