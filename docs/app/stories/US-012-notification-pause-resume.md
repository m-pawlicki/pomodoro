# US-012 — Pause/Resume button in the notification

**Status:** blocked
**Depends on:** US-011
**Learner practices:** notification actions; PendingIntent; routing an Android event back into Python

## Story
As a Pomodoro user, I want a Pause/Resume button right in the notification, so that
I can pause without opening the app.

## Why this matters
This was the last part of the original requirements. It's also the trickiest piece
of Android plumbing in v1: a tap in the system UI has to reach your Python service.

## Acceptance criteria
1. **Given** a running session **When** the shade is opened **Then** the notification
   has a "Pause" button.
2. **Given** "Pause" is tapped **When** the session pauses **Then** the notification
   updates to "Paused" with a "Resume" button within about a second.
3. **Given** "Resume" is tapped **When** the session resumes **Then** the countdown
   continues from the paused time.
4. **Given** the app UI is open **When** the notification button is used **Then** the
   main screen reflects the change too, with one source of truth (ADR-002).
5. **Given** the app has been swiped away **When** the button is used **Then** it
   still works.
6. **Given** a quick double-tap **When** both taps arrive **Then** the result is
   consistent (no crash, and the final state matches the label shown).

## Out of scope
- Reset or Skip in the notification (not requested for v1).

## Mentor notes
- **Concepts to understand first:** actions and `PendingIntent` in
  [tech/android-notifications.md](../tech/android-notifications.md); how p4a passes a
  start argument to a service in
  [tech/python-for-android-services.md](../tech/python-for-android-services.md).
- **Approach options to consider:** an action button's PendingIntent has to point at
  something that ends up in your Python service. Research the routes and compare:
  - an intent that (re)starts the service with an argument or extra;
  - a broadcast received in Python (PyJNIus / p4a broadcast support. UNVERIFIED,
    check the p4a docs).
  For each: how does the service tell "Pause" from "Resume"? Which can you see in
  logcat most easily?
- **Common pitfalls:** PendingIntent flags (the Android docs example uses
  `FLAG_IMMUTABLE`); reusing the same request code for different actions so one
  overwrites the other; the button label getting out of sync with the real state.
- **Questions to ask yourself before coding:**
  - Should the button send "toggle" or an explicit "pause"/"resume"? Think about
    criterion 6.
  - Draw the path of one tap from the shade to the timer core.

## References
- Tech guides: [tech/android-notifications.md](../tech/android-notifications.md),
  [tech/pyjnius.md](../tech/pyjnius.md),
  [tech/python-for-android-services.md](../tech/python-for-android-services.md)
- Related: US-011, ADR-002
- Official docs: https://developer.android.com/develop/ui/views/notifications/build-notification
  — "Add action buttons", `addAction` with `PendingIntent`.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
