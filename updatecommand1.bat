setlocal enabledelayedexpansion

:move_file
move "C:\Users\Haydar\Downloads\XVXBROWSERUPD.pak"  "%~dp0"
if errorlevel 1 (
    echo "Move failed. Retrying..."
    goto move_file
) else (
    python update.py
    echo "File moved successfully."
)