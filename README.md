# hz-overlay
Lightweight Windows overlay to indicate monitor refresh rate changes (120Hz/144Hz) and bit-depth hints.

## Features
- Detects display refresh rate using Win32 API.
- Displays 120Hz as an animated rainbow text with a subtle nudge animation.
- Displays 144Hz as red, italicized text with a glow effect.
- Positions overlay near bottom-right (configurable in script).
- Minimal dependencies (uses Tkinter and Python stdlib).

## Files
- `hz_overlay.py` — main overlay script (scrubbed for release).
- `README.md` — this file.
- `LICENSE` — MIT license.
- `RELEASE.md` — suggested GitHub release notes.

## Usage
1. Ensure Python 3.8+ is installed on Windows.
2. Run with console: `python hz_overlay.py`  
   Or run without console: `pythonw hz_overlay.py`

## Building an EXE
See included `BUILD_EXE.md` in the original release for PyInstaller guidance.

## License
MIT
