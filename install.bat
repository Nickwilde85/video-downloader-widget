@echo off
echo Установка Video Downloader Widget...
echo.

REM Проверка Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Python не установлен!
    echo Скачайте Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Установка зависимостей...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ОШИБКА: Не удалось установить зависимости
    pause
    exit /b 1
)

echo.
echo Установка завершена успешно!
echo Запустите run.bat для старта приложения
pause
