# US-001 — Interval plan from settings

**Status:** ready
**Depends on:** none
**Learner practices:** modelling a domain in plain Python; first pytest tests; project layout

## Story
As a Pomodoro user, I want the timer to know the exact sequence of work and break
intervals for my settings, so that every session follows the classic pattern.

## Why this matters
Everything else (the screen, the service, the notification) asks "what interval is
this, and what comes next?" Getting that right in plain, tested Python first means
later bugs are about Kivy or Android, not about the sequence itself. This is also
your walking skeleton: the smallest piece of real behavior.

## Acceptance criteria
1. **Given** the default settings (work 25, short break 5, long break 20, N=4)
   **When** the Interval plan is produced **Then** it is: work, short, work, short,
   work, short, work, long. That's 8 intervals, each with its type and length.
2. **Given** N=1 **When** the plan is produced **Then** it is: work, long (no short
   break).
3. **Given** any interval in the plan **When** you ask for its position
   **Then** you can tell which work interval it belongs to (e.g. "Work 2 of 4"), so
   the screen can show progress.
4. **Given** settings outside the allowed ranges (work 1–90, short break 1–15,
   long break 15–60, N 1–12)
   **When** a plan is requested **Then** it is refused with a clear error message, not
   a silently wrong plan.
5. **Given** the project **When** you run pytest **Then** tests covering criteria 1–4
   pass, and the code under test imports nothing from Kivy or Android.

## Out of scope
- Any timing, clocks, or UI. This story is only "what is the sequence".
- Saving settings (US-006).

## Mentor notes
- **Concepts to understand first:** [Interval plan](../GLOSSARY.md#interval-plan),
  [Repetitions (N)](../GLOSSARY.md#repetitions-n),
  [Work interval / Short break / Long break](../GLOSSARY.md#work-interval--short-break--long-break); pytest
  basics in [tech/pytest.md](../tech/pytest.md).
- **Approach options to consider:**
  - Build the whole list up front, or compute "the interval at position i" on
    demand. A list is easy to inspect in tests; computing on demand stores less state.
    Which is easier to explain to someone else?
  - How to represent an interval type: plain strings, constants, or an `enum`. What
    happens with each option when you mistype "shrot"?
  - Where settings live: one small object holding all four values, or four separate
    arguments. Consider what US-005 and US-006 will need to pass around.
- **Common pitfalls:** off-by-one at the end (a short break *and* a long break after
  the last work interval); mixing minutes and seconds; letting validation drift
  away from the ranges in the glossary/restatement.
- **Questions to ask yourself before coding:**
  - What should the tests be? Write the expected plan for N=1, N=2, and N=4 on paper first.
  - Where will this code live so that Kivy, the service, and pytest can all import
    it without importing each other?
  - Should invalid settings raise an exception or return something? What would the
    settings screen (US-005) find easiest to work with?

## References
- Tech guides: [tech/pytest.md](../tech/pytest.md)
- Related: ADR-004 (desktop first), ADR-002 (core reused in the service)
- Official docs: https://docs.pytest.org/en/stable/getting-started.html — how test
  files and functions are discovered; your first test.

## Definition of done
- [ ] Every acceptance criterion verified (pytest output for 1–5)
- [ ] Learner can explain how it works and why they built it that way
- [ ] Docs/glossary updated if new terms appeared
