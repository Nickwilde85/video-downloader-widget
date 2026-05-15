@echo off
echo ========================================
echo Upload to GitHub Helper
echo ========================================
echo.

REM Проверка git
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is NOT installed!
    echo.
    echo Option 1: Install Git
    echo Download from: https://git-scm.com/download/win
    echo.
    echo Option 2: Use GitHub Desktop (EASIER!)
    echo Download from: https://desktop.github.com/
    echo.
    pause
    exit /b 1
)

echo Git is installed!
echo.
echo ========================================
echo Step 1: Initialize repository
echo ========================================
git init
if errorlevel 1 (
    echo Already initialized or error occurred
)

echo.
echo ========================================
echo Step 2: Add all files
echo ========================================
git add .

echo.
echo ========================================
echo Step 3: Create first commit
echo ========================================
git commit -m "Initial commit: Video Downloader Widget v1.0"

echo.
echo ========================================
echo SUCCESS! Local repository ready!
echo ========================================
echo.
echo NEXT STEPS:
echo.
echo 1. Go to: https://github.com/new
echo.
echo 2. Fill in:
echo    - Repository name: video-downloader-widget
echo    - Description: Modern Windows widget for downloading videos from 1000+ sites
echo    - Public: YES
echo    - Add README/LICENSE: NO (we have them)
echo.
echo 3. Click "Create repository"
echo.
echo 4. Copy YOUR repository URL and run:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/video-downloader-widget.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Replace YOUR_USERNAME with your actual GitHub username!
echo.
echo ========================================
pause
