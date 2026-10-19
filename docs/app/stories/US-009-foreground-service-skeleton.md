# US-009 — Foreground service skeleton + notification permission

**Status:** blocked
**Depends on:** US-008
**Learner practices:** python-for-android services; manifest permissions; foreground service type; the Android 13+ notification permission prompt

## Story
As a Pomodoro user, I want a notification to appear when I start a session and stay
while the session is active, so that I can see the app is still working when I leave it.

## Why this matters
This is the foundation for every Android story after it. It's deliberately thin: a
service that starts, shows a basic notification, survives the app being closed, and
stops on Reset. The timer doesn't move in yet (US-010), so if something breaks you
know it's the service setup.

## Acceptance criteria
1. **Given** Android 13+ and a fresh install **When** the user first taps Start
   **Then** the app asks for notification permission, in context, not at launch.
2. **Given** Start is tapped **When** the service starts **Then** a notification with
   the app name and a fixed text (e.g. "Pomodoro running") appears.
3. **Given** the service is running **When** the app is swiped out of Recents
   **Then** the notification stays and logcat shows the service is still alive
   (e.g. a periodic log line).
4. **Given** the app is opened again and Reset is tapped **When** the service stops
   **Then** the notification disappears.
5. **Given** the user denied notification permission **When** Start is tapped
   **Then** the app still works (the service still runs), and nothing crashes.
6. **Given** a phone running Android 14+ **When** the service starts **Then** it
   doesn't crash for lack of a foreground service type.

## Out of scope
- Moving the timer into the service (US-010); live countdown text (US-011).

## Mentor notes
- **Concepts to understand first:** [Foreground service](../GLOSSARY.md#foreground-service),
  [tech/python-for-android-services.md](../tech/python-for-android-services.md),
  [tech/android-notifications.md](../tech/android-notifications.md) (the permission section).
- **Approach options to consider:**
  - Which foreground service type fits? Read the Android service-types page and
    argue for one in a sentence. Note what Google Play would require for it.
  - `:sticky` or not? The p4a docs say sticky makes the OS restart the service. Is
    that what you want when the user pressed Reset? What about after a crash?
  - Use the p4a built-in foreground notification (title/content arguments to
    `start`) for now, versus building your own. Which is enough for *this* story?
- **Common pitfalls:** the service class name depends on `package.domain`,
  `package.name`, and the capitalized service name; missing manifest permissions
  show up only on the device; the service's Python output appears in logcat under a
  different process.
- **Questions to ask yourself before coding:**
  - What happens to the service if the app process dies? What should?
  - Which permissions does this story need in `buildozer.spec`, and where in the
    official docs does each one come from?

## References
- Tech guides: [tech/python-for-android-services.md](../tech/python-for-android-services.md),
  [tech/android-notifications.md](../tech/android-notifications.md),
  [tech/pyjnius.md](../tech/pyjnius.md)
- Related: ADR-002, US-008
- Official docs: https://python-for-android.readthedocs.io/en/latest/services.html —
  declaring services, `:foreground`, `foregroundServiceType`, starting a service;
  https://developer.android.com/develop/ui/views/notifications/notification-permission
  — POST_NOTIFICATIONS, foreground-service notification behavior when denied;
  https://developer.android.com/develop/background-work/services/fgs/service-types —
  types and required permissions.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
