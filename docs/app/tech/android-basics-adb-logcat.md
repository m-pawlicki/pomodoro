# Android basics: adb and logcat

**Used for:** installing your APK on the phone and reading its logs and crash tracebacks (US-008 onward).
**Official docs:** https://developer.android.com/tools/adb · https://developer.android.com/tools/logcat   **Version covered:** current docs as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://developer.android.com/tools/adb
- https://developer.android.com/tools/logcat

## What it is
- **adb** (Android Debug Bridge): "a versatile command-line tool that lets you
  communicate with a device", for installing and debugging apps. A client on your
  PC talks to a server, which talks to a small program (adbd) on the phone.
- **logcat**: "a command-line tool that dumps a log of system messages", including
  messages from your app. Python's output and tracebacks from a Kivy app end up
  here, which makes it your main debugging tool on the phone.

## Why we use it here
Android Studio does these steps for you, but we aren't using Android Studio (we
build with Buildozer). adb and logcat are the standard tools for this.

## Set up
1. **Install adb on Arch.** UNVERIFIED: no Arch-specific source was fetched. adb is
   part of Google's "Android SDK Platform-Tools". Find the Arch package or download
   in the Arch Wiki / Android docs yourself, and note what you used.
2. **Enable Developer options and USB debugging** (source:
   https://developer.android.com/tools/adb): on most phones, Settings → About phone →
   tap **Build number** seven times, then turn on **USB debugging** under Developer
   options. Accept the RSA key prompt when you connect the USB cable.
3. **Verify:** `adb devices -l`. Your phone should be listed with status `device`
   (not `offline` or `unauthorized`).
4. **Install an APK:** `adb install path_to_apk` (source: adb docs).

## First steps to explore
1. Run `adb logcat` while opening your app, and see how much output there is.
2. Filter by tag and priority (source: logcat docs): filters look like `tag:priority`,
   and `*:S` silences everything you didn't name, e.g.
   `adb logcat "MyTag:D *:S"`. Quote the expression so the shell doesn't expand `*`.
   Find out which tag your Python output uses by looking at unfiltered output once
   (python-for-android apps commonly log under a "python" tag. UNVERIFIED, so check
   on your device).
3. Trigger a deliberate exception in your app and find the traceback in logcat.

## Common problems
- `adb: more than one device/emulator`: use `adb -s <serial> install ...` (adb docs).
- Device shows `offline` or isn't listed: check the cable and that USB debugging is
  on, and re-accept the RSA prompt.
- Installing over an app signed with a different key fails. Uninstall the old one first.

## Going deeper
- adb reference: https://developer.android.com/tools/adb
- logcat reference: https://developer.android.com/tools/logcat
