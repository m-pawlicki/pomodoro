# Glossary

The shared vocabulary for this app — used in stories, docs, and conversation.
Entries are in the order they were discovered, not alphabetical.

## Session
One full run from Start until "Session complete" or Reset.
Distinct from: Interval (a single timed block inside a session).

## Interval
One timed block of a given type: work interval, short break, or long break.

## Work interval / Short break / Long break
The three interval types. A short break follows each work interval except the last; a single long break follows the Nth (last) work interval and then the session ends.

## Repetitions (N)
The number of work intervals in a session.

## Interval plan
The ordered list of intervals a session will run, derived from the settings when each interval starts.

## Auto-advance
When an interval ends, the alarm fires and the next interval starts without the user tapping anything.

## Reset
Returns the session to work interval 1 at full time, stopped.
Distinct from: Pause (keeps your place and remaining time).

## Alarm mode
The user's choice of how an interval end is announced — one of the bundled sounds, vibrate-only, or silent. The phone's ringer mode / Do Not Disturb can further quiet it.

## Session notification
The persistent Android notification shown only while a session is active (running or paused), showing interval type, remaining time, progress, and a Pause/Resume button.

## Foreground service
An Android background component that keeps running (with a visible notification) even when the app is closed; here it owns the running timer. See [tech/python-for-android-services.md](tech/python-for-android-services.md).

## End time
The moment the current interval is due to finish; remaining time is always calculated from it rather than counted down tick by tick.
Distinct from: Remaining time (derived, not stored while running).
