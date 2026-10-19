# US-014 — Notification lifecycle + end-to-end check

**Status:** blocked
**Depends on:** US-012, US-013
**Learner practices:** cleaning up resources; end-to-end acceptance testing on a device

## Story
As a Pomodoro user, I want the notification to appear only while a session is active
and to tell me when the session is complete, so that it's useful and never clutters
my phone.

## Why this matters
"Only while a session is active" was a confirmed rule, and a notification that never
goes away is the quickest way to get an app uninstalled. This story also runs the
full success test from the design session, which is how you know v1 is done.

## Acceptance criteria
1. **Given** a session completes (long break ends) **When** the shade is opened
   **Then** the notification says "Session complete" and has no Pause button.
2. **Given** the "Session complete" notification **When** the user dismisses it
   (or taps it and the app opens) **Then** it's gone and the service has stopped.
3. **Given** a running or paused session **When** Reset is tapped in the app
   **Then** the notification disappears and the service stops.
4. **Given** no session is active **When** the shade is opened **Then** there is no
   Pomodoro notification.
5. **Given** a running session **When** the phone is rebooted **Then** after the reboot
   there's no stale notification and the app opens in the stopped state (a reboot
   ends the session, as confirmed).
6. **End-to-end success test:** **Given** settings 1 / 1 / 1 min, N=2, a sound Alarm
   mode **When** the user taps Start, locks the phone, and swipes the app away
   **Then**: the notification shows the countdown; an alarm sounds at each
   interval change; Pause/Resume from the notification works; after the long break
   the notification shows "Session complete".

## Out of scope
- Statistics or history of completed sessions (out of scope for v1).

## Mentor notes
- **Concepts to understand first:** stopping a p4a service and removing a
  notification, in [tech/python-for-android-services.md](../tech/python-for-android-services.md)
  and [tech/android-notifications.md](../tech/android-notifications.md).
- **Approach options to consider:**
  - Should the service stop itself when the session completes, or wait until the
    "complete" notification is dismissed? A foreground notification is tied to its
    service. Research what happens to it when the service stops.
  - How do you find out the user dismissed a notification? Research "delete intent".
    Is it worth it, or is "tap to open" enough for v1? Bring your choice to the mentor.
- **Common pitfalls:** a sticky service restarting after you stopped it on purpose;
  a "complete" notification that can't be dismissed because it's still the
  foreground notification.
- **Questions to ask yourself before coding:**
  - List every way a session can end. Does each one remove the notification?
  - Write criterion 6 as a checklist you can repeat after every future change.

## References
- Tech guides: [tech/android-notifications.md](../tech/android-notifications.md),
  [tech/python-for-android-services.md](../tech/python-for-android-services.md)
- Related: US-009–US-013, ADR-002
- Official docs: https://developer.android.com/develop/ui/views/notifications/build-notification
  — removing notifications (`cancel()`); https://python-for-android.readthedocs.io/en/latest/services.html.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
