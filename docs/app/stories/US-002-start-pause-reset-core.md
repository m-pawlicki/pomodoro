# US-002 — Start, pause, resume, reset in the timer core

**Status:** ready
**Depends on:** US-001
**Learner practices:** state machines; End-time-based timing; testing time by passing in a controllable clock

## Story
As a Pomodoro user, I want to start, pause, resume, and reset the timer, so that I'm
in control of my session.

## Why this matters
"Easy start/pause/reset" was one of the first requirements. Before there are
buttons, the rules need to be right: what's allowed in which state, and what
remaining time is reported. A clear set of states (stopped, running, paused, and
later complete) stops whole categories of bugs, like "pause while stopped".

## Acceptance criteria
1. **Given** a stopped session **When** Start happens **Then** the session is
   running in work interval 1 and remaining time equals the full work length.
2. **Given** a running session **When** 10 minutes pass **Then** remaining time is
   reported as 15:00 (for a 25-minute interval). The test checks this without
   waiting 10 real minutes.
3. **Given** a running session **When** Pause happens **Then** remaining time stops
   changing, however much time passes.
4. **Given** a paused session **When** Resume happens **Then** the countdown continues
   from the paused remaining time.
5. **Given** a session in any state **When** Reset happens **Then** it is stopped, in
   work interval 1, at full work length.
6. **Given** an action that doesn't make sense in the current state (e.g. Pause while
   stopped) **When** it happens **Then** nothing changes and nothing crashes.
7. Remaining time is always computed from an End time (ADR-003), never by counting
   ticks.

## Out of scope
- What happens when remaining time reaches zero (US-003).
- Any UI or display formatting.

## Mentor notes
- **Concepts to understand first:** [End time](../GLOSSARY.md#end-time),
  [Reset](../GLOSSARY.md#reset), [ADR-003](../decisions/ADR-003-end-time-timing.md).
  Also "state machine": a fixed set of states plus rules for which actions move between them.
- **Approach options to consider:**
  - Draw the state diagram first (boxes for states, arrows for actions). Which arrows
    are missing on purpose?
  - Time source: call the clock directly inside the core, or give the core a way to
    ask "what time is it?" that tests can replace. That's dependency injection. What
    does each choice do to criterion 2?
  - What to store while paused: the End time, the remaining time, or both? What can
    go wrong if you store both?
- **Common pitfalls:** pausing and resuming twice and losing or gaining seconds;
  rounding remaining time too early; using a clock that can jump or that stops
  while the phone sleeps (see ADR-003's links).
- **Questions to ask yourself before coding:**
  - Which clock will you use, and why? Read `time.monotonic` and `CLOCK_BOOTTIME`
    in the Python docs and write down one sentence about each.
  - How will a test say "pretend 10 minutes passed"?

## References
- Tech guides: [tech/pytest.md](../tech/pytest.md)
- Related: US-001, ADR-003
- Official docs: https://docs.python.org/3/library/time.html — `time.monotonic()`,
  `time.time()` note on going backwards, `CLOCK_BOOTTIME` and suspend.

## Definition of done
- [ ] Every acceptance criterion verified (pytest)
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
