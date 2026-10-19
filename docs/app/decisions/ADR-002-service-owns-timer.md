# ADR-002 — The timer service owns the running session; UI and notification are remotes

**Date:** 2026-10-12 **Status:** accepted

## Context
The confirmed behavior says the timer **keeps running when the app is swiped out of
Recents**, and the Session notification can pause and resume it. On Android, code
that runs while the app isn't open has to live in a service. python-for-android
says services are the way to run code when the app isn't open, that they run in a
**separate process**, and suggests OSC as a lightweight way for the app and service
to communicate.
Source: https://python-for-android.readthedocs.io/en/latest/services.html

## Options considered
1. **The service owns the timer state.** The Kivy UI and the notification's
   Pause/Resume button send commands (start, pause, resume, reset, settings changed)
   to the service. The service sends state back for display.
2. **The UI owns the timer; the service only shows a notification.** Simpler at
   first, but the timer stops when the app is closed, which breaks a confirmed
   requirement.

## Decision
Option 1. There is a single source of truth for the session, and it lives in the
service.

## Consequences
- Two processes have to talk to each other: this is inter-process communication
  (IPC), done over OSC (see [tech/osc-ipc.md](../tech/osc-ipc.md)).
- The UI must handle "I just opened, what's the current state?" by asking the
  service rather than assuming.
- The timer core (pure Python, US-001–003) is reused unchanged inside the
  service. That's why it must not import Kivy or Android code.
- On desktop (US-004–007) the UI runs the core directly. US-010 moves it into the
  service.
- On Android 14+, `:foreground` services need a `foregroundServiceType` (p4a docs).
  `specialUse` fits a timer (Android FGS types page) but needs a justification that
  Google Play reviews. That's fine for sideloading; revisit before publishing.
  Source: https://developer.android.com/develop/background-work/services/fgs/service-types
