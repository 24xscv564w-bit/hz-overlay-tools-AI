BUILD_EXE.md
============
1. Install PyInstaller: `pip install pyinstaller`
2. From the repository root run:
   `pyinstaller --noconsole --onefile --add-data "hz_overlay.py;." hz_overlay.py`
3. The exe will appear in `dist/`.
