# ADR-003 — Measure time from an End time, not by counting ticks

**Date:** 2026-10-12 **Status:** accepted

## Context
The countdown must be accurate over 25+ minutes, keep correct time while the phone
sleeps, and survive pausing and resuming. Kivy's Clock docs say scheduled callbacks
are approximate: frames don't land exactly on the interval, and `dt` can be under
or over the target.
Source: https://kivy.org/doc/stable/api-kivy.clock.html

## Options considered
1. **Store the End time.** When an interval starts or resumes, record when it
   should finish. Every display refresh calculates remaining time from the End time
   and the current time. Pausing keeps the remaining time; resuming sets a new End
   time.
2. **Decrement a counter on each tick.** Intuitive, but every late tick adds error,
   and missed ticks (device asleep, process paused) are lost.

## Decision
Option 1. Ticks only refresh the display; they never measure time.

## Consequences
- The timer core needs a source of "now". If tests can supply their own "now", they
  can check 25 minutes passing instantly (see US-002).
- Think about which clock to use. Python's docs say `time.time()` can go backwards
  if the system clock is set back, while `time.monotonic()` isn't affected by clock
  updates. A phone also **suspends** (deep sleep), and the docs describe
  `CLOCK_BOOTTIME` as like `CLOCK_MONOTONIC` "except it also includes any time
  that the system is suspended." Read
  https://docs.python.org/3/library/time.html (`time.monotonic`,
  `CLOCK_BOOTTIME`) and choose before US-002 (or at least before US-010).
- Good exercise: try option 2 in a scratch file and watch it drift.
