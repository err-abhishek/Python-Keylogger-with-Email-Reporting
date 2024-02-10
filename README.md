# Python Keylogger with Email Reporting

This Python script serves as a keylogger capable of monitoring keyboard input and sending encrypted email reports of logged keystrokes at regular intervals.

## Features

- **Keylogging:** Captures both alphanumeric and special keys pressed by the user.
- **Email Reporting:** Sends periodic email reports of logged keystrokes to a specified email address.
- **Configurability:** Offers customizable options such as log file format, logging intervals, and targeted keystroke monitoring.

## Requirements

- Python 3.x
- pynput library (`pip install pynput`)

## Usage

1. Replace placeholders in the script with your email address and password.
2. Run the script.
3. Press `Esc` key to stop the keylogger.

## Configuration

- `interval`: Interval in seconds for sending email reports (default is 60 seconds).
- `to_email`: Email address to which reports will be sent.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or raise issues for any suggestions or bug fixes.

