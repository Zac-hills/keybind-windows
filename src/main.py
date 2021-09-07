import keyboard as kb
import win32gui 
import win32con
import win32process
import json
import win32com.client
import pythoncom
# globals
KEY_BINDS="key_binds"
KEY_PROP="keys"
PID_PROP="pid"
# active_window_pid gets process id of current focuses window
def active_window_pid() -> int:
    window = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(window)
    return pid 
# has_parent checks if the window handle passed in is the top most window handle
def has_parent(hwnd: int) -> bool:
    return win32gui.GetWindow(hwnd, win32con.GW_OWNER) != 0
# get_window_handle enumerates through every open window and matches the window by process id can return None
def get_window_handle(pid: int) -> int:
    window_handle = []
    def win_enum_handler(hwnd, _):
        _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == window_pid and not has_parent(hwnd):
            window_handle.append(hwnd)
        return 
    win32gui.EnumWindows(win_enum_handler, None)
    if len(window_handle) == 0:
        return None
    return window_handle[0]
# set_window_focus moves window into focus by window handle
def set_window_focus(pid: int, hwnd: int) -> None:
    if pid == active_window_pid():
        return
    # initialize commands required due to the keyboard library threading    
    pythoncom.CoInitialize()
    # basically alt tabbing
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    # setting window as the selected alt tab
    win32gui.SetForegroundWindow(hwnd)
    return

def main()-> None:
    with open('config.json') as config_file:
        config = json.load(config_file)
        key_bind_list = config[KEY_BINDS]
        for i in range(0, len(key_bind_list)):
            pid = int(key_bind_list[i][PID_PROP])
            temp_hwnd = get_window_handle(pid)
            if temp_hwnd == None:
                return
            kb.add_hotkey(key_bind_list[i][KEY_PROP], set_window_focus, [pid, temp_hwnd])
        kb.wait()
    return

main()