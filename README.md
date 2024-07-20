# Automation Script

This Python script automates a series of actions using the `pyautogui`and `pyperclip` libraries. It clicks on a specific coordinate, drags and copies data, and interacts with the Gemini AI for processing and pasting responses.

## Requirements

- Python 3.x
- `pyautogui` library
- `pyperclip` library

## Installation

1. Install the required libraries using pip:

```bash
pip install pyautogui pyperclip
```

And import gemini_ai file

## Usage

1. Run the script:

```bash
python ChatBot.py
```

2. The script performs the following actions:
   - Clicks on a specified coordinate.
   - Drags and copies data from a defined area.
   - Processes the copied data using Gemini AI Api.
   - Pastes and sends the processed data.

## Script Details

- **Constants:**
  - `BREVE_CLICK_COORDS`: Coordinates to click the Breve button.
  - `DRAG_START_COORDS`: Starting coordinates for dragging.
  - `DRAG_END_COORDS`: Ending coordinates for dragging.

- **Functions:**
  - `run()`: Performs the dragging, copying, and returns the copied data.
  - `Function_call(new_data,name)`: Processes the copied data and interacts with Gemini AI Api to paste and send responses.

- **Main Loop:**
  - Continuously checks the current time.
  - Calls `run()` to perform actions.
  - Calls `Function_call()` to process and handle data.
  - Stops the script at the specified `CHECK_HOUR` and `CHECK_MINUTE`.

## Note
Ensure that the `gemini_ai_api` file is correctly set up and that you have the Gemini Ai Api Key for the automated actions performed by `pyautogui`.
To test the script, you can adjust the constants for your specific coordinates and times. The script will automate the defined actions based on your input.
