@echo off
echo Creating desktop shortcut...

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Video Downloader.lnk'); $Shortcut.TargetPath = '%CD%\run.bat'; $Shortcut.WorkingDirectory = '%CD%'; $Shortcut.Description = 'Video Downloader Widget'; $Shortcut.Save()"

echo.
echo Desktop shortcut created successfully!
echo You can now run Video Downloader from your desktop.
pause
