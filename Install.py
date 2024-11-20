# Quick Sheridan sign-in
# Created by (a very frustrated) Sheridan student


# ========== SETUP ========== #
#
#   1. Edit the code to set up your passwords correctly - mine will be different from yours
#   2. Edit your emails in the file
#   3. Set whether you use 2FA and which email you use for Visual Studio (TODO: Allow for no email)
#   4. Save the zip someone like onedrive or google drive where you can access it quickly
#

# ========== HOW TO USE ========== #
#
#   1. Set Google Chrome as the default browser (TODO: set it automatically later?)
#   2. Use run.bat to run the program
#   3. Input your passwords as asked (TODO: Encrypted password bank/file from ToboPasswords?)
#   4. Input 2FA codes as asked
#


import time
import pyautogui as pg


using2FA = True

slateEmail = ""
githubEmail = ""
visualStudioEmail = ""
useSheridanEmailForVisualStudio = False # I use my personal email for Visual Studio
unityEmail = ""
miroEmail = ""

miroPass = #
slatePass = #
githubPass = #
visualStudioPass = #
unityPass = #





time.sleep(0.1)

def type(comm, delay = 0):
    pg.write(comm)
    time.sleep(delay)

def press(key, delay = 0):
    pg.write([key])
    time.sleep(delay)

def openProgram(program, delay):
    press("winleft", 0.5)
    type(program, 0.5)
    press("enter", delay)

def tab(count = 1):
    for i in range(count):
        press("tab", 0.1)

def enter(delay):
    press("enter", delay)

def tabEnter(count, delay):
    tab(count)
    enter(delay)

def typeEnter(command, delay):
    type(command, 0.1)
    enter(delay)


def waitFor2FA(program):
    if using2FA:
        print("Input 2FA for " + program + ". Press 'Enter' to continue.")
        input()


# ========== Github Desktop Download ========== #
openProgram("chrome", 2.0)
typeEnter("https://central.github.com/deployments/desktop/desktop/latest/win32", 1.0)
#enter(1.0) # Confirm download
time.sleep(3.5) # These PCs are fast, take about a second to download

pg.hotkey("winleft", "r") # Open Run dialog
typeEnter("downloads", 1.0)
press("right", 0.2) # Highlight file
enter(1.0) # Start setup

pg.hotkey("ctrl", "w") # Close Explorer
time.sleep(0.5)
pg.hotkey("ctrl", "w") # Close Chrome

print("Giving Github Desktop time to open...")
time.sleep(10)
enter(1.5) # Open login


# ========== Github Sign-in ========== #
type(githubEmail, 0.5)
tab()
typeEnter(githubPass, 0.5)

# Wait for 2FA...


# ========== SLATE Sign-in ========== #
pg.hotkey("ctrl", "t") # New tab
time.sleep(0.5)
typeEnter("slate.sheridancollege.ca", 1.0)
tabEnter(2, 2.0) # Navigate to "Sign In"

typeEnter(slateEmail, 1.5) # Email
typeEnter(slatePass, 1.0) # Pass

# Wait for 2FA...


# ========== Visual Studio Sign In ========== #
"""
openProgram("visual studio 2022", 7.0)
tabEnter(2, 2.0) # Sign into account

if not useSheridanEmailForVisualStudio:
    tabEnter(1, 2.5) # Seperate email (not organization)
    typeEnter(visualStudioEmail, 1.0)
    typeEnter(visualStudioPass, 1.0)

# Wait for 2FA...
#waitFor2FA("Sheridan Email" if useSheridanEmailForVisualStudio else "Microsoft Account")
"""

# ========== Unity Hub Sign In ========== #
"""
openProgram("unity hub", 5.0)
tabEnter(1, 3.0) # Login
tabEnter(3, 0.3) # Close cookies window
tab(7) # Navigate to username input

type(unityEmail, 0.5)
tab()
type(unityPass, 0.5)
tabEnter(3, 2.5) # Login button
tabEnter(2, 1.0) # Redirect to hub
"""

# ========== Miro Sign In ========== #
openProgram("chrome", 2.0)
typeEnter("miro.com/login", 5.0) # Go to webpage, wait for cookie popup
tabEnter(2, 1.0)
tab(12) # Navigate back to email field

type(miroEmail, 0.5)
tab()
typeEnter(miroPass, 0.5)
