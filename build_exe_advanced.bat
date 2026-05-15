@echo off
echo ========================================
echo Building Video Downloader EXE (Advanced)
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
echo Building EXE with all dependencies...
pyinstaller --onefile ^
    --windowed ^
    --name "VideoDownloader" ^
    --icon=NONE ^
    --add-data "README.md;." ^
    --hidden-import=yt_dlp ^
    --hidden-import=tkinter ^
    --collect-all yt_dlp ^
    video_downloader.py

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
echo EXE file: dist\VideoDownloader.exe
echo Size: 
dir dist\VideoDownloader.exe | find "VideoDownloader.exe"
echo.
echo The EXE is portable and includes:
echo - Python runtime
echo - All required libraries
echo - yt-dlp for video downloading
echo.
echo Note: FFmpeg is NOT included. For best quality:
echo - Install FFmpeg separately OR
echo - Place ffmpeg.exe in the same folder as VideoDownloader.exe
echo.
pause
