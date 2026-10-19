# Android notifications

**Used for:** the Session notification: live status, Pause/Resume button, "Session complete" (US-009, US-011, US-012, US-014).
**Official docs:** https://developer.android.com/develop/ui/views/notifications   **Version covered:** current docs as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://developer.android.com/develop/ui/views/notifications/build-notification
- https://developer.android.com/develop/ui/views/notifications/notification-permission
- https://plyer.readthedocs.io/en/latest/api.html

## What it is
A notification is a message Android shows outside your app (status bar and
notification shade). Key ideas:
- **Notification channel:** a category the user can control in system settings.
  Required on Android 8.0+. The docs say to create it at startup, and that
  re-creating an existing channel does nothing.
- **Notification ID:** posting again with the same ID **updates** the existing
  notification. If the user dismissed it, a new one appears.
- **Action buttons:** up to three. Each carries a `PendingIntent`, a "token" that
  lets the system perform an action on your app's behalf later. An action can
  target a broadcast receiver instead of opening an activity.
- **Rate limit:** the docs warn Android may drop updates if you post too often.
- **setOnlyAlertOnce:** sound/vibration only the first time, not on updates.

## Why we use it here
The persistent notification with Pause/Resume was an original requirement. Plyer's
`notify` can't update, stay ongoing, or show buttons (Plyer API page), so we use the
Android APIs through [PyJNIus](pyjnius.md).

## Set up
1. **Permission (Android 13+):** declare `POST_NOTIFICATIONS` and request it at
   runtime, in context (e.g. on first Start), per the permission page. How to declare
   it in Buildozer: `android.permissions` in `buildozer.spec` (see
   [buildozer-docker.md](buildozer-docker.md)).
2. **If denied:** notifications are blocked, but a foreground service's notification
   still shows in the Task Manager (permission page).
3. **Verify:** after granting, the app appears with notifications enabled in system
   Settings → Apps → your app → Notifications.

## First steps to explore
1. Read "Create a notification" (build-notification page) top to bottom: channel →
   builder → notify → update → actions → remove.
2. Translate the channel-creation example into PyJNIus calls (on paper first).
3. Look up these methods in the `NotificationCompat.Builder` reference
   (https://developer.android.com/reference/androidx/core/app/NotificationCompat.Builder):
   `setOngoing`, `setOnlyAlertOnce`, `setSilent`, `setUsesChronometer`,
   `setDeleteIntent`. UNVERIFIED: the reference page was too large to fetch fully, so
   read the descriptions yourself and note what each does.
4. Removing: the docs say `cancel()` removes a notification, including ongoing ones.

## Common problems
- **Nothing shows:** missing channel, missing permission, or (Android 13+) the user
  denied it.
- **Every update buzzes:** use `setOnlyAlertOnce` and don't make the channel noisy.
- **Updates lag or skip:** you hit the rate limit. Update less often.
- **Two buttons do the same thing:** PendingIntents that are too similar can
  overwrite each other. Research PendingIntent request codes.

## Going deeper
- Notifications overview: https://developer.android.com/develop/ui/views/notifications
- Permission: https://developer.android.com/develop/ui/views/notifications/notification-permission
