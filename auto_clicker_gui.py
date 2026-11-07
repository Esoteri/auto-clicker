import tkinter as tk
from tkinter import ttk
from math import isfinite
import pyautogui


def main() -> None:
    window = tk.Tk()
    window.title("Python Auto-Clicker")

    ttk.Label(window, text="Click count").pack(padx=16, pady=(12, 0))
    count_entry = ttk.Entry(window)
    count_entry.pack(padx=16)

    ttk.Label(window, text="Seconds between clicks").pack(padx=16, pady=(12, 0))
    delay_entry = ttk.Entry(window)
    delay_entry.pack(padx=16)

    countdown_job: str | None = None

    def finish_run(message: str) -> None:
        status.config(text=message)
        start_button.config(state="normal")
        stop_button.config(state="disabled")

    def click_once(clicks_left: int, delay_ms: int) -> None:
        nonlocal countdown_job
        countdown_job = None

        try:
            pyautogui.click()
        except pyautogui.FailSafeException:
            finish_run("Clicking stopped by the corner fail-safe.")
            return

        clicks_left -= 1
        if clicks_left == 0:
            finish_run("Clicks complete.")
            return

        status.config(text=f"Clicking... {clicks_left} remaining.")
        countdown_job = window.after(delay_ms, click_once, clicks_left, delay_ms)

    def countdown(seconds_left: int, click_count: int, delay_ms: int) -> None:
        nonlocal countdown_job

        if seconds_left == 0:
            click_once(click_count, delay_ms)
            return

        status.config(text=f"Starting in {seconds_left}...")
        countdown_job = window.after(
            1000, countdown, seconds_left - 1, click_count, delay_ms
        )

    def stop_countdown() -> None:
        nonlocal countdown_job

        if countdown_job is None:
            return

        window.after_cancel(countdown_job)
        countdown_job = None
        finish_run("Run cancelled.")

    def close_window() -> None:
        nonlocal countdown_job

        if countdown_job is not None:
            window.after_cancel(countdown_job)
            countdown_job = None

        window.destroy()

    def check_settings() -> None:
        errors = []

        try:
            click_count = int(count_entry.get())
        except ValueError:
            errors.append("Enter a whole number for click count.")
        else:
            if click_count < 1:
                errors.append("Click count must be at least 1.")

        try:
            delay_seconds = float(delay_entry.get())
        except ValueError:
            errors.append("Enter a number for the delay.")
        else:
            if not isfinite(delay_seconds) or delay_seconds <= 0:
                errors.append("Delay must be finite and greater than 0.")

        if errors:
            status.config(text="\n".join(errors))
            return

        if delay_seconds > 3600:
            status.config(text="Delay must be 3600 or less.")
            return

        delay_ms = max(1, round(delay_seconds * 1000))
        start_button.config(state="disabled")
        stop_button.config(state="normal")
        countdown(5, click_count, delay_ms)

    start_button = ttk.Button(window, text="Start", command=check_settings)
    start_button.pack(pady=12)
    stop_button = ttk.Button(
        window, text="Stop", command=stop_countdown, state="disabled"
    )
    stop_button.pack(pady=(0, 12))
    status = ttk.Label(window, text="Enter your click settings.")
    status.pack(padx=16, pady=(0, 12))

    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()


if __name__ == "__main__":
    main()
