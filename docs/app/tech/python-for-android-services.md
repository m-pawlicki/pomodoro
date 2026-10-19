# python-for-android services

**Used for:** the Timer service, which runs the session in the background so it survives the app being closed (US-009 onward, ADR-002).
**Official docs:** https://python-for-android.readthedocs.io/en/latest/services.html   **Version covered:** `latest` docs as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://python-for-android.readthedocs.io/en/latest/services.html
- https://developer.android.com/develop/background-work/services/fgs/service-types
- https://developer.android.com/develop/ui/views/notifications/notification-permission

## What it is
On Android, an **activity** is a screen the user sees (your Kivy app is one). A
**service** is a component that runs without a screen. A **foreground service** is
one the user is told about through a visible notification, which signals to Android
that the work matters to the user.

**python-for-android** (p4a) is what Buildozer uses under the hood. It lets you write
a service as a **separate Python script**. That script runs in its **own process**,
separate from the Kivy app, so the two can't share Python objects directly.

## Why we use it here
The p4a docs say services are the way to run code when the app isn't open. The
confirmed behavior ("keeps running after swipe-away") needs that. The alternative,
keeping the timer in the UI, was rejected in ADR-002.

## Set up
All from https://python-for-android.readthedocs.io/en/latest/services.html:

1. **Declare the service** in `buildozer.spec`, `[app]` section, with a `services`
   line in the form `name:path_to_script.py` plus optional flags. Multiple services
   are comma-separated.
2. **Flags:**
   - `:foreground`: run as an Android foreground service.
   - `:sticky`: the OS restarts the service after it exits or crashes.
   - `:foregroundServiceType=TYPE`: the docs say this is **mandatory with
     `:foreground` on Android 14+**.
3. **Start it from the app** with PyJNIus: get the generated service class via
   `autoclass`, then call its `start` method with the `PythonActivity.mActivity` reference
   and an argument string. The class name is `Service` plus your service name with a
   capital first letter, inside your app's package (`package.domain` + `package.name`).
   Read the docs' example rather than copying it blindly. Know what each part is.
4. **Foreground notification:** extra `start` arguments set the notification's small
   icon, title, and content.
5. **Arguments:** the start argument reaches the service as the
   `PYTHON_SERVICE_ARGUMENT` environment variable (a string; the docs suggest JSON
   for structured data).
6. **Verify:** start the service, swipe the app away, and confirm the service's log
   lines keep appearing in logcat.

## Choosing a foreground service type
From the Android service-types page: there is a fixed list of types (camera,
dataSync, location, mediaPlayback, shortService, specialUse, …), each with a matching
permission. `shortService` is for work of only a few minutes. `specialUse` covers
valid uses not covered by other types, needs `FOREGROUND_SERVICE_SPECIAL_USE`, and
asks for a written justification that Google Play reviews. Decide in US-009 and
record why.

## Notification permission
From the Android notification-permission page: on Android 13+ (API 33),
`POST_NOTIFICATIONS` is a runtime permission. Apps don't need it to *start* a
foreground service, but if it's denied, the service's notification shows in the
Task Manager instead of the notification drawer.

## First steps to explore
1. Read the whole p4a services page once, start to finish.
2. Make a service that only logs "alive" every few seconds. Watch it in logcat
   while you open and close the app.
3. Find out what happens on Reset if the service is `:sticky`.

## Common problems
- **Wrong class name** when starting the service: check package domain/name and the
  capitalization rule.
- **Crash on Android 14+** without a service type (docs: mandatory).
- **"Why can't the service see my app's variables?"** Separate processes (see
  [osc-ipc.md](osc-ipc.md)).

## Going deeper
- p4a docs home: https://python-for-android.readthedocs.io/en/latest/
- Android foreground service types:
  https://developer.android.com/develop/background-work/services/fgs/service-types
