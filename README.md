# hz-overlay
Lightweight Windows overlay to indicate monitor refresh rate changes (120Hz/144Hz) and bit-depth hints.

## Features
- Detects display refresh rate using Win32 API.
- Displays 120Hz as an animated rainbow text with a subtle nudge animation.
- Displays 144Hz as red, italicized text with a glow effect.
- Positions overlay near bottom-right (configurable in script).
- Minimal dependencies (uses Tkinter and Python stdlib).

👉 **[Download Latest Release](https://github.com/24xscv564w-bit/hz-overlay/releases/latest)**  

## 📁 Included Files
### Core Files
- **`hz_overlay.py`** — primary overlay script (scrubbed for release)  
- **`README.md`** — project documentation  
- **`LICENSE`** — MIT license  
- **`RELEASE.md`** — suggested GitHub release notes  
- **`BUILD_EXE.md`** — instructions for building a standalone EXE with PyInstaller  
### Helper Tools
- **`Start_Hz_Overlay.bat`** — launches the overlay  
- **`Start_Hz_Overlay - Shortcut.lnk`** — Windows shortcut for easy autostart  
- **`ToggleHZ.ahk`** — AutoHotkey script for toggling 120 Hz ↔ 144 Hz  
- **`ToggleHZ.bat`** — Batch version of the refresh-rate toggle
- **`Toggle2k.exe`** — instantly switches monitor to 2560×1440 (2K1440p)
- **`Toggle2k16.exe`** — instantly switches monitor to 2560×1600 (2K1600p)
### Media
- **`Screenshot.png`** — still image of the overlay in action  
- **`hz_overlay_in_action.mov`** — short demonstration video  
## Preview
Example of 144Hz detection (bottom-right overlay)

![Overlay Screenshot](Screenshot_144.png)

## 🖼 Icon previews

Preview of the 2K resolution toggle icons included in the release.

<p align="center">
  <img src="assets/icons/2k1600.png" alt="2K1600 toggle icon preview" width="256" height="256" style="border-radius:12px; margin-right:20px;" />
  <img src="assets/icons/2k1440.png" alt="2K1440 toggle icon preview" width="256" height="256" style="border-radius:12px;" />
</p>

<p align="center">
  <strong>2K1600</strong> — `Toggle2k16.exe` &nbsp;&nbsp; | &nbsp;&nbsp; <strong>2K1440</strong> — `Toggle2k.exe`
</p>
## Usage
1. Ensure Python 3.8+ is installed on Windows.
2. Run with console: `python hz_overlay.py --alpha 0.3`  
   Or run without console: `pythonw hz_overlay.py`
3. Add Start_Hz_Overlay - Shortcut.lnk to shell:startup (set run to minizmized in properties) 
4. Add ToggleHZ.ahk.ahk to shell:startup for easy CTRL + ALT + H  hertz toggle or set to custom
5. Optional: Use
Toggle2k.exe → switch to 2560×1440/1920x1080
Toggle2k16.exe → switch to 2560×1600/1920x1200
   
## Why this exists
Many monitors switch between 120 Hz (10-bit) and 144 Hz (8-bit), 
but Windows provides no quick visual indicator.  
This overlay gives an instant, automatic notification whenever 
your refresh rate changes.

## Building an EXE
See included `BUILD_EXE.md` in the original release for PyInstaller guidance.

## License
MIT

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-00adef)
![Downloads](https://img.shields.io/github/downloads/24xscv564w-bit/hz-overlay/total?color=blue)
