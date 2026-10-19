# US-007 — Alarm mode choice, played on desktop

**Status:** ready
**Depends on:** US-004, US-006
**Learner practices:** bundling assets; playing sounds with Kivy; keeping side effects out of the core

## Story
As a Pomodoro user, I want to pick an alarm sound, vibrate-only, or silent, so that
interval changes are announced the way I like.

## Why this matters
With auto-advance, the alarm is the only thing that tells you a break has started.
This story builds the choice and playback on desktop, where it's easy to test. US-013
redoes playback for Android and adds silent-mode handling.

## Acceptance criteria
1. **Given** the settings screen **When** the user opens the Alarm mode option
   **Then** they can choose one of 3–5 bundled sounds, "Vibrate only", or "Silent".
2. **Given** a sound is chosen **When** the user picks it **Then** a short preview
   plays.
3. **Given** a sound Alarm mode **When** any interval ends (auto-advance) **Then** the
   sound plays once (a few seconds) and needs no dismissing.
4. **Given** "Vibrate only" on desktop **When** an interval ends **Then** no sound
   plays and nothing crashes (desktops can't vibrate; log a message instead).
5. **Given** "Silent" **When** an interval ends **Then** nothing plays.
6. **Given** the app is reopened **When** settings load **Then** the chosen Alarm mode
   is remembered (US-006 mechanism).
7. **Given** the sound files **When** you check the project **Then** they are
   bundled with the app, with a license that lets you ship them.

## Out of scope
- The phone's ringer mode / Do Not Disturb (US-013).
- Custom sound files from the device (out of scope for v1).

## Mentor notes
- **Concepts to understand first:** [Alarm mode](../GLOSSARY.md#alarm-mode);
  `SoundLoader` in [tech/kivy.md](../tech/kivy.md).
- **Approach options to consider:**
  - Who plays the alarm: the core (no, it must stay free of Kivy, see ADR-004), the UI
    listening to the core's "interval ended" event, or a separate small "alarm"
    module the UI calls. Which one will move into the service most easily in US-013?
  - Load sounds once at startup, or each time they play?
- **Common pitfalls:** audio formats the Kivy docs don't promise to support (test
  your chosen files early, including on the phone after US-008); paths to asset files
  that only work from one directory; sounds without a clear license.
- **Questions to ask yourself before coding:**
  - What should the alarm module expose so it works the same whether a sound or
    vibration happens underneath?
  - Where will you find freely licensed short sounds, and how will you record the
    license?

## References
- Tech guides: [tech/kivy.md](../tech/kivy.md),
  [tech/android-alarm-audio-vibrate.md](../tech/android-alarm-audio-vibrate.md) (for later)
- Related: US-003 (event), US-006, US-013
- Official docs: https://kivy.org/doc/stable/api-kivy.core.audio.html — `SoundLoader.load`,
  `Sound.play`/`stop`.

## Definition of done
- [ ] Every acceptance criterion verified by hand
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
