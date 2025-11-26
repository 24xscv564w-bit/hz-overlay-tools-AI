# hz_overlay.py
# Overlay indicator for monitor refresh rate (120Hz/144Hz)
# Shows 120Hz as animated rainbow + nudge, 144Hz as red italic with glow.

import ctypes
from ctypes import wintypes, Structure, byref, c_wchar, c_ushort, c_ulong, c_short
import tkinter as tk
import threading
import time
import colorsys

class DEVMODEW(Structure):
    _fields_ = [
        ("dmDeviceName", c_wchar * 32),
        ("dmSpecVersion", c_ushort),
        ("dmDriverVersion", c_ushort),
        ("dmSize", c_ushort),
        ("dmDriverExtra", c_ushort),
        ("dmFields", c_ulong),
        ("dmOrientation", c_short),
        ("dmPaperSize", c_short),
        ("dmPaperLength", c_short),
        ("dmPaperWidth", c_short),
        ("dmScale", c_short),
        ("dmCopies", c_short),
        ("dmDefaultSource", c_short),
        ("dmPrintQuality", c_short),
        ("dmColor", c_short),
        ("dmDuplex", c_short),
        ("dmYResolution", c_short),
        ("dmTTOption", c_short),
        ("dmCollate", c_short),
        ("dmFormName", c_wchar * 32),
        ("dmLogPixels", c_ushort),
        ("dmBitsPerPel", c_ulong),
        ("dmPelsWidth", c_ulong),
        ("dmPelsHeight", c_ulong),
        ("dmDisplayFlags", c_ulong),
        ("dmDisplayFrequency", c_ulong),
    ]

user32 = ctypes.WinDLL('user32', use_last_error=True)
EnumDisplaySettingsW = user32.EnumDisplaySettingsW
EnumDisplaySettingsW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, ctypes.POINTER(DEVMODEW)]
EnumDisplaySettingsW.restype = wintypes.BOOL
ENUM_CURRENT_SETTINGS = -1

def read_display_mode():
    dm = DEVMODEW()
    dm.dmSize = ctypes.sizeof(DEVMODEW)
    ok = EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, byref(dm))
    if not ok:
        return None, None
    return int(dm.dmDisplayFrequency), int(dm.dmBitsPerPel)

def rainbow_hex(p):
    p = p % 1
    r,g,b = colorsys.hsv_to_rgb(p,1,1)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

def run_overlay():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    try: root.attributes("-alpha",0.85)
    except: pass

    TRANSPARENT="#123456"
    try:
        root.wm_attributes("-transparentcolor",TRANSPARENT)
        bg=TRANSPARENT
    except:
        bg="black"

    canvas = tk.Canvas(root,bg=bg,highlightthickness=0,bd=0)
    canvas.pack()

    font_size=20
    base_font=("Segoe UI",font_size,"bold")
    italic_font=("Segoe UI",font_size,"italic")

    padding=6
    root.update_idletasks()
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()

    def resize_and_place(text,font,glow=False):
        canvas.delete("measure")
        item=canvas.create_text(0,0,text=text,font=font,anchor="nw",tags=("measure",))
        canvas.update_idletasks()
        bbox=canvas.bbox(item)
        if bbox:
            w=bbox[2]-bbox[0]+padding*2
            h=bbox[3]-bbox[1]+padding*2
        else:
            w,h=100,30
        canvas.config(width=w,height=h)
        canvas.update_idletasks()
        x=sw-w
        y=sh-h-40  # up 40px now
        root.geometry(f"+{x}+{y}")

    rainbow_phase=0
    previous=None
    visible_until=0
    anim=False

    def nudge():
        nonlocal anim
        if anim: return
        anim=True
        seq=[0,-4,-8,-4,0]
        i=0
        def step():
            nonlocal i,anim
            if i>=len(seq):
                anim=False
                return
            dx=seq[i]
            canvas.update_idletasks()
            w=canvas.winfo_width()
            h=canvas.winfo_height()
            x=sw-w+dx
            y=sh-h-40
            root.geometry(f"+{x}+{y}")
            i+=1
            root.after(35,step)
        step()

    def draw(text,color,font,glow=False):
        resize_and_place(text,font,glow)
        canvas.delete("all")
        w=canvas.winfo_width()
        h=canvas.winfo_height()
        if glow:
            for ox,oy in [(-2,0),(2,0),(0,-2),(0,2),(-1,-1),(1,1)]:
                canvas.create_text(w-padding+ox,h-padding+oy,text=text,fill="#fff",font=font,anchor="se")
        canvas.create_text(w-padding,h-padding,text=text,fill=color,font=font,anchor="se")
        canvas.update_idletasks()

    import time
    def updater():
        nonlocal rainbow_phase,previous,visible_until
        while True:
            hz,_=read_display_mode()
            txt=f"{hz}Hz"
            if hz!=previous:
                previous=hz
                visible_until=time.time()+3
                if hz==120:
                    rainbow_phase=0
                    draw(txt,rainbow_hex(rainbow_phase),base_font,False)
                    root.deiconify()
                    root.after(0,nudge)
                elif hz==144:
                    draw(txt,"#ff0000",italic_font,True)
                    root.deiconify()
                else:
                    draw(txt,"#FFF9B1",base_font,False)
                    root.deiconify()

            if time.time()<visible_until:
                if hz==120:
                    rainbow_phase+=0.06
                    draw(txt,rainbow_hex(rainbow_phase),base_font,False)
                elif hz==144:
                    draw(txt,"#ff0000",italic_font,True)
                else:
                    draw(txt,"#FFF9B1",base_font,False)
            else:
                root.withdraw()
            time.sleep(0.1)

    import threading
    threading.Thread(target=updater,daemon=True).start()
    root.mainloop()

if __name__=="__main__":
    run_overlay()
