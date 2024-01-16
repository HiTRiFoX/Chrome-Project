import math
from selenium import webdriver # To open the web driver
from selenium.webdriver.common.action_chains import ActionChains # to send keys without using elements
from selenium.webdriver.common.keys import Keys # To use the keys including "CONTROL", "SPACE".
from selenium.webdriver.common.by import By # To find elements by id or by anything else
from selenium.webdriver.support.ui import WebDriverWait # To wait until an element
from selenium.webdriver.support import expected_conditions as EC # To find an element

PATH = "D:\JetBrains\PycharmProjects\ChromeProject\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH) # this is the user's driver that he control

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

def openDrivers(num_of_drivers):
    """
    Gets a number of drivers to be opened and open that amount of drivers
    :param int num_of_drivers: number of driver to be opened
    :return list of hwnd of every driver
    """
    list_of_drivers = []
    for num in range(int(num_of_drivers)):
        driver.switch_to.new_window('window')
        list_of_drivers.append(driver.current_window_handle) # current_window_handle is the current window that opened

    return list_of_drivers

def closeAllDrivers(list_of_drivers):
    """
    Gets a list of drivers and close all the windows
    :param arr list_of_drivers: an array of drivers
    """
    for d in list_of_drivers:
        driver.switch_to.window(d)
        driver.close()

def setURLtoAllDrivers(list_of_drivers, url):
    """
    Gets a list of drivers and URL and set every URL to each driver
    :param arr list_of_drivers: an array of drivers
    :param string URL: specific site
    """
    for d in list_of_drivers:
        driver.switch_to.window(d)
        driver.get(url)

#TODO: Do description for all the functions. find a easy way to access to sites without type every time the id and name and what ever.
def driverClickButton(list_of_drivers, kind, name):
    for d in list_of_drivers:
        driver.switch_to.window(d)
        exec(f"driver.find_element_by_{kind}('{name}').click()")

def driverTypeText(list_of_drivers, text):
    for d in list_of_drivers:
        driver.switch_to.window(d)
        actions = ActionChains(driver)
        actions.send_keys(text)
        actions.perform()

def driverPressKey(list_of_drivers, key):
    for d in list_of_drivers:
        driver.switch_to.window(d)
        actions = ActionChains(driver)
        exec(f"actions.send_keys(Keys.{key})")
        actions.perform()


# this is from the tablet:

def getClickInWindow(mouse_x, mouse_y, win_x, win_y):
    """
    Gets the position of the mouse and the position of the windows
    and return the position of the click in the window.
    :param int mouse_x: X coordinte of the mouse
    :param int mouse_y: Y coordinte of the mouse
    :param int win_x: X coordinate of the window
    :param int win_y: Y coordinate of the window
    :return: array that contains the coordinates of the click in the window.
    """
    x = mouse_x + win_x
    y = mouse_y + win_y
    return [x, y]

def clickNewWindow(win_x, win_y, x, y):
    """
    Gets the position of the window, and the position in the window (delta)
    and return the position to be pressed in the new window
    :param int win_x: X coordinte of the window
    :param int win_y: Y coordinate of the window
    :param int x: The difference of window and click position by X coordinte
    :param int y: The difference of window and click position by Y coordinte
    :return: array that contains the coordinates of the position to be pressed
    """
    x = win_x + x
    y = win_y + y
    return [x, y]

def getSizeOfWindows(screen_x, screen_y, n):
    """
    Gets the size of the screen and the number of the windows
    and return the size of every window
    :param int screen_x: size of the screen by X coordinate
    :param int screen_y: size of the screen by Y coordinate
    :param int n: number of windows
    :return: the size that every window should be
    """
    n_x = 1
    n_y = 1
    x = screen_x
    y = screen_y
    for i in range(n):
        if math.log(n_x)/math.log(3) <= math.ceil(math.log(n_y)/math.log(3)):
            n_x += 1
            x = screen_x / n_x
        else:
            n_y += 1
            y = screen_y / n_y
    return [x, y]

def getWindowSize(lst): #TODO: tetaken oti o timhak
    """
    Get list of the hwnd and return the size of the first window
    :param lst:
    :return:
    """
    driver.switch_to_window(lst[0])
    return driver.get_window_size()

def orgenizeWindows(lst, size_x, size_y, screen_x, screen_y):
    """
    Gets list of hwnd and size to set for each window and the screen size
    :param lst: hwnd of every window
    :param int size_x: size to set for every window by X
    :param int size_y: size to set for every window by Y
    :param int screen_x: size of the screen by X
    :param int screen_y: size of the screen by Y
    """
    x = 0
    y = 0
    for d in lst:
        driver.switch_to.window(d)
        driver.set_window_size(size_x, size_y)
        driver.set_window_position(x, y)
        x += size_x
        if x >= screen_x:
            x = 0
            y += size_y


# //button[contains(string(), "חיפוש תמונות")]