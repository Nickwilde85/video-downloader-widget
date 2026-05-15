@echo off
echo ========================================
echo Building Video Downloader EXE
echo ========================================
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not installed!
    pause
    exit /b 1
)

echo Installing PyInstaller...
pip install pyinstaller

echo.
echo Building EXE file...
pyinstaller --onefile --windowed --name "VideoDownloader" --icon=NONE video_downloader.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo EXE file location: dist\VideoDownloader.exe
echo.
echo You can now:
echo 1. Copy VideoDownloader.exe to any location
echo 2. Create a desktop shortcut
echo 3. Share with others (they don't need Python)
echo.
pause
