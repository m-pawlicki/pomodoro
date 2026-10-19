# App Overview

## What this is

This is a personal Android Pomodoro timer, built in Python with Kivy, by a junior developer learning Kivy and Android along the way. It's for one user, on their own phone, with no accounts. It runs a classic Pomodoro session: work, then a short break, repeated N times, then a long break, then it stops. Each change is announced with an alarm, and the session keeps running with a live notification even when the app itself is swiped away. The point of the app is twofold: help someone focus in timed blocks with as few taps as possible, and teach the core Android ideas behind it, like background work, notifications, and audio.

## Major parts

The timer core is pure Python, with no Kivy or Android dependencies. It knows the interval plan, the current state (stopped, running, paused, or complete), and works out remaining time from a stored end time rather than counting down tick by tick. It's tested with pytest, and everything else in the app builds on top of it.

The app UI is the Kivy-based main screen, showing the interval type, the time as mm:ss, a label like "Work 2 of 4", and Start/Pause/Reset controls, plus a settings screen. On Android, this UI acts as a remote control for the timer service rather than running the timer itself.

The timer service is a python-for-android foreground service. It owns the running session so that the session survives the app being closed, and it talks to the UI over OSC messages (see decisions/ADR-002).

The session notification shows the service's current state and sends Pause/Resume actions back to it.

The alarm plays the chosen bundled sound, vibrates, or stays silent at each interval's end, depending on the alarm mode, and it follows the phone's ringer mode.

The settings store remembers interval lengths, the number of repetitions (N), and the alarm mode between launches. Changes made here apply starting from the next interval, not retroactively to the one in progress.
