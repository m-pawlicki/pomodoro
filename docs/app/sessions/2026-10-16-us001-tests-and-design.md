# Session 2026-10-16 — US-001 tests and interval design

## Topic
Mentoring session on US-001 (Interval plan from settings). Started from "do I need to
store the settings yet?", then worked through the first real tests, two bugs, and a
redesign of how intervals and the plan are modelled.

## Where things stand
- `src/pomodoro/interval.py`: `Interval.create_interval` builds a `list[IntervalType]`
  and validates type and range for work / short / long / n.
- `tests/test_interval.py`: 30 tests, all passing (pass, edge min/max, below-min,
  above-max, float/bool type checks, n=1, default plan).
- Not yet committed.
- US-001 is **not done**: criterion 1 (each interval carries its length) and
  criterion 3 (position, e.g. "Work 2 of 4") are still open.

## What was learned
- **Scope:** saving settings is US-006 (after US-005). For now, settings are values
  passed in; defaults live in `interval_settings.py`.
- **`range` starts at 0.** `range(n)` runs n times, which produced one extra
  work + short pair. An empty range (`range(0)`) runs the loop body zero times, so
  the special `n == 1` branch was redundant and was removed.
- **`self` and method calls.** Calling through an instance fills in `self`; calling
  through the class doesn't. The test was referencing the function without calling
  it. A method that never uses `self` is a design signal.
  Ref: [Python 3.13 tutorial, 9.3.4 Method Objects](https://docs.python.org/3.13/tutorial/classes.html#method-objects)
- **Chained comparisons.** `MIN < x > MAX` only checks the upper bound (it's
  `MIN < x and x > MAX`). Stating the rule in English first ("out of range if less
  than min **or** greater than max") led to the correct condition.
- **Read the failure message.** `DID NOT RAISE` (missing validation) is a different
  failure from an `assert` mismatch (wrong plan). The n=0 test was failing for the
  first reason, not because of the mutation.
- **Mutation checks.** Reverting to `range(n)` made 3 tests fail, which showed which
  tests actually guard the plan shape.
- **Tests without asserts** only prove "nothing raised". There was nothing else to
  assert for `work=60` because the output didn't depend on `work` yet, which points
  straight at criterion 1.
- **Check types before ranges** so non-ints never reach numeric comparisons.
  `type(x) is not int` correctly rejects `bool` (a subclass of `int`).

## Design decisions (to record in an ADR)
- **Interval:** one block, which knows its type, duration (pick minutes or seconds
  and label it), and position. Likely a class; a `@dataclass` (maybe `frozen=True`)
  was suggested.
  Ref: [Python 3.13 dataclasses](https://docs.python.org/3.13/library/dataclasses.html)
- **No separate `create_interval`:** the Interval constructor already creates one.
- **IntervalPlan:** receives all settings, validates them, and builds the intervals
  in one loop, assigning positions as it goes. It describes the sequence and does
  not change after it's built.
- **Session (US-002):** owns timekeeping and "where the user is". The plan does not
  track progress (Reset and the service/UI split in ADR-002 stay simple).
- **Breaks share the position of the work interval before them.** For N=4 the
  positions are 1, 1, 2, 2, 3, 3, 4, 4.
- **Store data, not display text.** "Work 2 of 4" / "Break 2 of 4" is formatted by
  each screen (US-004, US-011), not stored on the interval.
- Naming follows the glossary: Interval, Interval plan, Session are three distinct
  things.

## Next steps
1. Commit the current green state.
2. Write a short ADR for the Interval / IntervalPlan / Session split.
3. Write the N=4 test (types, durations, positions) first; watch it fail.
4. Refactor to `Interval` + `IntervalPlan`, running pytest often.
5. While parametrizing, add just-outside-the-limit cases (91, 16, 61, 13) and give
   the "pass" tests real asserts once durations exist.
   Ref: [pytest: How to parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)

## Open questions for next time
- Which existing tests will the refactor break, and which should pass unchanged?
  (Predict before refactoring.)
- Minutes or seconds for duration?
- Does IntervalPlan need its own class, or is a list plus a count enough? Decide in the ADR.

## Recurring themes
- Trace by hand before running (this caught the `range` and the `MIN < x > MAX` issue).
- Keep concepts separate: one interval vs. the plan vs. the session.
