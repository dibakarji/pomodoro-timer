# Pomodoro Timer 🍅

A terminal Pomodoro timer: 25-minute focus sprints separated by short breaks, with progress bar and terminal bell.

## Features

- Customizable work/short-break/long-break durations
- Live countdown with ASCII progress bar
- Terminal bell (`\a`) when each phase ends
- Cycle counter after every completed pomodoro
- Pure standard library

## Usage

```bash
python pomodoro.py                       # classic 25/5/15
python pomodoro.py --work 50 --break 10  # deep-work variant
python pomodoro.py --cycles 6            # six pomodoros today
```

## Example

```
Pomodoro #1 - WORK (25 min)
[####################------------------] 12:34 remaining
\a
Time's up! Take a 5 min break.
```

## The Technique

1. Pick one task → work 25 minutes, no distractions
2. Short break (5 min)
3. Every 4th pomodoro → long break (15 min)
4. Repeat

---
Part of my **31 Python Projects** challenge - one small, genuine project at a time.
