from time import sleep

import pyautogui

from math import isfinite


def auto_click(click_count: int, delay_seconds: float) -> None:
    for _ in range(click_count):
        pyautogui.click()
        sleep(delay_seconds)


def prompt_click_count() -> int:
    while True:
        try:
            click_count = int(input("How many clicks? "))
        except ValueError:
            print("Enter a whole number.")
            continue

        if click_count >= 1:
            return click_count

        print("Click count must be at least 1.")


def prompt_delay_seconds() -> float:
    while True:
        try:
            delay_seconds = float(input("Seconds between clicks? "))
        except ValueError:
            print("Enter a number.")
            continue
        if isfinite(delay_seconds) and delay_seconds > 0:
            return delay_seconds

        print("Delay must be a finite number greater than 0.")


def main() -> None:
    click_count = prompt_click_count()
    delay_seconds = prompt_delay_seconds()

    print("Clicking starts in 5 seconds. Move your cursor into position.")
    sleep(5)

    try:
        auto_click(click_count=click_count, delay_seconds=delay_seconds)
    except pyautogui.FailSafeException:
        print("Clicking stopped by the corner fail-safe.")


if __name__ == "__main__":
    main()
