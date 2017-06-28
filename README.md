This repository was created to reproduce this issue: https://github.com/appium/appium/issues/8573
## Installation
Create a virtual environment with python 3.6

Run `pip install -r requirements.txt`

Make sure to have an iOS simulator created `iPhone 7` iOS `10.3`

Run Appium Server 1.6.5

Run `python3 textfield_test.py`

The test will run up to 100 times trying to set up a text in the input box.
It will break into the debugger when the text retrieved after the `send_keys` action does not match.

