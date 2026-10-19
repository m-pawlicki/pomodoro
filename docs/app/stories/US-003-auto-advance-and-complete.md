# US-003 — Auto-advance and "Session complete"

**Status:** ready
**Depends on:** US-002
**Learner practices:** transitions and edge cases; signalling "something happened" without coupling to UI

## Story
As a Pomodoro user, I want the next interval to start automatically when one ends,
and the session to stop after the long break, so that I don't have to babysit the
timer.

## Why this matters
Auto-advance was the confirmed behavior: the alarm fires and the next interval
starts on its own. The alarm, the screen, and the notification all need to know
*when* an interval ended, so the core has to announce it in a way any of them can
listen to, without the core knowing they exist.

## Acceptance criteria
1. **Given** a running work interval (not the last) **When** its End time passes
   **Then** the session is running in the following short break, at full short-break
   length.
2. **Given** the Nth work interval ends **When** it advances **Then** the long break
   starts.
3. **Given** the long break ends **When** it advances **Then** the session state is
   "complete" and remaining time shows 0:00.
4. **Given** each interval end **When** it happens **Then** the core reports an
   "interval ended" event exactly once, including which interval ended and what
   comes next (or that the session is complete). This is what the alarm (US-007)
   will listen for.
5. **Given** settings were changed during an interval **When** the next interval
   starts **Then** it uses the new lengths, and the running interval was not
   affected.
6. **Given** time jumps far ahead (e.g. the device was asleep through several
   intervals) **When** the core is next checked **Then** it lands in the correct
   interval with the correct remaining time, or in "complete". It must not get
   stuck or go negative.
7. **Given** a complete session **When** Start happens **Then** a fresh session
   begins at work interval 1.

## Out of scope
- Actually playing an alarm (US-007, US-013).
- Showing the "Session complete" screen (US-004).

## Mentor notes
- **Concepts to understand first:** [Auto-advance](../GLOSSARY.md#auto-advance),
  [Session](../GLOSSARY.md#session); "observer"/"callback" patterns, a way for one
  piece of code to notify others without importing them.
- **Approach options to consider:**
  - Who notices that time is up? The core can check whenever it's asked for the
    remaining time, or someone outside can call an explicit "tick/update". Which
    one makes criterion 6 easier?
  - How to announce events: callbacks registered on the core, returning a list of
    events from an update call, or something else. Think about which one is easiest
    to test, and which one works in a separate process later (ADR-002).
- **Common pitfalls:** firing the event twice for the same interval; accumulated
  drift when the next End time is based on "now" instead of the previous End time;
  forgetting criterion 5 when building the plan up front in US-001.
- **Questions to ask yourself before coding:**
  - If the phone sleeps through two intervals, how many "interval ended" events
    should fire, and should the alarm play for each? Write down your answer and
    bring it to the mentor. It's a product decision.
  - Does your US-001 design still fit criterion 5, or does it need to change?

## References
- Tech guides: [tech/pytest.md](../tech/pytest.md)
- Related: US-002, ADR-003
- Official docs: https://docs.pytest.org/en/stable/getting-started.html

## Definition of done
- [ ] Every acceptance criterion verified (pytest)
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
