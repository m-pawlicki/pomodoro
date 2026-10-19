# US-006 — Remember settings between launches

**Status:** ready
**Depends on:** US-005
**Learner practices:** Kivy JsonStore; `App.user_data_dir`; app lifecycle

## Story
As a Pomodoro user, I want my settings remembered after I close the app, so that I
set them once.

## Why this matters
Nobody wants to re-enter "50 / 10 / 30" every morning. This story also teaches
*where* an app is allowed to write files, which matters a lot on Android.

## Acceptance criteria
1. **Given** settings were changed and confirmed **When** the app is closed and
   reopened **Then** the settings screen and main screen show the saved values.
2. **Given** a fresh install (no saved settings) **When** the app opens **Then** the
   defaults 25 / 5 / 20 / 4 are used.
3. **Given** the saved settings file is missing, empty, or corrupted **When** the app
   opens **Then** it falls back to defaults without crashing.
4. **Given** the settings are saved **When** you look for the file **Then** it is in
   the app's user data directory, not in the project or current working directory.
5. **Given** the Alarm mode is added later (US-007) **When** it is saved **Then** it
   uses the same mechanism (this story's design should allow that).

## Out of scope
- Saving session progress (a reboot ends the session, which is confirmed).

## Mentor notes
- **Concepts to understand first:** `JsonStore` and `App.user_data_dir` in
  [tech/kivy.md](../tech/kivy.md). On Android, `user_data_dir` is the app's private
  files directory.
- **Approach options to consider:**
  - Save on every change, or on "Save" / app exit. The Kivy docs warn that after
    `on_pause`, `on_resume` may never be called. What does that tell you about
    saving only on exit?
  - Keep loading/saving in its own small module, or inside the settings screen.
    Which one can the service (US-010) reuse?
- **Common pitfalls:** a relative file path that works from your terminal but not on the
  phone; not handling the corrupted-file case.
- **Questions to ask yourself before coding:**
  - Who reads the settings on Android once the timer lives in the service (ADR-002)?
    Both processes? Just one?
  - How will you test criterion 3 on purpose?

## References
- Tech guides: [tech/kivy.md](../tech/kivy.md)
- Related: US-005, US-007, ADR-002
- Official docs: https://kivy.org/doc/stable/api-kivy.storage.html — JsonStore;
  https://kivy.org/doc/stable/api-kivy.app.html — `user_data_dir`, `on_pause`/`on_stop`
  warnings.

## Definition of done
- [ ] Every acceptance criterion verified by hand
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
