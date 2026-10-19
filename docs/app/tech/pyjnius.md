# PyJNIus

**Used for:** calling Android's Java APIs from Python: starting the service, building the Session notification, reading the ringer mode (US-009, US-011–013).
**Official docs:** https://pyjnius.readthedocs.io/en/latest/   **Version covered:** `latest` docs as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://pyjnius.readthedocs.io/en/latest/quickstart.html
- https://python-for-android.readthedocs.io/en/latest/services.html (its service-start example uses PyJNIus)
- https://plyer.readthedocs.io/en/latest/api.html (shows what Plyer can't do)

## What it is
Android's APIs are written in Java and Kotlin. PyJNIus lets Python use Java classes
directly: `autoclass('some.java.ClassName')` gives you a Python object that wraps the
Java class, so you can call its methods and read its fields. The quickstart shows
this with `java.util.Stack`. Nested Java classes are reached with a `$` separator,
e.g. `android.os.Build$VERSION`.

## Why we use it here
**Plyer** gives simple cross-platform APIs, but its `notify` has no action buttons,
no ongoing flag, and no way to update a notification (Plyer API page). The Session
notification needs all three. The p4a docs also use PyJNIus to start services.
There's no simpler documented alternative for these features from Python.

## Set up
PyJNIus is used on the phone, inside the APK. Its setup is part of your Buildozer
build. UNVERIFIED: whether you must list `pyjnius` in `requirements` or p4a
includes it automatically. Check the p4a / Buildozer docs and note what you find.
On desktop, Android classes don't exist, so code using them must only run on
Android. Figure out how your app will know which platform it's on (look up
`kivy.utils.platform` in the Kivy docs).

## First steps to explore
1. Read the quickstart. Try `autoclass` with the `java.util.Stack` example, if you
   can get PyJNIus running on desktop (needs a JDK; optional).
2. Pick one small Android doc example (e.g. reading `Build$VERSION`) and run it on
   the phone, logging the result.
3. Practice **translating** a Kotlin snippet from developer.android.com into the
   equivalent PyJNIus calls on paper, then compare with the mentor.

## Common problems
- **ClassNotFound:** check the full Java class name, and use `$` for nested classes.
- **Static fields and constants** (e.g. `PendingIntent.FLAG_IMMUTABLE`) are read
  off the autoclass'ed class.
- **Calling Android-only code on desktop** crashes. Guard by platform.

## Going deeper
- PyJNIus docs: https://pyjnius.readthedocs.io/en/latest/
- Android API reference: https://developer.android.com/reference
