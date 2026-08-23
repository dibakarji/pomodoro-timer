#!/usr/bin/env python3
"""Terminal Pomodoro timer with progress bar and terminal bell alerts."""

import argparse
import sys
import time


def countdown(label: str, minutes: float, cycle: int | None = None):
    total_seconds = int(minutes * 60)
    prefix = f"Pomodoro #{cycle} - " if cycle is not None else ""
    width = 38

    for remaining in range(total_seconds, -1, -1):
        filled = int(width * (1 - remaining / max(total_seconds, 1)))
        bar = "#" * filled + "-" * (width - filled)
        mm, ss = divmod(remaining, 60)
        sys.stdout.write(f"\r{prefix}{label:<7} [{bar}] {mm:02d}:{ss:02d}")
        sys.stdout.flush()
        if remaining > 0:
            time.sleep(1)

    sys.stdout.write("\a\n")  # terminal bell
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description="Pomodoro focus timer")
    parser.add_argument("--work", type=float, default=25.0,
                        help="Work length in minutes (default: 25)")
    parser.add_argument("--break", dest="short_break", type=float, default=5.0,
                        help="Short break in minutes (default: 5)")
    parser.add_argument("--long-break", type=float, default=15.0,
                        help="Long break every 4 pomodoros (default: 15)")
    parser.add_argument("--cycles", type=int, default=4,
                        help="Number of pomodoros before stopping (default: 4)")
    parser.add_argument("--test", action="store_true",
                        help="Ultra-short durations to verify it works")
    args = parser.parse_args()

    if args.test:
        args.work = args.short_break = args.long_break = 0.05

    print(f"Plan: {args.cycles} x {args.work:g} min work "
          f"(breaks: {args.short_break:g} / long {args.long_break:g})")
    print("Press Ctrl+C to quit early.\n")

    try:
        for cycle in range(1, args.cycles + 1):
            countdown("WORK", args.work, cycle)

            if cycle == args.cycles:
                print(f"\nAll {args.cycles} pomodoros done. Great session!")
                break

            is_long = cycle % 4 == 0
            break_min = args.long_break if is_long else args.short_break
            print(f"\nTime's up! Take a {'LONG ' if is_long else ''}break "
                  f"({break_min:g} min).")
            countdown("BREAK", break_min)
            print("\nBreak over - back to work!\n")

    except KeyboardInterrupt:
        print("\nTimer stopped. See you next session!")


if __name__ == "__main__":
    main()
