#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; HOTKEY: Ctrl+Alt+H
^!h::
{
    qresPath := "C:\Program Files (x86)\Qres\QRes.exe"
    if !FileExist(qresPath) {
        TrayTip, Refresh Rate, QRes not found:`n%qresPath%, 5
        return
    }

    ; === Get monitor info via WMI (reliable) ===
    try {
        wbem := ComObjGet("winmgmts:\\.\root\CIMV2")
        colItems := wbem.ExecQuery("Select * from Win32_VideoController")
    } catch {
        TrayTip, Refresh Rate, Failed to query WMI., 5
        return
    }

    CurHz := ""
    CurW := ""
    CurH := ""
    for item in colItems {
        ; Use the first controller that has a numeric CurrentRefreshRate
        if (item.CurrentRefreshRate) {
            CurHz := item.CurrentRefreshRate
            ; Some WMI classes expose CurrentHorizontalResolution / CurrentVerticalResolution
            if (item.CurrentHorizontalResolution)
                CurW := item.CurrentHorizontalResolution
            if (item.CurrentVerticalResolution)
                CurH := item.CurrentVerticalResolution
            break
        }
    }

    if (CurHz = "") {
        TrayTip, Refresh Rate, Could not detect current refresh rate via WMI., 4
        return
    }

    ; If resolution not found via WMI, try a fallback (use screen size)
    if (CurW = "" || CurH = "") {
        CurW := A_ScreenWidth
        CurH := A_ScreenHeight
    }

    ; Decide target
    if (CurHz = 144)
        target := 120
    else
        target := 144

    TrayTip, Refresh Rate, Detected %CurHz% Hz @ %CurW%x%CurH% — switching to %target%Hz..., 2

    ; Run QRes specifying resolution + refresh (more reliable)
    ; Example: "C:\Program Files (x86)\Qres\QRes.exe" /x:1920 /y:1080 /r:120
    cmd := ComSpec " /c """ qresPath """ /x:" CurW " /y:" CurH " /r:" target
    RunWait, %cmd%, , Hide

    Sleep, 600

    ; Verify using WMI again
    newHz := ""
    colItems2 := wbem.ExecQuery("Select * from Win32_VideoController")
    for item2 in colItems2 {
        if (item2.CurrentRefreshRate) {
            newHz := item2.CurrentRefreshRate
            break
        }
    }

    if (newHz = target)
        TrayTip, Refresh Rate, Success — now at %newHz% Hz., 2
    else
        TrayTip, Refresh Rate, Attempted %target%Hz but detected %newHz% (try running as admin), 5

    return
}
