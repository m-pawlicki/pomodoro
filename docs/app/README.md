# Pomodoro App — Design Docs

These docs describe **what** the Pomodoro app should do and **why**, broken into
user stories you can pick up one at a time. They do not contain the code — you
write all of it. A mentor (Claude) helps with questions, hints, design advice, and
reviews.

## Learner profile

- **Who:** the developer building this app (solo).
- **Experience:** comfortable with Python (classes, modules, virtualenvs, pip);
  new to Kivy and to Android development.
- **Machine:** Arch Linux.
- **Learning style:** try first, read the docs when stuck.
- **Time:** a few hours a week, so stories are sized to finish in about one sitting.

Hints and tech guides are written for this level. If that changes, update this
section so future stories match.

## How the docs fit together

| File / folder | What it's for |
|---|---|
| [OVERVIEW.md](OVERVIEW.md) | Read first: what the app is and its major parts |
| [GLOSSARY.md](GLOSSARY.md) | The words we use (Session, Interval, End time…) and what they mean here |
| [BACKLOG.md](BACKLOG.md) | Every story, its status, and what it depends on |
| [TECH-STACK.md](TECH-STACK.md) | The technologies chosen, with one line on why for each |
| [stories/](stories/) | One file per user story: behavior, acceptance criteria, mentor hints |
| [tech/](tech/) | Beginner guides: what each tool is, how to set it up, where to read more |
| [decisions/](decisions/) | Short records of architecture choices and why they were made |
| [sessions/](sessions/) | Log of each design session: decisions, assumptions, open questions |

## How to pick up a story

1. Open [BACKLOG.md](BACKLOG.md) and pick the lowest-numbered `ready` story.
2. Read the story, then the tech guides it links to, and check any unfamiliar term in the glossary.
3. Answer the story's "Questions to ask yourself before coding" in a few
   sentences, then write the code.
4. Check every acceptance criterion by hand, then ask for a review.
5. Update the story's status in BACKLOG.md.

Stuck? Ask the mentor and say what you tried and what you saw. You'll get a hint,
not the answer.

## Index

- Stories: US-001 to US-014, see [BACKLOG.md](BACKLOG.md)
- Tech guides: [kivy](tech/kivy.md) · [pytest](tech/pytest.md) ·
  [buildozer-docker](tech/buildozer-docker.md) ·
  [android-basics-adb-logcat](tech/android-basics-adb-logcat.md) ·
  [python-for-android-services](tech/python-for-android-services.md) ·
  [pyjnius](tech/pyjnius.md) · [android-notifications](tech/android-notifications.md) ·
  [osc-ipc](tech/osc-ipc.md) · [android-alarm-audio-vibrate](tech/android-alarm-audio-vibrate.md)
- Decisions: [ADR-001](decisions/ADR-001-buildozer-docker.md) ·
  [ADR-002](decisions/ADR-002-service-owns-timer.md) ·
  [ADR-003](decisions/ADR-003-end-time-timing.md) ·
  [ADR-004](decisions/ADR-004-desktop-first.md)
- Sessions: [2026-10-12 v1 design](sessions/2026-10-12-v1-design.md)
