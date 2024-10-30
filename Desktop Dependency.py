import ctypes
from ctypes import wintypes
import win32gui
from PIL import Image

class FILEINFO(ctypes.Structure):
    _fields_ = [
        ("icon_handle", wintypes.HICON),
        ("icon_index", ctypes.c_int), 
        ('dwFileAttributes', wintypes.DWORD),
        ("szDisplayName", wintypes.CHAR * 260),
        ("szTypeName", wintypes.CHAR * 80)
    ]

SHGFI_ICON = 0x000000100
SHGFI_LARGEICON = 0x000000000
SHGFI_SMALLICON = 0x000000001

def get_file_icon(file_extension, large_icon=True):
    info = FILEINFO()
    # Create a unicode buffer for the file extension
    file_extension_w = ctypes.create_unicode_buffer(file_extension)

    result = ctypes.windll.shell32.SHGetFileInfoW(
        file_extension_w,
        0,
        ctypes.byref(info),
        ctypes.sizeof(info),
        SHGFI_ICON | (SHGFI_LARGEICON if large_icon else SHGFI_SMALLICON)
    )

    if result:
        
        icon_handle = info.icon_handle

        if icon_handle:
        
            icon_info = win32gui.GetIconInfo(icon_handle)
            bmp = win32gui.GetObject(icon_info[4])
    
    else:
    
        print(f"SHGetFileInfoW failed with error code: {ctypes.GetLastError()}")

icon = get_file_icon(r"C:\Users\Shreyas Nair\Desktop\Oct2024.rar", large_icon=True)
if icon:
    icon.show()
else:
    print("Icon not found.")
