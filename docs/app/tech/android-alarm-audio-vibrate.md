# Alarm on Android: sound, vibration, ringer mode

**Used for:** announcing interval ends according to the Alarm mode and the phone's silent/DND state (US-007, US-013).
**Official docs:** see sources   **Version covered:** current docs as of 2026-10-12
**Sources (fetched 2026-10-12):**
- https://kivy.org/doc/stable/api-kivy.core.audio.html
- https://plyer.readthedocs.io/en/latest/api.html

## What it is
Three separate pieces:
1. **Playing a sound.** On desktop, Kivy's `SoundLoader.load()` gives a `Sound` with
   `play()`/`stop()` (Kivy audio page; it doesn't list formats or Android specifics).
2. **Vibrating.** Plyer's `vibrator` facade offers `vibrate(time=1)`,
   `pattern(pattern, repeat)`, `cancel()`, and `exists()`. Durations are in
   **seconds** (Plyer API page). The page doesn't list platforms.
3. **Respecting the phone's mode.** Android's `AudioManager` reports the **ringer
   mode** (normal / vibrate / silent), and Do Not Disturb is reported by
   `NotificationManager`'s interruption filter.
   **UNVERIFIED:** the Android reference pages for these were too large to fetch
   and read in this session. Read
   https://developer.android.com/reference/android/media/AudioManager (`getRingerMode`)
   and https://developer.android.com/reference/android/app/NotificationManager
   (`getCurrentInterruptionFilter`) yourself and note what they say.

## Why we use it here
The confirmed rule is that the alarm follows the phone's mode, and sound or vibration
must work from the service when the app is closed. Plyer is the simplest documented
vibration API from Python. PyJNIus covers what Plyer doesn't.

## Set up
- **Sound files:** short, freely licensed files bundled with the app. Check
  `source.include_exts` in `buildozer.spec` includes their extension.
- **Vibration permission:** UNVERIFIED: Android normally requires the `VIBRATE`
  permission. Confirm in the Plyer docs/source or the Android docs, and add it via
  `android.permissions`.
- **Verify:** on the phone, trigger each Alarm mode from a debug button and confirm
  what happens in each ringer mode.

## First steps to explore
1. **Spike (US-013):** can `SoundLoader` play your file from inside the service
   process (which has no Kivy window)? Try it before designing anything else. If it
   can't, research Android's `MediaPlayer` or `SoundPool` in the Android reference.
2. Compare two strategies for "follow the phone's mode": check the ringer mode
   yourself, or play with an audio type that Android already silences in silent/DND
   (research Android "audio attributes" and "usage"). Bring your findings to the mentor.
3. Try Plyer's `vibrator.exists()` on desktop vs. phone.

## Common problems
- Sound works on desktop but not in the APK: the file wasn't packaged, or the path is
  relative to the wrong directory.
- Vibration silently does nothing: missing permission, or the phone's own vibration
  setting is off.
- Playback cut off: the sound/player object was garbage-collected. Keep a reference.

## Going deeper
- Kivy audio: https://kivy.org/doc/stable/api-kivy.core.audio.html
- Plyer API: https://plyer.readthedocs.io/en/latest/api.html
