# Keylogger

A simple Python-based keylogger that records all keystrokes into a `log.txt` file. Built using the `pynput` library, this tool listens to keyboard events and logs both regular and special keys.

> **Disclaimer**: This project is for educational purposes only. Do not use this tool without proper authorization. Unauthorized use may violate privacy laws and ethical standards.

---

## Project Structure

```
keylogger/
├── keylogger.py
├── log.txt
└── README.md
```

---

## Features

- Logs all keystrokes to `log.txt`.
- Handles special keys like Space, Enter, and Escape.
- Detects and prints both key presses and releases.
- Stops logging when the `Esc` key is pressed.

---

## Requirements

- Python 3.6 or later.
- Install required packages with:

```bash
pip install pynput
```

---

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/onyango-granton/keylogger.git
    cd keylogger
    ```

2. Run the script:

    ```bash
    python keylogger.py
    ```

3. Stop the logger:

    - Press the `Escape (Esc)` key to stop listening and close the program.

4. Check the output:

    - Open the `log.txt` file to view the recorded keys.

---

## How It Works

- **`on_press`**: Captures key presses, appends them to a list, and writes to `log.txt`.
- **`on_release`**: Stops the listener if `Esc` is released.
- **`pynput.Listener`**: Listens for both press and release events.
- Special keys (e.g., Space and Enter) are logged as `" "` and newline respectively.

---

## Sample Output (`log.txt`)

If you typed:

```
Hello world
```

Your `log.txt` would look like:

```
H e l l o   w o r l d
```

---

## Code Snippet

```python
if key == Key.space:
     f.write(" ")
elif key == Key.enter:
     f.write("\n")
else:
     f.write(str(key).replace("'", ""))
```

---

## Disclaimer

This software is intended for educational and authorized testing environments only. Unauthorized use is illegal and unethical.

---

## Author

**Granton Onyango**  
Passionate about Python, automation, and system-level scripting.
