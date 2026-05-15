@echo off
echo ========================================
echo Установка FFmpeg для максимального качества
echo ========================================
echo.

REM Проверка наличия winget
winget --version >nul 2>&1
if errorlevel 1 (
    echo Winget не найден. Используем альтернативный метод...
    goto manual_install
)

echo Установка FFmpeg через winget...
winget install --id=Gyan.FFmpeg -e
goto check_install

:manual_install
echo.
echo Скачайте FFmpeg вручную:
echo 1. Откройте: https://www.gyan.dev/ffmpeg/builds/
echo 2. Скачайте: ffmpeg-release-essentials.zip
echo 3. Распакуйте в C:\ffmpeg
echo 4. Добавьте C:\ffmpeg\bin в PATH
echo.
echo Или используйте Chocolatey:
echo   choco install ffmpeg
echo.
pause
exit /b 0

:check_install
echo.
echo Проверка установки...
timeout /t 2 >nul
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ВНИМАНИЕ: FFmpeg не найден в PATH
    echo Перезапустите командную строку или компьютер
) else (
    echo.
    echo ✓ FFmpeg успешно установлен!
)

echo.
pause
