'''
Docstring for main.py
* this is the main entry point for the application
* it will initialize the application and start the main loop
* input and output will be handled here
* input '\\q' for stopping the application
'''

# public imports

# private imports
from pipeline import pipeline


# main loop

while True:
    user_input = input("🎯Input: ")
    
    if user_input == "\\q":
        print("Exiting the application. Goodbye!")
        break

    result = pipeline(user_input)
    print(f"▶ Output: {result}")