
Dim sName
Dim fso
Dim fol

' kreira filesystem
Set fso = WScript.CreateObject("Scripting.FileSystemObject")
    
Set fol = fso.GetFolder(".")


For Each fil In fol.Files
    ' provjera za space
    If InStr(1, fil.Name, " ") <> 0 Then
        ' replace spejsa s underskorom
        sName = Replace(fil.Name, " ", "_")
        ' rename datoteke
        fil.Name = sName
    End If
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "c")
        fil.Name = sName
    End If
   
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "c")
        fil.Name = sName
    End If
Next    
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "C")
        fil.Name = sName
    End If
Next    
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "C")
        fil.Name = sName
    End If
Next     
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "S")
        fil.Name = sName
    End If
Next   
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "s")
        fil.Name = sName
    End If
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "D")
        fil.Name = sName
    End If
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "d")
        fil.Name = sName
    End If
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "Z")
        fil.Name = sName
    End If
Next
'�
For Each fil In fol.Files
    If InStr(1, fil.Name, "�") <> 0 Then
        sName = Replace(fil.Name, "�", "z")
        fil.Name = sName
    End If
Next

WScript.Echo "Gotovo!"