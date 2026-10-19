# US-013 — Android alarm that follows ringer mode

**Status:** blocked
**Depends on:** US-010, US-007
**Learner practices:** vibration and audio on Android; reading the phone's ringer mode; a research spike

## Story
As a Pomodoro user, I want the alarm to play my chosen sound or vibrate at each
interval change, while respecting my phone's silent and Do Not Disturb settings,
so that it never embarrasses me in a meeting.

## Why this matters
With auto-advance, the alarm is how you know a break started, and it must fire even
when the app is closed. That means it plays from the service, which has no Kivy
window. The confirmed rule is to follow the phone's mode.

## Acceptance criteria
1. **Given** a sound Alarm mode and ringer on normal **When** an interval ends (app
   open or closed) **Then** the chosen sound plays once.
2. **Given** "Vibrate only" **When** an interval ends **Then** the phone vibrates
   briefly and no sound plays.
3. **Given** a sound Alarm mode and the phone on vibrate **When** an interval ends
   **Then** it vibrates instead of playing sound.
4. **Given** the phone on silent or in Do Not Disturb **When** an interval ends
   **Then** no sound plays (vibration only if the phone's mode allows it). Record
   exactly what you implemented.
5. **Given** "Silent" Alarm mode **When** an interval ends **Then** nothing happens.
6. **Given** the screen is off and the phone locked **When** an interval ends
   **Then** criteria 1–3 still hold.

## Out of scope
- Overriding silent mode like an alarm clock (it follows the phone's mode, as confirmed).

## Mentor notes
- **Concepts to understand first:** [Alarm mode](../GLOSSARY.md#alarm-mode);
  [tech/android-alarm-audio-vibrate.md](../tech/android-alarm-audio-vibrate.md).
- **Start with a spike** (a short time-boxed experiment, about one sitting): can
  Kivy's `SoundLoader` play your bundled file from inside the service process, or do
  you need Android's own media player through PyJNIus? This is an open question in
  the [session log](../sessions/2026-10-12-v1-design.md). Write down what you find.
- **Approach options to consider:**
  - Vibration: Plyer's `vibrator` (simple API) vs. Android's Vibrator through PyJNIus.
    Does Plyer need any permission in `buildozer.spec`? Check its docs.
  - Ringer mode / DND: check them yourself before playing, or let Android decide by
    choosing the right audio type (e.g. "notification" vs. "alarm"). Which matches
    "follow the phone's mode" more faithfully? Research it.
- **Common pitfalls:** the vibrate permission missing from the manifest; assets not
  found from the service's working directory; playback cut off because the player
  object was garbage-collected.
- **Questions to ask yourself before coding:**
  - Can you reuse your US-007 alarm module's interface and just swap what's underneath?
  - How will you test criterion 4 on your own phone?

## References
- Tech guides: [tech/android-alarm-audio-vibrate.md](../tech/android-alarm-audio-vibrate.md),
  [tech/pyjnius.md](../tech/pyjnius.md)
- Related: US-007, US-010, ADR-002
- Official docs: https://plyer.readthedocs.io/en/latest/api.html — Vibrator facade;
  https://developer.android.com/reference/android/media/AudioManager — ringer mode
  (see the tech page; details UNVERIFIED there).

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
