# US-011 — Live Session notification

**Status:** blocked
**Depends on:** US-010
**Learner practices:** PyJNIus; notification channels; updating a notification in place; Android rate limits

## Story
As a Pomodoro user, I want the notification to show which interval I'm in and how
long is left, so that I can check the timer without opening the app.

## Why this matters
This was one of the four original requirements. Plyer's notification API has no way
to update a notification or keep it ongoing (see the Plyer docs), so this is your
first real use of Android's own APIs through PyJNIus.

## Acceptance criteria
1. **Given** a running session **When** the user pulls down the notification shade
   **Then** the Session notification shows the interval type, remaining mm:ss, and
   progress (e.g. "Work 2 of 4 · 12:34").
2. **Given** a running session **When** time passes **Then** the remaining time in the
   notification keeps updating, at least once a minute (decide and record the actual
   rate and why).
3. **Given** a paused session **When** the shade is opened **Then** it shows "Paused"
   and the frozen remaining time.
4. **Given** updates to the notification **When** they happen **Then** they don't make
   sound or vibrate each time. Only the alarm makes noise.
5. **Given** the notification is tapped **When** the app isn't open **Then** the app
   opens to the main screen.
6. **Given** the notification channel **When** the user looks in the app's system
   notification settings **Then** it has a clear, human-readable name.

## Out of scope
- Action buttons (US-012). Removing the notification at completion (US-014).

## Mentor notes
- **Concepts to understand first:** [Session notification](../GLOSSARY.md#session-notification),
  notification channels and updating by ID in
  [tech/android-notifications.md](../tech/android-notifications.md), `autoclass` in
  [tech/pyjnius.md](../tech/pyjnius.md).
- **Approach options to consider:**
  - Replace p4a's built-in foreground notification with your own using the same
    notification ID, or post a second notification. What would the user see in each case?
  - Update rate: every second looks nice, but Android documents a rate limit and may
    drop updates. Every 30–60 s, or on state changes only, is gentler. Android also has
    a built-in "chronometer" countdown display. Research it (UNVERIFIED that it fits;
    check the NotificationCompat.Builder reference).
- **Common pitfalls:** translating Kotlin/Java examples to PyJNIus (static fields,
  nested classes with `$`); forgetting to create the channel before posting;
  updates making noise on every tick.
- **Questions to ask yourself before coding:**
  - Which process builds the notification (ADR-002)? Why?
  - Which official doc example are you translating, and what does each call do?

## References
- Tech guides: [tech/android-notifications.md](../tech/android-notifications.md),
  [tech/pyjnius.md](../tech/pyjnius.md)
- Related: ADR-002, US-010
- Official docs: https://developer.android.com/develop/ui/views/notifications/build-notification
  — channels, updating with the same ID, `setOnlyAlertOnce`, rate limit;
  https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder —
  method reference; https://plyer.readthedocs.io/en/latest/api.html — what Plyer's
  `notify` does and doesn't offer.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
