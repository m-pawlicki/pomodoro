# US-010 — Move the timer into the service, talk over OSC

**Status:** blocked
**Depends on:** US-009, US-003
**Learner practices:** inter-process communication (IPC); single source of truth; designing a small message protocol

## Story
As a Pomodoro user, I want the timer to keep counting when I close the app, and to
show the right time when I reopen it, so that closing the app never loses my session.

## Why this matters
This is the core architecture move (ADR-002). After it, the service owns the
session and the UI is a remote control. If your core and UI were cleanly separated
in US-001–004, this story is mostly plumbing.

## Acceptance criteria
1. **Given** the app on the phone **When** Start / Pause / Resume / Reset are tapped
   **Then** the commands reach the service and the main screen reflects the
   service's state within about a second.
2. **Given** a running session **When** the app is swiped away for 3 minutes and
   reopened **Then** the main screen shows the correct interval and remaining time
   (about 3 minutes less), not a fresh session.
3. **Given** a 1-minute work interval **When** it ends while the app is closed
   **Then** auto-advance still happens in the service (visible in logcat and on
   reopening).
4. **Given** settings are changed in the app **When** a session is running **Then**
   the service applies them from the next interval (US-003 criterion 5).
5. **Given** the app opens while no service is running **When** the main screen
   loads **Then** it shows the stopped state and doesn't hang waiting for a reply.
6. **Given** desktop runs (`python main.py`) **When** the app starts **Then**
   everything still works, either through a desktop path that runs the core in the
   app or a local service stand-in. You choose which and record why.

## Out of scope
- Notification content (US-011) and buttons (US-012); Android alarm (US-013).

## Mentor notes
- **Concepts to understand first:** IPC and why two processes can't just share a
  Python object; OSC addresses and messages in [tech/osc-ipc.md](../tech/osc-ipc.md);
  [ADR-002](../decisions/ADR-002-service-owns-timer.md).
- **Approach options to consider:**
  - Should the UI *poll* the service ("what's the state?") or the service *push*
    state to the UI? What happens to pushed messages when the UI is closed?
  - Message design: a few command addresses (e.g. one per action) plus one state
    message, or a single generic message with JSON. Which is easier to debug in logcat?
  - Ports: fixed numbers or passed in at start? What if one is already in use?
  - Which process reads saved settings, and how does the other find out about changes?
- **Common pitfalls:** OSC is UDP, so messages can be lost or arrive with nobody
  listening; blocking the Kivy UI thread while waiting for a reply; byte strings vs.
  text (oscpy's `encoding` option); two sources of truth creeping back in.
- **Questions to ask yourself before coding:**
  - Write down every message (name, direction, contents) before writing code. Bring
    the list to the mentor for review.
  - If a command is lost, how does the UI recover?

## References
- Tech guides: [tech/osc-ipc.md](../tech/osc-ipc.md),
  [tech/python-for-android-services.md](../tech/python-for-android-services.md)
- Related: ADR-002, ADR-003, US-003, US-006
- Official docs: https://python-for-android.readthedocs.io/en/latest/services.html —
  separate process, OSC suggestion, `PYTHON_SERVICE_ARGUMENT`;
  https://github.com/kivy/oscpy — server/client, `encoding`.

## Definition of done
- [ ] Every acceptance criterion verified on a real phone
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
