# Python Auto-Clicker

A Python learning project with terminal and desktop GUI interfaces.

## Features

- Validated click count and delay
- Five-second startup countdown
- GUI Start and Stop buttons
- PyAutoGUI corner fail-safe
- Cancellation when the GUI closes

## Requirements

- Python 3.10 or newer
- PyAutoGUI
- Tkinter available in your Python installation

Developed and manually tested on Windows.

## Installation

From the project folder:

```powershell
python -m pip install -r requirements.txt
```

## Run

Terminal version:

```powershell
python auto_clicker.py
```

GUI version:

```powershell
python auto_clicker_gui.py
```

Enter a positive whole number for the click count and a positive,
finite number for the delay in seconds.

The GUI accepts delays up to 3600 seconds. It rounds the scheduled
wait to milliseconds, with a minimum of 1 millisecond. Actual time
between clicks also includes PyAutoGUI's processing time.

Press Start, then move the cursor into position during the countdown.
Clicks occur wherever the cursor is located.

## Stop a run

In the GUI, press Stop to cancel the countdown or remaining clicks.
Closing the GUI also cancels pending actions.

In either version, move the cursor to a corner of the primary screen
and hold it there. PyAutoGUI checks its fail-safe before the next click.

## Learning goals

Functions, input validation, exception handling, GUI callbacks,
variable scope, and scheduling with Tkinter's after() method.