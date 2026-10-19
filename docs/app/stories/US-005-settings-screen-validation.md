# US-005 — Settings screen with validation

**Status:** ready
**Depends on:** US-004
**Learner practices:** multiple screens (ScreenManager); validating user input; "applies from the next interval" rule

## Story
As a Pomodoro user, I want to adjust the work, short break, and long break lengths
and the number of repetitions, so that sessions fit how I work.

## Why this matters
Adjustable intervals and repetitions was the first requirement. Validation protects
the core from nonsense (0 minutes, 500 repetitions), and the "next interval" rule
means changing a setting never makes the running clock jump.

## Acceptance criteria
1. **Given** the main screen **When** the user opens Settings **Then** they see the
   current work, short break, and long break lengths (minutes) and N, and can get
   back to the main screen.
2. **Given** the settings screen **When** values within range are entered (work 1–90,
   short break 1–15, long break 15–60, N 1–12) and confirmed **Then** they are accepted.
3. **Given** an out-of-range, empty, or non-numeric value **When** the user tries to
   confirm **Then** it is not accepted, and the user sees which field is wrong and the
   allowed range.
4. **Given** a stopped session **When** settings change **Then** the main screen
   immediately shows the new work length and "Work 1 of <new N>".
5. **Given** a running or paused session **When** settings change **Then** the
   current countdown is unaffected and the new values apply from the next
   interval.
6. **Given** the app has never been configured **When** Settings opens **Then** it
   shows the defaults 25 / 5 / 20 / 4.

## Out of scope
- Remembering settings after the app closes (US-006).
- Alarm mode choice (US-007).

## Mentor notes
- **Concepts to understand first:** `ScreenManager` and `Screen` in
  [tech/kivy.md](../tech/kivy.md).
- **Approach options to consider:**
  - Free text inputs, sliders, or +/− steppers. Steppers and sliders make invalid
    input impossible; text needs validation. Which teaches you more, and which would
    a user prefer?
  - Who validates: the screen, the core (US-001 already refuses bad settings), or
    both? What does a duplicated rule cost you when the range changes?
  - Apply on every change, or only on "Save"?
- **Common pitfalls:** what N means mid-session (if N drops below the current work
  interval number, what happens? Write down your answer); the range in the UI and the
  range in the core drifting apart.
- **Questions to ask yourself before coding:**
  - Where is the single source of truth for the allowed ranges?
  - How does the main screen find out that settings changed?

## References
- Tech guides: [tech/kivy.md](../tech/kivy.md)
- Related: US-001 (validation), US-003 (criterion 5, next interval)
- Official docs: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html — `Screen`,
  `ScreenManager.current`.

## Definition of done
- [ ] Every acceptance criterion verified by hand
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
