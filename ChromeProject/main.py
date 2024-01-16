from selenium import webdriver
import functions as f

arr_of_command = [
    "tag_name",
    "name",
    "class_name",
    "id",
    "xpath",
    "css_selector",
    "link_text",
    "partial_link_text"]

if __name__ == '__main__':


    URL = "http://www.google.com"
    num = int(input("Enter the number of webdrivers you want to open: "))
    list_of_drivers = f.openDrivers(num)

    s = f.getSizeOfWindows(1920,1080,num)
    f.orgenizeWindows(list_of_drivers, s[0], s[1], 1920, 1080)

    f.setURLtoAllDrivers(list_of_drivers, URL)

    # kind = input("Enter type of element: ")
    # name = input("Enter name of element: ")
    # text = input("Enter text to the element: ")

    # f.driverClickButton(list_of_drivers, kind, name)
    #
    # f.driverTypeText(list_of_drivers, text)
    #
    # key = input("Enter key to be pressed: ")
    #
    # f.driverPressKey(list_of_drivers, key)
    #
    # input("Press anything to quit drivers")
    input("Press any key to quit..")
    f.closeAllDrivers(list_of_drivers)
