# US-004 — Desktop main screen

**Status:** ready
**Depends on:** US-003
**Learner practices:** Kivy App and widgets; KV language; Kivy properties; Clock for refreshing the display

## Story
As a Pomodoro user, I want one screen that shows what interval I'm in and how long is
left, with big Start/Pause/Reset buttons, so that I can control my session at a glance.

## Why this matters
This is the first time you'll see the app. It also forces a clean boundary: the
screen only *displays* what the core says and *sends* actions to it. Keeping it that
way makes US-010 (moving the timer into a service) a swap, not a rewrite.

## Acceptance criteria
1. **Given** the app launches **When** nothing has been tapped **Then** the screen
   shows "Work", the full work length as mm:ss (e.g. 25:00), "Work 1 of 4", and a
   Start button.
2. **Given** a stopped or paused session **When** Start/Resume is tapped **Then** the
   countdown runs and updates at least once per second.
3. **Given** a running session **When** Pause is tapped **Then** the countdown stops,
   and the same button now offers Resume.
4. **Given** any state **When** Reset is tapped **Then** the screen returns to the
   launch state in criterion 1.
5. **Given** an interval ends **When** auto-advance happens **Then** the interval type
   and progress label update (e.g. "Short break", "Work 2 of 4").
6. **Given** the long break ends **When** the session completes **Then** the screen
   shows "Session complete" and offers Start for a new session.
7. **Given** the window is left running for a full interval **When** compared with a
   stopwatch **Then** the displayed time is within 1 second of real time.

## Out of scope
- Settings screen (US-005), sounds (US-007), Android (US-008+).
- Looking good. Simple and readable is enough.

## Mentor notes
- **Concepts to understand first:** Kivy `App`/`build()`, the KV language, and
  Kivy properties (they update the UI automatically when they change), all in
  [tech/kivy.md](../tech/kivy.md). `Clock.schedule_interval` is *only* for refreshing
  the display (ADR-003).
- **Approach options to consider:**
  - Layout in a `.kv` file vs. building widgets in Python. KV keeps layout apart
    from logic. What would you have to change in each case to move a button?
  - Where the core object lives: on the App, or on the root widget. Who else will
    need to reach it later (settings screen, alarm)?
  - One toggle button for Start/Pause/Resume, or separate buttons. Which is
    "easier", the word from the requirements?
- **Common pitfalls:** decrementing the display yourself instead of asking the core;
  mm:ss formatting at 0 and at 60 seconds; logic creeping into the KV file.
- **Questions to ask yourself before coding:**
  - What is the *only* information the screen needs from the core? List it.
  - If you deleted the UI file, would your pytest tests still pass?

## References
- Tech guides: [tech/kivy.md](../tech/kivy.md)
- Related: US-003, ADR-003, ADR-004
- Official docs: https://kivy.org/doc/stable/guide/basic.html — creating an app;
  https://kivy.org/doc/stable/guide/lang.html — KV language, `root`/`app`/`self`;
  https://kivy.org/doc/stable/api-kivy.clock.html — `schedule_interval`, accuracy.

## Definition of done
- [ ] Every acceptance criterion verified by hand
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
