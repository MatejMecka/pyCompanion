
import speech_recognition as sr
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print("I think you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    os.system("espeak 'I couldn't understand what you said, say it again please")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

words = r.recognize_google(audio).split()
print (words)

searchText = ' '.join(words[1:])
print (searchText)

if (words[0] == "YouTube"):

        os.system("espeak 'Opening youtube, standby'")


        driver = webdriver.Firefox()
        driver.set_window_size(800, 500)
        driver.set_window_position(50,50)

        driver.get('https://youtube.com')

        # wait for the search field to be loaded
     

        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "masthead-search-term"))
        )
        print('Successfully loaded search form')
 
        searchCmd = driver.find_element_by_id("masthead-search-term")

        searchCmd.send_keys(searchText)

        driver.find_element_by_id('search-btn').click()

        os.system("espeak 'There you go, have fun'")

if (words[0] == "Facebook"):

        os.system("espeak 'Logging you on Facebook, standby'")

        driver = webdriver.Firefox()
        driver.set_window_size(800, 500)
        driver.set_window_position(50,50)

        driver.get('https://facebook.com')

        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        print('Successfully loaded email form')
        
        ##### email and pass for Facebook #### 

        myEmail = "youremail"
        myPassword = "yourpass"

        ######################################

        emailCmd = driver.find_element_by_id("email")
        passCmd = driver.find_element_by_id("pass")


        emailCmd.send_keys(myEmail)
        passCmd.send_keys(myPassword)

        driver.find_element_by_id('u_0_n').click()

        os.system("espeak 'There you go, have fun'")


if (words[0] == "Google"):

        os.system("espeak 'Going to make a search on Google, standby'")


        driver = webdriver.Firefox()
        driver.set_window_size(800, 500)
        driver.set_window_position(50,50)

        driver.get('https://google.com')

        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "lst-ib"))
        )
        print('Successfully loaded search form')
 
        searchCmd = driver.find_element_by_id("lst-ib")

        searchCmd.send_keys(searchText)

        os.system("espeak 'There you go, have fun'")

       

else:
    print('Error')
    os.system("espeak 'Check your code!")