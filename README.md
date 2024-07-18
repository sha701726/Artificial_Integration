# Automation Script

This Python script automates a series of actions using the `pyautogui`, `pyperclip`, and `gemini_ai` libraries. It clicks on a specific coordinate, drags and copies data, and interacts with the Gemini AI for processing and pasting responses.

## Requirements

- Python 3.x
- `gemini_ai` library
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
python chatBot.py
```

2. The script performs the following actions:
   - Clicks on a specified coordinate.
   - Drags and copies data from a defined area.
   - Processes the copied data using Gemini AI.
   - Pastes and sends the processed data.

## Script Details

- **Constants:**
  - `BREVE_CLICK_COORDS`: Coordinates to click the Breve button.
  - `DRAG_START_COORDS`: Starting coordinates for dragging.
  - `DRAG_END_COORDS`: Ending coordinates for dragging.
  - `CHECK_HOUR` and `CHECK_MINUTE`: Time to stop the script.

- **Functions:**
  - `run()`: Performs the dragging, copying, and returns the copied data.
  - `write_in_file(new_data)`: Processes the copied data and interacts with Gemini AI to paste and send responses.

- **Main Loop:**
  - Continuously checks the current time.
  - Calls `run()` to perform actions.
  - Calls `write_in_file()` to process and handle data.
  - Stops the script at the specified `CHECK_HOUR` and `CHECK_MINUTE`.

## Example

To test the script, you can adjust the constants for your specific coordinates and times. The script will automate the defined actions based on these settings.

## Note

Ensure that the `gemini_ai` library is correctly set up and that you have the necessary permissions for the automated actions performed by `pyautogui`.
