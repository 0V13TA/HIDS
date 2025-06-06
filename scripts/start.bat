@echo off
REM Activate the virtual environment
call ..\.venv\Scripts\activate

REM Change to the project root directory
cd ..

REM Run the HIDS main script in a new background window and log output
start /b python main.py > hids.log 2>&1