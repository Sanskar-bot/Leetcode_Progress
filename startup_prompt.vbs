' ============================================================
'  LeetCode Tracker — Startup Prompt
'  Shows a popup on login asking to update progress
'  Place shortcut to this file in Windows Startup folder
' ============================================================

Dim answer
answer = MsgBox("🧑‍💻 LeetCode Tracker" & vbCrLf & vbCrLf & _
                "Do you want to update your LeetCode progress" & vbCrLf & _
                "and push to GitHub now?" & vbCrLf & vbCrLf & _
                "Last updated: Check progress_tracker.json", _
                vbYesNo + vbQuestion, _
                "LeetCode Daily Update")

If answer = vbYes Then
    Dim shell
    Set shell = CreateObject("WScript.Shell")
    shell.Run "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File ""C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\update_progress.ps1""", 0, False
    WScript.Sleep 2000
    MsgBox "✅ Update started!" & vbCrLf & vbCrLf & "Your LeetCode progress is being synced to GitHub in the background.", _
           vbOKOnly + vbInformation, "LeetCode Tracker"
End If
