import pyautogui, time, datetime, keyboard

time.sleep(5) 

while True: 
    # to display the time at which the message is sent 
    print(datetime.datetime.now()) 
    pyautogui.typewrite("Reminder: Drink water!") 
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('You Pressed A Key!')
        break  # finish the loop

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Take medicine!") 
    pyautogui.press("enter") 
    time.sleep(6) 

    if keyboard.is_pressed('q'):  
        print('You Pressed A Key!')
        break  

    print(datetime.datetime.now()) 

    pyautogui.typewrite("Reminder: Take the dog for a walk!") 
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


