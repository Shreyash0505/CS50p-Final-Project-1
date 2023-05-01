# Intellibot.AI
#### Video Demo:  <https://youtu.be/qQcWXTHR1dA>

## __Definition__
 This is a virtual assistant inspired by the character JARVIS from the Marvel movie Iron Man. It is a high-level virtual assistant designed to perform various tasks using voice commands. The assistant has functionalities such as retrieving information from Wikipedia, opening websites, playing music, sending messages on WhatsApp, taking screenshots, managing tasks, telling jokes, and more.

 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

## __Libraries__

pyttsx3 : for text-to-speech conversion... [(Readmore)](https://www.geeksforgeeks.org/python-text-to-speech-by-using-pyttsx3/)

speech_recognition : for speech recognition and processing voice commands..[(Readmore)](https://pypi.org/project/SpeechRecognition/)

datetime : for getting the current date and time.. [(Readmore)](https://docs.python.org/3/library/datetime.html)

webbrowser : for opening websites.. [(Readmore)](https://docs.python.org/3/library/webbrowser.html)

os : for interacting with the operating system, e.g., playing music, opening applications, etc.. [(Readmore)](https://docs.python.org/3/library/os.html)

wikipedia : to extract information form wikipedia.. [(Readmore)](https://pypi.org/project/wikipedia/)

pywhatkit : The pywhatkit library allows you to send individual Whatsapp messages, send messages to groups, and even send images - all from Python.. [(Readmore)](https://pypi.org/project/pywhatkit/)

pyautogui : PyAutoGUI is a cross-platform GUI automation Python module for taking screenshots and managing tasks..[(Readmore)](https://pypi.org/project/PyAutoGUI/#:~:text=PyAutoGUI%20is%20a%20cross%2Dplatform,https%3A%2F%2Fpyautogui.readthedocs.org)

## **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

## __Functioning__

the project.py contains 9 functions including the main function.

### __Main()__ function:
The main() function is the main entry point of the program, which serves as the starting point for the virtual assistant's execution. It contains a loop that keeps running until the program is terminated. Inside the loop, it listens for voice commands from the user using the "take_command()" function. It is used to perform actions based on the user commeand such as search on wikipedia, tell todays date and time, greet, open certain web pages or youtube, open certain applications, etc. The function uses conditional statements (if, elif, else) to determine what action to take based on the voice command given by the user.

### __Today_date()__ function:
It is a function used to tell today date. When this function is called, it will return the current date as a string in the format "YYYY-MM-DD".

### __Wikipedia()__ function:
In this code, this function is uses Wikipedia API to search for and retrieve information from Wikipedia pages based on a user's query.

### __Wishme__() function :
the wishme() function is a custom function that doesn't take any arguments. The purpose of this function is to wish the user based on the current time.

### __Take_command()__ function:
The take_command() function is a custom function defined in a program, which is designed to take input from the user in the form of speech or text and return the user's command as a string.

### __Speak()__ function:
The speak() function takes a string as an argument and converts it to speech using pyttsx3. This function is used in the code to make the assistant speak responses to the user.

#### Also there are 3 more functions, get_github(to open github), get_chrome(to open chrome app), joke(to crack a random joke)

### Author : Shreyash S. Patil.
