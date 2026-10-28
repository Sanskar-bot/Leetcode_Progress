' ============================================================
'  LeetCode Tracker — Startup Launcher
'  Launches the modern WPF popup silently on login
'  Shortcut to this file lives in Windows Startup folder
' ============================================================

Dim shell
Set shell = CreateObject("WScript.Shell")
shell.Run "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File ""C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\startup_prompt.ps1""", 0, False
