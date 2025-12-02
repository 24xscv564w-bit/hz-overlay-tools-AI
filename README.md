# hz_overlay
Ready to use lightweight Windows overlay to indicate monitor refresh rate. The overlays alone under 15kb, total repo 18.5mb

👉 **[Download Latest Release](https://github.com/24xscv564w-bit/hz-overlay/releases/latest)** 
### AI part
Human tweaked AI code
## Overlay Preview
Clean Hz detection (**`hz_overlay.py`** and **`Stay_Overlay.py`**)

![Overlay Screenshot](Screenshot_144.png) ![Overlay Screenshot](Screenshot_Transparent144hz.png) 

## Main tools
 **`hz_overlay.py`**  [⬇️] https://github.com/24xscv564w-bit/hz-overlay-tools/blob/main/hz_overlay.py
<a id="raw-url" href="https://github.com/username/repo/blob/main/hz_overlay.py?raw=1" download>Download</a>
 >  - **`Stay_Overlay.py`** *Ready to Use* https://github.com/24xscv564w-bit/hz-overlay-tools/blob/main/Stay_Overlay.py
 -------------  
 > - **`AHK toggle`** Add to **`shell:startup`** *Check Path*, install **`Qres`**  https://github.com/24xscv564w-bit/hz-overlay-tools/blob/main/ToggleHZ.ahk.ahk 
 > - **`Start_Hz_Overlay.bat`** *Edit path* https://github.com/24xscv564w-bit/hz-overlay-tools/blob/main/Start_Hz_Overlay.bat
 > - **`Start_Hz_Overlay Shortcut (.lnk)`** Add to **`shell:startup`** (https://github.com/24xscv564w-bit/hz-overlay-tools/blob/main/Start_Hz_Overlay%20-%20Shortcut.lnk) **
 ## Notes"
 > - AHK switches hz and requires Qres to be in C:\Program Files (x86)\Qres\QRes.exe or customized path updated in notepad.
 >  - **`Stay_Overlay.py`** Always on, simple and is not distracting.
 >     

---

## Features
- Detects display refresh rate using Win32 API.
- Displays 120Hz as an animated rainbow text with a subtle nudge animation.
- Displays 144Hz as red, italicized text with a glow effect.
- Positions overlay near bottom-right (configurable in script).
- Minimal dependencies (uses Tkinter and Python stdlib).

## 📁 Included Files
### Core Files
- **`hz_overlay.py`** — primary overlay script  
- **`README.md`** — project documentation  
- **`LICENSE`** — MIT license  
- **`RELEASE.md`** — suggested GitHub release notes  
- **`BUILD_EXE.md`** — instructions for building a standalone EXE with PyInstaller
- **`Stay_Overlay.py`** Does not dissapear is **very plain**
  
### Helper Tools
- **`Start_Hz_Overlay.bat`** — launches the overlay  
- **`Start_Hz_Overlay - Shortcut.lnk`** — Windows shortcut for easy autostart  
- **`ToggleHZ.ahk`** — AutoHotkey script for toggling 120 Hz ↔ 144 Hz  
- **`ToggleHZ.bat`** — Batch version of the refresh-rate toggle
- **`Stay_Overlay.py`** - Alaways on overlay plain and transparent. 
- **`Toggle2k.exe`** — instantly switches monitor between 1080p/2K1440p
- **`Toggle2k16.exe`** — instantly switches monitor between 1200p/2K1600p
### Media  
- **`Screenshot_Transparent144hz.png`** - super simple overlay
- **`Screenshot.png`** — still image of the overlay in action  
- **`hz_overlay_in_action.mov`** — short demonstration video
## Resolution toggles Preview

Preview of the QHD <-> FHD toggles

<img src="icon 1.ico" width="100">  <img src="icon 2.ico" width="100">


## Usage
1. Ensure Python 3.8+ is installed on Windows.
2. Run with console: `python hz_overlay.py --alpha 0.3`  
   Or run without console: click the file
3. Click Stay_Overlay.py - Alaways on overlay plain and transparent.
4. Install Qres for AHK, Install Auto Hot Key
5. Add Start_Hz_Overlay - Shortcut.lnk to shell:startup (set run to minizmized in properties) 
6. Add ToggleHZ.ahk.ahk to shell:startup for easy CTRL + ALT + H  hertz toggle or set to custom
7. Optional: Toggle between QHD & FHD with Toggle2k.exe  Toggle2k16.exe veriants

   
## Why this exists
Many monitors switch between 120 Hz (10-bit) and 144 Hz (8-bit), 
but Windows provides no quick visual indicator.  
This overlay gives an instant, automatic notification whenever 
your refresh rate changes.

## Building an EXE
See included `BUILD_EXE.md` in the original release for PyInstaller guidance.
**some exes included**
   
---


## Credits

Created by **24xscv564w-bit (K.P.)**, 2025  
Part of the **hz_overlay** project ecosystem.

---

## License

MIT License — free for personal + commercial use.

---


![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-00adef)
![Downloads](https://img.shields.io/github/downloads/24xscv564w-bit/hz-overlay/total?color=blue)
