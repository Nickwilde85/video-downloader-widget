Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = oWS.SpecialFolders("Desktop") & "\Video Downloader.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = WScript.ScriptFullName
oLink.WorkingDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
oLink.Arguments = ""
oLink.Description = "Video Downloader Widget"
oLink.WindowStyle = 1
oLink.Save

' Создаем ярлык для запуска
sLinkFile2 = oWS.SpecialFolders("Desktop") & "\Video Downloader.lnk"
Set oLink2 = oWS.CreateShortcut(sLinkFile2)
oLink2.TargetPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName) & "\run.bat"
oLink2.WorkingDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
oLink2.Description = "Video Downloader Widget"
oLink2.WindowStyle = 1
oLink2.Save

MsgBox "Ярлык создан на рабочем столе!", vbInformation, "Готово"
