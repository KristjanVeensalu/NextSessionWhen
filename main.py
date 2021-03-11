import functions as fc
import time
#Software check, install.
fc.install("requests")
fc.install("selenium")
fc.install("pynput")
fc.install("keyboard")

#Import dependancies
import requests
import keyboard
from selenium import webdriver
from requests.auth import HTTPBasicAuth 
from selenium.webdriver.common.keys import Keys

wordsToDetect = ['Millal session?','next session when','millal sess?','session when?']
running = True

username = str(input("Messenger username? - "))
password = str(input("Messenger password? - "))

driver = fc.login(username,password)

#keyboard.press_and_release("enter")

print(type(driver.page_source))
time.sleep(5)
textAlreadyRespondedto = []
incomingMessages = driver.find_elements_by_class_name("oo9gr5id")
outgoingMessages = driver.find_elements_by_class_name("ljqsnud1")


while running:
    incomingMessages = driver.find_elements_by_class_name("oo9gr5id")
    outgoingMessages = driver.find_elements_by_class_name("ljqsnud1")
    latestOutMessage = outgoingMessages[-1].get_attribute('innerText')
    latestInMessage = incomingMessages[-1].get_attribute('innerText')
    for x in wordsToDetect:
        if x in latestInMessage or x in latestOutMessage: 
            keyboard.write("Järgmine reede on plaanis")
            keyboard.press_and_release("enter")
            time.sleep(2)
    time.sleep(10)


'''
    for x in wordsToDetect:
        try:
            if className not in elementsAlreadyResponded:
                elementsAlreadyResponded.append(className)
                print(elementsAlreadyResponded)
                if x == 'Millal session?':
                        keyboard.write("Found '" + x + "' in chat.")
                        keyboard.press_and_release("enter")
                        keyboard.write("Järgmine reede on plaanis")
                        keyboard.press_and_release("enter")
                        time.sleep(20)
        except:
            #keyboard.write("Found '" + x + "' in chat.")
            #keyboard.press_and_release("enter")
            print("Listening for text")
            time.sleep(10)'''