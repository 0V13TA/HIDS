@echo off
REM Activate the virtual environment
call ..\.venv\Scripts\activate

REM Change to the project root directory
cd ..

REM Run the HIDS main script
python main.py

REM Pause so the window stays open if run by double-click
pause