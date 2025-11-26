@echo off
REM --- Get current refresh rate via PowerShell ---
for /f "usebackq delims=" %%a in (`powershell -NoProfile -Command "(Get-CimInstance Win32_VideoController | Select-Object -First 1 -ExpandProperty CurrentRefreshRate).ToString()"`) do set "hz=%%a"

echo Detected refresh rate: %hz%

REM --- Toggle between 144 and 120 ---
if "%hz%"=="144" (
    echo Switching to 120Hz...
    "C:\Program Files (x86)\Qres\QRes.exe" /r:120
) else (
    echo Switching to 144Hz...
    "C:\Program Files (x86)\Qres\QRes.exe" /r:144
)
