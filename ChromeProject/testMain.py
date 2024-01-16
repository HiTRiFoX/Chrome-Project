# # encoding: utf-8
# from __future__ import print_function
# from os import path
# from pywinauto import Desktop, Application
# import win32gui
# from pynput.mouse import Listener
# import pyautogui as ag
#
#
# hwnd_arr = []
# def getWindowCords(hwnd, extra):
#     """
#     returns the coordinates of window. (x,y)
#     """
#     if "כרטיסייה חדשה" in win32gui.GetWindowText(hwnd):
#         rect = win32gui.GetWindowRect(hwnd)
#         x = rect[0]
#         y = rect[1]
#         w = rect[2] - x
#         h = rect[3] - y
#         print("Window %s:" % win32gui.GetWindowText(hwnd))
#         print("\tLocation: (%d, %d)" % (x, y))
#         print("\t    Size: (%d, %d)" % (w, h))
#         hwnd_arr.append(hwnd)
#
# def getMouseCords(x, y, button, pressed):
#     t = getMouseCordsInWindow(ag.position()[0], ag.position()[1], pos_arr[1][0], pos_arr[1][1])
#     clickOnNewWindow(t[0], t[1])
#     pass
#
# def getMouseCordsInWindow(mouse_x, mouse_y, win_x, win_y):
#     new_win_x = mouse_x - win_x
#     new_win_y = mouse_y - win_y
#     return [new_win_x, new_win_y]
#
# def clickOnNewWindow(new_win_x, new_win_y):
#     ag.click(new_win_x, new_win_y)
#     return
#
# def getWindowsPos(hwnd_array):
#     pos_array = []
#     for hwnd in hwnd_array:
#         window_rect = win32gui.GetWindowRect(hwnd)
#         pos_array.append(window_rect)
#     return pos_array
#
#
#
# win32gui.EnumWindows(getWindowCords, None)
# print(hwnd_arr)
# pos_arr = getWindowsPos(hwnd_arr)
# print(pos_arr)
#
#
#
# with Listener(on_click=getMouseCords) as listener:
#     listener.join()
#
#
#
#
#
#
#
#
#
#
#
#
# """
# app = Application(backend='uia')
# app.start('notepad.exe')
# app = Application(backend='uia').connect(title='Untitled - Notepad')
# app.UntitledNotepad.print_control_identifiers()
# """
#
#
#
#
#
# """
# chrome_dir = r'"C://Program Files//Google//Chrome//Application//chrome.exe"'
# tab_log_in = u'Google (Incognito)' # tab name
# tab_drive = 'My Drive - Google Drive (Incognito)'
#
# command = '--force-renderer-accessibility --incognito --start-maximized'
# url = 'google.com'
#
# # # start google chrome
# chrome = Application(backend='uia') # can be changed to backend="win32"
# chrome.start(chrome_dir + " " + command + " " + url) # this is the template to run the chrome.
#
# # wait while a page is loading
# chrome[tab_log_in].child_window(title_re='Reload.*', control_type='Button').wait('visible', timeout=10)
# ch_window = chrome[tab_drive].child_window(title="Google Chrome", control_type="Custom")
#
# # log in
# chrome.window().type_keys('TestPywinauto{ENTER}')  # username
# chrome[tab_log_in].child_window(title="Google Chrome", control_type="Custom").\
#     child_window(title="Back", control_type="Image").wait(wait_for='visible', timeout=10)
#
# chrome.window().type_keys('testpywinauto123{ENTER}')  # password
# ch_window.child_window(title="Getting started PDF", control_type="ListItem").wait(wait_for='visible')
#
# # start explorer in the current path
# dir_path = path.join(path.dirname(path.realpath(__file__)), 'UIA_Drive')
# explorer = Application().start('explorer.exe ' + dir_path)
# Desktop(backend='uia').window(title='UIA_Drive', active_only=True).wait('visible', timeout=10)
# dlg = Application(backend='uia').connect(path='explorer.exe', title='UIA_Drive')
#
# # find file
# file = dlg.UIA_Drive.ItemsView.wrapper_object().get_item('test.zip')
#
# # drag n drop
# destination = chrome.top_window().wrapper_object()
# file.press_mouse_input(coords=file.rectangle().mid_point())
# file.move_mouse_input(coords=destination.rectangle().mid_point())
# chrome.top_window().set_focus()
# file.release_mouse_input(coords=destination.rectangle().mid_point())
#
# # wait upload file
# ch_window.child_window(title="test.zip Compressed Archive", control_type="ListItem").wait('visible')
#
# print('DONE')"""