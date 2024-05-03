#     Reminder bot
# This is a Python script that uses the pyautogui library to automate typing and pressing keys

import pyautogui, time, datetime, keyboard  #This line imports the necessary Python libraries for this script The 'pyautogui'
# library is used to automate typing and pressing keys


time.sleep(5)   #This line causes the program to pause for 5 seconds

while True:  #This line starts an infinite loop. The code inside this loop will keep running until you manually stop the program.
    # to display the time at which the message is sent 
    print(datetime.datetime.now()) 
    pyautogui.typewrite("Reminder: Drink water!")  #This line uses pyautogui to type the string “Reminder: Drink water!”.
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        break  # finish the loop

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Take medicine!")  #This line uses pyautogui to type the string “Reminder: Take medicine!”.
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Take the dog for a walk!")   #This line uses pyautogui to type the string “Reminder: Drink water!”.
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Drink water!") 
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Drink water!") 
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  
    

quit
quit
quit
quit


